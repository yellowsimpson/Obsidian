#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray, String
from geometry_msgs.msg import PoseStamped, PoseArray
from nav2_msgs.action import FollowWaypoints
from rclpy.action import ActionClient
from tf2_msgs.msg import TFMessage
from tf_transformations import quaternion_from_euler, quaternion_multiply, euler_from_quaternion, quaternion_matrix, quaternion_inverse
import numpy as np



class TaskManager(Node):
	def __init__(self):
		super().__init__('task_manager')
		self._action_client = ActionClient(self, FollowWaypoints, 'follow_waypoints')
		self.pick_place_pub = self.create_publisher(Float64MultiArray, '/target_point', 10)
		self.pick_place_status_sub = self.create_subscription(
			String, '/pick_place_status', self.pick_place_status_callback, 10
		)
		self.tf_sub = self.create_subscription(
			TFMessage, '/tf', self.tf_callback, 10
		)
		# Subscriptions to individual model pose topics
		self.object1_pose_sub = self.create_subscription(
			PoseArray, '/model/object1/pose', self.object1_pose_callback, 10
		)
		# self.object2_pose_sub = self.create_subscription(
		# 	PoseArray, '/model/object2/pose', self.object2_pose_callback, 10
		# )

		self.wf = 1.0  # World frame
		self.rf = 2.0  # Robot frame

		self.sg = 1.0
		self.tg = 2.0
		
		self.load = 1.0
		self.unload = 2.0
		
		self.pick_waypoints = [(-4.7, 5.6, np.pi)]
		self.drop_waypoints = [(-0.3, 1.2, np.pi)]#, (2.6, -2.7, -np.pi/2)]
		self.robot_drop_positions = [
			(0.3, 0.1, 0.03, 1, 0, 0, 0, self.rf),
			# (0.3, -0.1, 0.03, 1, 0, 0, 0, self.rf),
		]
		self.final_drop_positions = [
			(1., 1.0, 1.214, 0, 0, 0, 1, self.wf),
			# (-3., -2.3, 1.214, 1, 0, 0, 0, self.wf),
		]

		self.pick_place_done = False
		self.navigation_done = False

		self.base_position = None
		self.base_orientation = None
		
		# Initialize object_poses with None, to be updated from ROS 2 topics
		self.object_poses = {
			'object1': None,
			# 'object2': None
		}

	def tf_callback(self, msg):
		for transform in msg.transforms:
			if transform.header.frame_id == 'odom' and transform.child_frame_id == 'base_footprint':
				self.base_position = [
					transform.transform.translation.x,
					transform.transform.translation.y,
					transform.transform.translation.z + 0.55
				]
				self.base_orientation = [
					transform.transform.rotation.x,
					transform.transform.rotation.y,
					transform.transform.rotation.z,
					transform.transform.rotation.w
				]
				# self.get_logger().info(f"{euler_from_quaternion(self.base_orientation)}")

	def object1_pose_callback(self, msg):
		"""Callback for /model/object1/pose topic."""
		if msg.poses:  # Check if the PoseArray contains any poses
			# Extract the first pose (assuming it’s the relevant one)
			pose = msg.poses[0]
			position = [pose.position.x+0.04, pose.position.y, pose.position.z]
			orientation = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
			self.object_poses['object1'] = {'position': position, 'orientation': orientation}
			# self.get_logger().info(f"Updated object1 pose: {self.object_poses['object1']}")
		else:
			self.get_logger().warn("Received empty PoseArray for object1.")

	# def object2_pose_callback(self, msg):
	# 	"""Callback for /model/object2/pose topic."""
	# 	if msg.poses:  # Check if the PoseArray contains any poses
	# 		# Extract the first pose (assuming it’s the relevant one)
	# 		pose = msg.poses[0]
	# 		position = [pose.position.x, pose.position.y, pose.position.z]
	# 		orientation = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
	# 		self.object_poses['object2'] = {'position': position, 'orientation': orientation}
	# 		# self.get_logger().info(f"Updated object2 pose: {self.object_poses['object2']}")
	# 	else:
	# 		self.get_logger().warn("Received empty PoseArray for object2.")



	def compute_ee_frame(self, object_position, object_orientation, grasp_dir):
		"""Transforms the object's pose from world frame to robot's frame."""
		
		# Check if robot's pose is available
		if self.base_position is None or self.base_orientation is None:
			self.get_logger().warn("Base pose not available. Cannot compute EE frame.")
			return None, None
		
		# Convert inputs to numpy arrays for easier manipulation
		p_w = np.array(object_position)  # Object position in world frame
		q_w = np.array(object_orientation)  # Object orientation in world frame
		t_o_r = np.array(self.base_position)  # Robot position in odom frame
		q_o_r = np.array(self.base_orientation)  # Robot orientation in odom frame
		
		# Step 1: Define the rotation from frame_o (odom) to frame_w (world)
		# World frame is odom frame rotated by 90 degrees around z-axis
		R_o_w = np.array([[0, 1, 0],
						[-1,  0, 0],
						[0,  0, 1]])  # Rotation matrix: 90° around z
		
		# Step 2: Transform object's position from frame_w to frame_o
		# frame_o = R_o_w^T * frame_w (since frame_w = R_o_w * frame_o)
		R_w_o = R_o_w.T
		p_o = np.dot(R_w_o, p_w)
		
		# Step 3: Transform object's orientation from frame_w to frame_o
		# Convert rotation matrix to quaternion and get inverse
		q_o_w = quaternion_from_euler(0, 0, np.pi / 2)  # 90° around z
		q_w_o = quaternion_inverse(q_o_w)
		q_o = quaternion_multiply(q_w_o, q_w)
		
		# Step 4: Transform object's position from frame_o to frame_r
		# p_r = R_o_r^T * (p_o - t_o_r)
		R_o_r = quaternion_matrix(q_o_r)[:3, :3]  # Robot's rotation matrix
		p_r = np.dot(R_o_r.T, p_o - t_o_r)

		self.get_logger().info(f"Object in odom frame: pos={p_o}, quat={q_o}")

		# Step 5: Transform object's orientation from frame_o to frame_r
		# q_r = q_o_r^{-1} * q_o
		q_r = quaternion_multiply(quaternion_inverse(q_o_r), q_o)
		
		# Step 6: Adjust orientation based on grasp_dir (if needed)
		if grasp_dir == self.sg:
			# Example: Rotate 90° around x-axis for grasp_dir == 1.0
			grasp_adjust = quaternion_from_euler(np.pi / 2, 0, 0)
			q_r = quaternion_multiply(q_r, grasp_adjust)

		# For grasp_dir == 2.0, no adjustment (identity quaternion)
		
		# Convert outputs to lists for compatibility with your code
		grasp_pos = list(p_r)
		grasp_quat = list(q_r)
		
		# Logging for debugging
		self.get_logger().info(f"Object in world frame: pos={object_position}, quat={object_orientation}")
		self.get_logger().info(f"Robot in odom frame: pos={self.base_position}, quat={self.base_orientation}")
		self.get_logger().info(f"Object in robot frame: pos={grasp_pos}, quat={grasp_quat}")
		# print(1/0)
		
		return grasp_pos, grasp_quat

	def generate_waypoint(self, x, y, theta=0.0):
		wp = PoseStamped()
		wp.header.frame_id = 'map'
		wp.pose.position.x, wp.pose.position.y = x, y
		q = quaternion_from_euler(0, 0, theta)
		wp.pose.orientation.x, wp.pose.orientation.y, wp.pose.orientation.z, wp.pose.orientation.w = q
		return wp

	def ensure_reach_waypoint(self, desired_x, desired_y, threshold=0.5):
		self.get_logger().info(f"Ensuring reach to waypoint ({desired_x}, {desired_y})")
		while rclpy.ok():
			if self.base_position is None:
				self.get_logger().warn("Base position unavailable. Retrying...")
				time.sleep(1.0)
				continue
			error_x = abs(self.base_position[0] - desired_x)
			error_y = abs(self.base_position[1] - desired_y)
			error = np.sqrt(error_x**2 + error_y**2)
			self.get_logger().info(f"Current Position: ({self.base_position[0]}, {self.base_position[1]}), Error: {error:.4f}")
			if error < threshold:
				self.get_logger().info("Base has reached the desired position.")
				break
			self.get_logger().info("Re-issuing navigation command...")
			self.navigate_to_waypoint([self.generate_waypoint(desired_x, desired_y)])
			self.wait_for_navigation()
			time.sleep(1.0)

	def navigate_to_waypoint(self, waypoints):
		goal_msg = FollowWaypoints.Goal()
		goal_msg.poses = waypoints
		self.get_logger().info(f"Sending navigation goal to {waypoints[0].pose.position.x}, {waypoints[0].pose.position.y}")
		self._action_client.wait_for_server()
		self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
		self._send_goal_future.add_done_callback(self.goal_response_callback)

	def goal_response_callback(self, future):
		goal_handle = future.result()
		if not goal_handle.accepted:
			self.get_logger().info('Navigation goal rejected.')
			return
		self.get_logger().info('Navigation goal accepted.')
		self._get_result_future = goal_handle.get_result_async()
		self._get_result_future.add_done_callback(self.get_result_callback)

	def feedback_callback(self, feedback_msg):
		feedback = feedback_msg.feedback
		current_waypoint = feedback.current_waypoint

	def get_result_callback(self, future):
		self.get_logger().info('Navigation completed.')
		self.navigation_done = True

	def wait_for_navigation(self):
		self.navigation_done = False
		self.get_logger().info("Waiting for navigation to complete...")
		while not self.navigation_done:
			rclpy.spin_once(self, timeout_sec=0.1)

	def pick_object(self, start, goal, task):
		self.pick_place_done = False

		if self.base_position is None or self.base_orientation is None:
			self.get_logger().warn("Skipping task due to missing base transform.")
			return

		obj_start_pos, obj_start_orient, obj_start_frame, obj_start_grasp_dir = (start[0], start[1], start[2]), (start[3], start[4], start[5], start[6]),  start[7],  start[8]
		obj_goal_pos, obj_goal_orient, obj_goal_frame, object_goal_grasp_dir = (goal[0], goal[1], goal[2]), (goal[3], goal[4], goal[5], goal[6]), goal[7], goal[8]

		if obj_start_frame == self.wf:
			start_xyz, start_quat = self.compute_ee_frame(obj_start_pos, obj_start_orient, obj_start_grasp_dir)
		else:
			start_xyz, start_quat = obj_start_pos, obj_start_orient
		start = [*start_xyz, *start_quat]

		if obj_goal_frame == self.wf:
			goal_xyz, goal_quat = self.compute_ee_frame(obj_goal_pos, obj_goal_orient, object_goal_grasp_dir)
		else:
			goal_xyz, goal_quat = obj_goal_pos, obj_goal_orient
		goal = [*goal_xyz, *goal_quat]

		self.get_logger().info(f"Pick-and-place from {start} to {goal}...")
		

		target_point = Float64MultiArray(data=start + goal + [task])
		self.pick_place_pub.publish(target_point)

	def pick_place_status_callback(self, msg):
		if msg.data == "DONE":
			self.pick_place_done = True
			self.get_logger().info("Pick and place operation completed.")

	def wait_for_pick_place_completion(self):
		self.get_logger().info("Waiting for pick/place operation to complete...")
		while not self.pick_place_done:
			rclpy.spin_once(self, timeout_sec=0.1)

	def send_goal(self):

		self.get_logger().info("Starting pick phase...")
		pick_loc = self.pick_waypoints[0]
		self.navigate_to_waypoint([self.generate_waypoint(*pick_loc)])
		self.wait_for_navigation()
		self.ensure_reach_waypoint(pick_loc[0], pick_loc[1])

		self.pick_object(
			(*self.object_poses['object1']['position'], *self.object_poses['object1']['orientation'], self.wf, self.sg),
			(*self.robot_drop_positions[0], self.tg), 
			self.load
		)
		self.wait_for_pick_place_completion()

		# self.pick_object(
		# 	(*self.object_poses['object2']['position'], *self.object_poses['object2']['orientation'], self.wf, self.sg),
		# 	(*self.robot_drop_positions[1], self.tg), 
		# 	self.load
		# )
		# self.wait_for_pick_place_completion()

		# self.get_logger().info("All objects loaded onto robot.")

		for i, (drop_loc, robot_pos, final_pos) in enumerate(zip(self.drop_waypoints, self.robot_drop_positions, self.final_drop_positions)):
			self.get_logger().info(f"Delivering object {i+1} to drop-off location {drop_loc}")
			self.navigate_to_waypoint([self.generate_waypoint(*drop_loc)])
			self.wait_for_navigation()
			self.ensure_reach_waypoint(drop_loc[0], drop_loc[1])
			self.pick_object((*robot_pos, self.tg), (*final_pos, self.sg), self.unload)
			self.wait_for_pick_place_completion()

		self.get_logger().info("All objects delivered. Task completed.")
		rclpy.shutdown()

def main(args=None):
	rclpy.init(args=args)
	task_manager = TaskManager()
	task_manager.send_goal()
	rclpy.spin(task_manager)

if __name__ == '__main__':
	main()