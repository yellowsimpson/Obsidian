import time
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

def open_gripper(sim, name):
    sim.setInt32Signal(name, 1)
    time.sleep(1)

def close_gripper(sim, name):
    sim.setInt32Signal(name, 0)
    time.sleep(1)

def move_joint(sim, joint_handles, tip_handle, target_handle, maxVel, maxAccel, maxJerk, targetConf):
    current_pose = sim.getObjectPose(tip_handle) #tip handle(dummy)를 현재 위치를 가져온다.
    sim.setObjectPose(target_handle, current_pose, sim.handle_world) #target handle(dummy)를 현재 위치로 보낸다.

    currentConf = []
    for i in range(len(joint_handles)):
        currentConf.append(sim.getJointPosition(joint_handles[i]))
    params = {}
    params['joints'] = joint_handles
    params['targetPos'] = targetConf
    params['maxVel'] = maxVel
    params['maxAccel'] = maxAccel
    params['maxJerk'] = maxJerk
    sim.moveToConfig(params) #Joint motion command

    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)    
    sim.wait(0.1)
    
def move_linear(sim, tip_handle, target_handle, maxVel, maxAccel, MaxJerk, target_pos) :
    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)

    target_pose = current_pose.copy()
    target_pose[0] = target_pos[0]
    target_pose[1] = target_pos[1]
    target_pose[2] = target_pos[2]

    params = {
        "object": target_handle,
        "targetPose": target_pose,
        "maxVel": maxVel,
        "maxAccel": maxAccel,
        "maxJerk": MaxJerk,
    }
    print("moveToPose() 호출 시 params:", params)

    try:
        data = sim.moveToPose(params)
    except Exception as e:
        print("moveToPose 실행 오류:", e)
