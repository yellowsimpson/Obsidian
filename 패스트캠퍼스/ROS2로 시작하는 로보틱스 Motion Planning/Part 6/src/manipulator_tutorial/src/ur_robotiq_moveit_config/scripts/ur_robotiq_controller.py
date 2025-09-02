#!/usr/bin/env python3

import time
import threading
import rclpy
import numpy as np
from rclpy.node import Node
from rclpy.logging import get_logger
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64MultiArray, String
from moveit.core.robot_state import RobotState  # Correct import
from moveit.planning import MoveItPy, MultiPipelinePlanRequestParameters
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive
from moveit.core.kinematic_constraints import construct_joint_constraint
from geometry_msgs.msg import Pose
from moveit_msgs.msg import Constraints, JointConstraint



def plan_and_execute(robot, planning_component, logger, 
					single_plan_parameters=None,
					multi_plan_parameters=None,
					sleep_time=0.0):
	
	logger.info("Planning trajectory")

	# constraints = Constraints()
	# constraints.name = "shoulder_lift_joint"
	# joint_constraint = JointConstraint()
	# joint_constraint.joint_name = "shoulder_lift_joint"
	# joint_constraint.position = -np.pi/2  # Target position (e.g., 0 for elbow down)
	# joint_constraint.tolerance_above = np.pi/9  # Range above target
	# joint_constraint.tolerance_below = np.pi*8/9  # Range below target
	# joint_constraint.weight = 1.0  # Importance of constraint

	# constraints.joint_constraints.append(joint_constraint)
	# planning_component.set_path_constraints(constraints)


	# plan_result = planning_component.plan()
	plan_result = False
	if multi_plan_parameters is not None:
			plan_result = planning_component.plan(
					multi_plan_parameters=multi_plan_parameters
			)
	elif single_plan_parameters is not None:
			plan_result = planning_component.plan(
					single_plan_parameters=single_plan_parameters
			)
	else:
			plan_result = planning_component.plan()

	if not plan_result:
		logger.error("Planning failed. No valid trajectory generated.")
		return False
	logger.info("Executing plan")
	robot_trajectory = plan_result.trajectory
	if robot_trajectory:
		robot.execute(robot_trajectory, controllers=[])
		time.sleep(sleep_time)
		return True
	else:
		logger.error("Execution failed. No valid trajectory.")
		return False

