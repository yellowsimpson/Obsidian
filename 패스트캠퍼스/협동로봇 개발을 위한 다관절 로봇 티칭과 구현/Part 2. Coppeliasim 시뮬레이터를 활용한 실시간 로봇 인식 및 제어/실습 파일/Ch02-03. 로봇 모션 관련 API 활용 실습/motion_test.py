import Command
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.require('sim')

sim.loadScene('C:/src/resource/coppeliasim/scene/simple_pick_and_place.ttt')

robotHandle = sim.getObject('/UR10')

joints = sim.getObjectsInTree(robotHandle, sim.object_joint_type)[:6]

gripper_handle = sim.getObject('/UR10/RG2')
tip_handle = sim.getObject('/UR10/UR10_tip')
target_handle = sim.getObject('/UR10/UR10_target')
base_handle = sim.getObject('/UR10')

vel = 110 * np.pi/180
accel = 40 * np.pi/180
jerk = 80 * np.pi/180
maxvel = [vel, vel, vel, vel, vel, vel]# Joint1 ~ JOint 6까지의 속도
maxAccel = [accel, accel, accel, accel, accel, accel]# Joint1 ~ JOint 6까지의 속도
maxJerk = [jerk, jerk, jerk, jerk, jerk, jerk]# Joint1 ~ JOint 6까지의 속도

j1 = 90 * np.pi/180 
j2 = 0 * np.pi/180
j3 = -90 * np.pi/180
j4 = 0 * np.pi/180
j5 = 90 * np.pi/180
j6 = 0 * np.pi/180

target_pos_1 = [j1, j2, j3, j4, j5, j6]
target_pos_2 = target_pos_1
target_pos_2[0] = 45 * np.pi/180

sim.startSimulation()
Command.move_joint(sim, joints, tip_handle, target_handle, maxvel, maxAccel, maxJerk, target_pos_1)
Command.move_joint(sim, joints, tip_handle, target_handle, maxvel, maxAccel, maxJerk, target_pos_2)
sim.stopSimulation()