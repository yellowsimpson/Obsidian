from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import cv2
import numpy as np

client = RemoteAPIClient()
sim = client.require('sim')

sim.loadScene('C:/src/resource/coppeliasim/scene/vision_realsense_connection.ttt')


vision_sensor_handle = sim.getObject('/UR10/visionSensor')

sim.startSimulation()
while(t := sim.getSimulationTime()) < 3:
    img, [resX, resY] = sim.getVisionSensorImg(vision_sensor_handle)
    img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
    cv2.imshow('', img)
    cv2.waitKey(1)
sim.stopSimulation()

cv2.destroyAllWindows()