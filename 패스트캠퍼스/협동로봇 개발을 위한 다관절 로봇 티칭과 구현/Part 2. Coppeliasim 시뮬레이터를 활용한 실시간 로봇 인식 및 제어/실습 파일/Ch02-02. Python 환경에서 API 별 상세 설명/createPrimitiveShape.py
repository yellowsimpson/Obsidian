from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.require('sim')

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


sim.startSimulation()

position = [0, 0, 0.5]
orientation = euler_to_quaternion(0, 0, 0)
pose = position + orientation

shape = sim.createPrimitiveShape(sim.primitiveshape_cuboid, [0.3, 0.2, 0.15], 0)
sim.setObjectPose(shape, pose, sim.handle_world)
sim.setShapeMass(shape, 1)
sim.setBoolProperty(shape, 'respondable', True)
sim.setBoolProperty(shape, 'dynamic', True)

sim.wait(10)
sim.stopSimulation()