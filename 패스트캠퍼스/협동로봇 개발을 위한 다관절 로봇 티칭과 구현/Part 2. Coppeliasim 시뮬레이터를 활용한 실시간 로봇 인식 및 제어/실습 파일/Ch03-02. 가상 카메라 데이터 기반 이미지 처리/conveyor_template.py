from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import cv2
import numpy as np
import time

client = RemoteAPIClient()
sim = client.require('sim')

if sim.getSimulationState() == sim.simulation_advancing_running:
    sim.stopSimulation()
    time.sleep(0.1)

sim.loadScene('C:/src/resource/coppeliasim/scene/conveyor_template.ttt')

vision_sensor_handle = sim.getObject('/visionSensor')
template_path = 'cylinder_template.jpg'
template = cv2.imread(template_path)
template_height, template_width = template.shape[:2]
flag = 0
sim.startSimulation()

while (t := sim.getSimulationTime()) < 30:
    if int(t) != flag:
        if int(t) % 2 == 0:
            shape = sim.createPrimitiveShape(sim.primitiveshape_cylinder, [0.1, 0.1, 0.025], 0)
            sim.setObjectPosition(shape, [0, 0, 0.405], sim.handle_world)
            sim.setShapeMass(shape, 1)
            sim.setBoolProperty(shape, 'respondable', True)
            sim.setBoolProperty(shape, 'dynamic', True)
            flag = int(t)

    img, [resX, resY] = sim.getVisionSensorImg(vision_sensor_handle)
    img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for loc in zip(*locations[::-1]):
        top_left = loc 
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 1)
    cv2.imshow('', img)
    cv2.waitKey(1)  

cv2.imwrite('vision_sensor_image.jpg', img)
sim.stopSimulation()