class Controller(Node):
	def __init__(self):
		super().__init__('commander')
		self.get_logger().info("\n\n\nInitialize Manipulator\n\n\n")

		self.subscription = self.create_subscription(
			Float64MultiArray, '/target_point', self.listener_callback, 10
		)
		self.status_pub = self.create_publisher(String, '/pick_place_status', 10)

		self.pose_goal = PoseStamped()
		self.pose_goal.header.frame_id = "base_link"

		self.ur = MoveItPy(node_name="moveit_py")
		self.get_logger().info("\n\n\nSuccessfully called moveit py node\n\n\n")
		self.ur_arm = self.ur.get_planning_component("ur_manipulator")
		self.ur_hand = self.ur.get_planning_component("robotiq_2f_85_gripper")
		self.logger = get_logger("moveit_py.pose_goal")

		robot_model = self.ur.get_robot_model()
		self.robot_state = RobotState(robot_model)

		# Heights and offsets
		self.backoff_dist = 0.4
		self.grasp_dist = 0.15
		self.carrying_height = 0.4

		# Side grasping orientation (w, x, y, z)
		self.side_grasp_orientation = (0.7071067811865476, 0.0, 0.7071067811865475, 0.0)
		self.top_grasp_orientation = (1., 0., 0., 0.)

		time.sleep(10)
		self.setup_workspace(self.ur)

	def setup_workspace(self, moveit):
		with moveit.get_planning_scene_monitor().read_write() as scene:
			objects_to_add = [
				("base", [1.5, 1.5, 0.5], [0., 0., 0.75]),
			]
			for name, size, position in objects_to_add:
				self.add_box(scene, name, size, position, base=True)
				self.get_logger().info(f"\tSuccessful placement of {name}")
			scene.current_state.update()

	def add_box(self, scene, name, size, position, base=False):
		co = CollisionObject()
		co.header.frame_id = 'world'
		co.id = name
		box = SolidPrimitive()
		box.type = SolidPrimitive.BOX
		box.dimensions = size
		co.primitives.append(box)
		pose = Pose()
		pose.position.x, pose.position.y, pose.position.z = position
		co.primitive_poses.append(pose)
		co.operation = CollisionObject.ADD
		scene.apply_collision_object(co)

	def publish_status(self, status_msg):
		status = String()
		status.data = status_msg
		self.status_pub.publish(status)
		self.get_logger().info(f"[DEBUG] Publishing pick-place completion: {status_msg}")

	def move_to(self, x, y, z, xo, yo, zo, wo):
		self.ur_arm.set_start_state_to_current_state()
		self.pose_goal.pose.position.x = x
		self.pose_goal.pose.position.y = y
		self.pose_goal.pose.position.z = z
		self.pose_goal.pose.orientation.x = xo
		self.pose_goal.pose.orientation.y = yo
		self.pose_goal.pose.orientation.z = zo
		self.pose_goal.pose.orientation.w = wo
		self.ur_arm.set_goal_state(pose_stamped_msg=self.pose_goal, pose_link="tool0")
		# initialise multi-pipeline plan request parameters
		multi_pipeline_plan_request_params = MultiPipelinePlanRequestParameters(
				self.ur, ["ompl_rrtc", "pilz_lin", "chomp_planner", "ompl_rrt_star", "stomp_planner"]
		)
		return plan_and_execute(self.ur, self.ur_arm, self.logger, multi_plan_parameters=multi_pipeline_plan_request_params, sleep_time=1.)

	def gripper_action(self, action):
		self.ur_hand.set_start_state_to_current_state()
		if action == 'open':
			joint_values = {"robotiq_85_left_knuckle_joint": 0.01}
		elif action == 'close':
			joint_values = {"robotiq_85_left_knuckle_joint": 0.65}
		else:
			self.get_logger().info("No such action")
			return False
		self.robot_state.joint_positions = joint_values
		joint_constraint = construct_joint_constraint(
			robot_state=self.robot_state,
			joint_model_group=self.ur.get_robot_model().get_joint_model_group("robotiq_2f_85_gripper"),
		)
		self.ur_hand.set_goal_state(motion_plan_constraints=[joint_constraint])
		return plan_and_execute(self.ur, self.ur_hand, self.logger, sleep_time=1.)

	def listener_callback(self, data):
		self.get_logger().info(f"Received target point: {[f'{x:.2f}' for x in data.data]}")
		self.publish_status("IN_PROGRESS")

		if data.data[-1] == 1.0:
			# Load mode
			start_x, start_y, start_z, start_xo, start_yo, start_zo, start_wo = data.data[0:7]
			goal_x, goal_y, goal_z, goal_xo, goal_yo, goal_zo, goal_wo = data.data[7:14]
			start_orientation = (start_xo, start_yo, start_zo, start_wo)
			goal_orientation = (goal_xo, goal_yo, goal_zo, goal_wo)

			valid = True

			valid = valid and self.move_to(0.4, 0.0, self.carrying_height, 1., 0., 0., 0.)

			# Backoff position (approach from side, along X-axis)
			start_backoff_x = start_x - self.backoff_dist
			self.get_logger().info(f"\n\nMoving to backoff position {start_backoff_x, start_y, start_z}\n\n")
			valid = valid and self.move_to(start_backoff_x, start_y, start_z, *start_orientation)

			print("\n\n\n\n\n\n")
			# Open gripper
			self.get_logger().info("Opening gripper")
			valid = valid and self.gripper_action("open")

			# Move to pick position (side grasp)
			start_grasp_x = start_x - 0.1
			self.get_logger().info(f"\n\nMoving to pick position {start_grasp_x, start_y, start_z}")
			valid = valid and self.move_to(start_grasp_x, start_y, start_z, *start_orientation)

			# Grasp (close gripper)
			self.get_logger().info("Grasping object")
			valid = valid and self.gripper_action("close")

			# Backup after grasping
			self.get_logger().info(f"Back up after grasp {start_backoff_x, start_y, start_z}")
			valid = valid and self.move_to(start_backoff_x, start_y, start_z, *start_orientation)

			# Move to goal backoff position
			goal_backoff_z = goal_z + self.backoff_dist
			self.get_logger().info("Moving to goal backoff position")
			valid = valid and self.move_to(goal_x, goal_y, goal_backoff_z, *goal_orientation)

			# Lower to place position
			goal_grasp_z = goal_z + self.grasp_dist
			self.get_logger().info("Lowering to place position")
			valid = valid and self.move_to(goal_x, goal_y, goal_grasp_z, *goal_orientation)

			# Release (open gripper)
			self.get_logger().info("Releasing object")
			valid = valid and self.gripper_action("open")

			# Backup after placing
			self.get_logger().info("Backing up after place")
			valid = valid and self.move_to(goal_x, goal_y, goal_backoff_z, *goal_orientation)

			valid = valid and self.move_to(0.4, 0.0, self.carrying_height, 1., 0., 0., 0.)

		elif data.data[-1] == 2.0:
			# Unload mode
			start_x, start_y, start_z, start_xo, start_yo, start_zo, start_wo = data.data[0:7]
			goal_x, goal_y, goal_z, goal_xo, goal_yo, goal_zo, goal_wo = data.data[7:14]
			start_orientation = (start_xo, start_yo, start_zo, start_wo)
			goal_orientation = (goal_xo, goal_yo, goal_zo, goal_wo)

			valid = True

			valid = valid and self.move_to(0.4, 0.0, self.carrying_height, 1., 0., 0., 0.)

			# Backoff position (approach from side, along Z-axis)
			start_backoff_z = start_z + self.backoff_dist
			self.get_logger().info("Moving to backoff position")
			valid = valid and self.move_to(start_x, start_y, start_backoff_z, *start_orientation)

			# Open gripper
			self.get_logger().info("Opening gripper")
			valid = valid and self.gripper_action("open")

			# Move to pick position (top grasp)
			self.get_logger().info("Moving to pick position")
			start_graspf_z = start_z + self.grasp_dist
			valid = valid and self.move_to(start_x, start_y, start_graspf_z, *start_orientation)

			# Grasp (close gripper)
			self.get_logger().info("Grasping object")
			valid = valid and self.gripper_action("close")

			# Backoff position (approach from side, along Z-axis)
			self.get_logger().info("Moving to backoff position")
			valid = valid and self.move_to(start_x, start_y, start_backoff_z, *start_orientation)

			# Backup after grasping
			backoff_x = goal_x - self.backoff_dist
			self.get_logger().info("Moving to backoff position")
			valid = valid and self.move_to(backoff_x, goal_y, goal_z, *goal_orientation)

			# Move to release position (side grasp)
			self.get_logger().info("Moving to pick position")
			goal_grasp_x = goal_x - self.grasp_dist
			valid = valid and self.move_to(goal_grasp_x, goal_y, goal_z, *goal_orientation)

			# Release (release gripper)
			self.get_logger().info("Grasping object")
			valid = valid and self.gripper_action("open")

			# Backup after unloading
			self.get_logger().info("Moving to backoff position")
			valid = valid and self.move_to(backoff_x, goal_y, goal_z, *goal_orientation)

			valid = valid and self.move_to(0.4, 0.0, self.carrying_height, 1., 0., 0., 0.)

		elif data.data[-1] == 3.0:
			# Simple Pick and Place
			start_x, start_y, start_z, start_xo, start_yo, start_zo, start_wo = data.data[0:7]
			goal_x, goal_y, goal_z, goal_xo, goal_yo, goal_zo, goal_wo = data.data[7:14]
			start_orientation = (start_xo, start_yo, start_zo, start_wo)
			goal_orientation = (goal_xo, goal_yo, goal_zo, goal_wo)

			valid = True

			valid = valid and self.move_to(0.4, 0.0, self.carrying_height, 1., 0., 0., 0.)

			# Backoff position (approach from side, along X-axis)
			start_backoff_z = start_z + 0.25
			self.get_logger().info(f"\n\nMoving to backoff position {start_x, start_y, start_backoff_z}\n\n")
			valid = valid and self.move_to(start_x, start_y, start_backoff_z, *start_orientation)

			print("\n\n\n\n\n\n")
			# Open gripper
			self.get_logger().info("Opening gripper")
			valid = valid and self.gripper_action("open")

			# Move to pick position (top grasp)
			start_grasp_z = start_z + 0.15
			self.get_logger().info(f"\n\nMoving to pick position {start_x, start_y, start_grasp_z}")
			valid = valid and self.move_to(start_x, start_y, start_grasp_z, *start_orientation)

			# Grasp (close gripper)
			self.get_logger().info("Grasping object")
			valid = valid and self.gripper_action("close")

			# Backup after grasping
			self.get_logger().info(f"Back up after grasp {start_x, start_y, start_backoff_z}")
			valid = valid and self.move_to(start_x, start_y, start_backoff_z, *start_orientation)

			# Move to goal backoff position
			goal_backoff_z = goal_z + 0.25
			self.get_logger().info("Moving to goal backoff position")
			valid = valid and self.move_to(goal_x, goal_y, goal_backoff_z, *goal_orientation)

			# Lower to place position
			goal_grasp_z = goal_z + 0.15
			self.get_logger().info("Lowering to place position")
			valid = valid and self.move_to(goal_x, goal_y, goal_grasp_z, *goal_orientation)

			# Release (open gripper)
			self.get_logger().info("Releasing object")
			valid = valid and self.gripper_action("open")

			# Backup after placing
			self.get_logger().info("Backing up after place")
			valid = valid and self.move_to(goal_x, goal_y, goal_backoff_z, *goal_orientation)

			valid = valid and self.move_to(0.4, 0.0, self.carrying_height, 1., 0., 0., 0.)


		if valid:
			self.publish_status("DONE")
		else:
			self.publish_status("FAILED")

if __name__ == '__main__':
	rclpy.init(args=None)
	controller = Controller()
	executor = rclpy.executors.MultiThreadedExecutor()
	executor.add_node(controller)
	executor_thread = threading.Thread(target=executor.spin, daemon=True)
	executor_thread.start()
	rate = controller.create_rate(2)
	try:
		while rclpy.ok():
			rate.sleep()
	except KeyboardInterrupt:
		pass
	rclpy.shutdown()
	executor_thread.join()