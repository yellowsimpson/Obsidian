from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import numpy as np

client = RemoteAPIClient()
sim = client.require('sim')

object_name = '/UR5'
object_handle = sim.getObject(object_name)

def euler_to_quaternion(roll, pitch, yaw):
    """
    오일러 각도를 쿼터니언(qx, qy, qz, qw)으로 변환하는 함수
    """
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)

    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return [qx, qy, qz, qw]

position = [2, 0, 0]
orientation = euler_to_quaternion(0, 0, 0)
pose = position + orientation

sim.startSimulation()
sim.setObjectPose(object_handle, pose, sim.handle_world)

print("Position:", position)    
sim.wait(7)

sim.stopSimulation()