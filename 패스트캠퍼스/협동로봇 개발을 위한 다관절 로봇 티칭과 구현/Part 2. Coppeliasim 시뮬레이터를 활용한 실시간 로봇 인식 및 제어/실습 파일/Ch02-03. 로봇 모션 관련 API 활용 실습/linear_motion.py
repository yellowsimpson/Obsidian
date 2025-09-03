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

vel = 0.5
accel = 0.5
jerk = 0.5

maxvel = [vel, vel, vel, 1]
maxacc = [accel, accel, accel, 1]
maxjerk = [jerk, jerk, jerk, 1]

current_pos = [- 0.17246, 0.6885, 1.237]
target_pos = [- 0.17246, 0.6885, 1.037]

sim.startSimulation()
Command.move_linear(sim, tip_handle, target_handle, maxvel, maxacc, maxjerk, target_pos)
Command.close_gripper(sim, "RG2_open")
Command.move_linear(sim, tip_handle, target_handle, maxvel, maxacc, maxjerk, current_pos)
Command.open_gripper(sim, "RG2_open")
sim.stopSimulation()