from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import cv2
import numpy as np

client = RemoteAPIClient()
sim = client.require('sim')

sim.loadScene('C:/src/resource/coppeliasim/scene/colorDetection.ttt')

vision_sensor_handle = sim.getObject('/visionSensor')

def findContourwithColor(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower_red1 = np.array([0, 70, 70])  # 빨간색의 첫 번째 범위
    # upper_red1 = np.array([10, 255, 255]) 
    # lower_red2 = np.array([170, 70, 70])  # 빨간색의 두 번째 범위
    # upper_red2 = np.array([180, 255, 255])

    lower_red1 = np.array([110, 70, 70])  # 빨간색의 첫 번째 범위
    upper_red1 = np.array([130, 255, 255]) 

    mask = cv2.inRange(hsv_img, lower_red1, upper_red1)
    #mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    #mask = cv2.bitwise_or(mask1, mask2)

    red_area = cv2.bitwise_and(img, img, mask=mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # 너무 작은 형상은 제외 (여기서는 100 이상)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 형상 주변에 녹색 사각형
    return img

sim.startSimulation()
while(t := sim.getSimulationTime()) < 10:
    img, [resX, resY] = sim.getVisionSensorImg(vision_sensor_handle)
    img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
    if t < 1:
        cv2.imwrite('vision_sensor_image.jpg', img)
    findContourwithColor(img)
    cv2.imshow('', img)
    cv2.waitKey(1)
sim.stopSimulation()

cv2.destroyAllWindows()