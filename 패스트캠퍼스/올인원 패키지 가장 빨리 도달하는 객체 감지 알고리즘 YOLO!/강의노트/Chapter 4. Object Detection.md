# CH04-01. R-CNN, Rol,NMS, mAP, Selective Search, Bounding-box regressor

1. Reguib Orioisak
2. Region Classification


Object detection
1. RoI(Region of Interest)(관심 영역) = Selective search
2. Object, No object = Objectness score
3. Bounding box prediction (Bbox regression)
4. Class prediction of each box
5. Non-maximum suprresion(NMS)

NMS
1. If Class score < C. Return
2. Sort(Prediction of predicted boxes)
3. boxes, IoU list = IoU(predicted boxes, ground truth boxes)
4. Remove (boxes, IoU list, NMS tolerance)


IoU(Intersction over union): 정확한 부분을 bounding box하기 위한 부분
IoU = Area of Overlap(겹치는 부분) / Area of Union(전체 부분)

```python
def calc_iou(b1, b2):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(b1[0], b2[0])
    yA = max(b1[1], b2[1])
    xB = min(b1[2], b2[2])
    yB = min(b1[3], b2[3])

    # compute the area of intersection rectangle
    area_intersect = (xB - xA) * (yB - yA)

    # Calculate area of boxes
    area_b1 = (b1[2] - b1[0]) * (b1[3] - b1[1])
    area_b2 = (b2[2] - b2[0]) * (b2[3] - b2[1])

    # areas - the intersection area
    epsilon = 1e-6
    iou = area_intersect / float(area_b1 + area_b2 - area_intersect + epsilon)

    return iou
```

FPS(Frames per second): 영상에서 1초 동안 표시되는 이미지(프레임)의 개수를 나타내는 단위

Recall and Precision
- TP(True Positive)
- FP(False Positive)
- TN(True Negative)
- FN(False Negative)

- recasll(재현율) = TP / (TP + FN)
- precision(정밀도) = TP / (TP + FP)  -> 1에 가까워 질수록 정밀도가 올라감


RP curve
mAP 

## R-CNN
1. ROI Extraction
2. Reature Extraction with CNN
3. Classification with SVN
4. BBox prediction with regressor

Disadvantage
- Skiw  RoI over 2000 > CNN
- Separated process. R-CNN, SVN, Bbox reg
- Large storage volume of extracted features


**핵심 원리:**

- 이미지에서 **Selective Search** 알고리즘으로 약 2000개의 후보 영역(region proposals)을 생성.
- 각 영역을 CNN에 입력하여 **특징(feature)** 추출 후, SVM으로 객체 분류.
- 경계박스(Bounding Box) 보정 회귀(regression)도 따로 수행.

**특징:**
- 정확도는 높지만 **속도가 매우 느림** (한 이미지 처리에 수 초 걸림).
- 완전한 end-to-end 학습 아님 (단계별 따로 학습: CNN, SVM, bbox regression).
## Fast R-CNN
입력 이미지에서 CNN 하지 말고 
ConvNet을 만들어서 RoI를 만들어서 잘라 넣자!

1. Full images > Feature extreaction with CovNet
2. RoI from feature map 
3. RoI Pooling to fix region size (H x W) > FCs
4. FC > Softmax for classification probability of RoI list
5. FC > Bbox regression
	Lcls(LOSS of classification) + Lloc(LOSS of location)

Disadvantage
- Separated selective search

Ross Girshick 이 개발한 소스 아래 링크에 다 있어!!
https://github.com/rbgirshick/fast-rcnn 

**핵심 원리:**

- Selective Search로 region proposal은 그대로 사용.
- 하지만 이미지를 CNN에 **한 번만 통과**시켜 feature map을 얻고,  
    각 ROI(Region of Interest)에 대해 **RoI Pooling**으로 특징 추출 후 분류 + 회귀를 **동시에** 수행.

**특징:**
- CNN 한 번만 수행 → **속도 대폭 개선.**
- 분류와 박스 회귀를 **end-to-end 학습** 가능.
- 여전히 **region proposal 단계는 느림** (Selective Search).

# CH04-02. Fast R-CNN, Faster R-CNN, SDD, YOLOv1

##  Faster R-CNN
개발자: Shaoging Ren
개발년도: 2015년 

Selective search -> RPN(region proposal network attention network)

RPN output = {objectness score, Bbox}

Model = VGG16 (MobileNet, DenseNet, ResNet152)

1. Feature extraction
2. RPN
3. RoI pooling
4. Classification
5. Bbox regression

![[스크린샷 2025-10-09 오후 11.57.18.png]]

**핵심 원리:**
- Region Proposal도 CNN이 하도록 개선 → **RPN (Region Proposal Network)** 도입.
- CNN feature map에서 anchor box 기반으로 candidate box를 예측.

**특징:**
- 완전한 **end-to-end 구조.**
- 속도와 정확도 둘 다 개선.
- 여전히 2단계 구조 (proposal → classification).
## SSD
개발자: Wei Liu
개발 년도: 2016년

SSD300 = 59fps, mAP 74.3%
SSD512 (512 x 512) = 22fps, mAP 76.8%

Feature extraction VGG16
Multi-scale conv
NMS

Output = {cx, xy, w, h, objectness, C1...Cn}

![[스크린샷 2025-10-10 오전 12.02.59.png]]

```python
def VGG16_SSD(img_height=300, img_width=300, img_channels=3):
    x1 = Input(shape=(img_height, img_width, img_channels))
    l2_reg = 0.0005

    conv1_1 = Conv2D(64, (3, 3), activation='relu', padding='same')(x1)
    conv1_2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv1_1)
    pool1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same')(conv1_2)

    conv2_1 = Conv2D(128, (3, 3), activation='relu', padding='same')(pool1)
    conv2_2 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv2_1)
    pool2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same')(conv2_2)

    conv3_1 = Conv2D(256, (3, 3), activation='relu', padding='same')(pool2)
    conv3_2 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv3_1)
    conv3_3 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv3_2)
    pool3 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same')(conv3_3)

    conv4_1 = Conv2D(512, (3, 3), activation='relu', padding='same')(pool3)
    conv4_2 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv4_1)
    conv4_3 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv4_2)
    pool4 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same')(conv4_3)

    conv5_1 = Conv2D(512, (3, 3), activation='relu', padding='same')(pool4)
    conv5_2 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv5_1)
    conv5_3 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv5_2)
    pool5 = MaxPooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(conv5_3)

    model = Model(inputs=x1, outputs=pool5)
    return model
```


**핵심 원리:**
- Faster R-CNN처럼 후보 영역을 따로 만들지 않음.
- CNN feature map의 여러 스케일에서 **bounding box와 class를 동시에 예측**.
- 다양한 크기의 객체 탐지를 위해 multi-scale feature 사용.
    
**특징:**
- “Single Shot” → 한 번의 CNN forward로 detection 완료.
- 빠르고 실시간 가능.
- 작은 물체 검출은 다소 약함.
## YOLO
개발자: Joseph Redmon 
개발 년도: 2016년

![[스크린샷 2025-10-10 오전 12.13.29.png]]

github링크: https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO

```python
class YoloLoss(nn.Module):
    def forward(self, self, predictions, target):
        predictions = predictions.reshape(-1, self.S, self.S, self.C + self.B * 5)

        iou_b1 = intersection_over_union(predictions[..., 21:25], target[..., 21:25])
        iou_b2 = intersection_over_union(predictions[..., 26:30], target[..., 21:25])
        ious = torch.cat((iou_b1.unsqueeze(0), iou_b2.unsqueeze(0)), dim=0)
        iou_maxes, bestbox = torch.max(ious, dim=0)  # max IoU box, the box index. bestbox[] == 1 or 0
        exists_box = target[..., 20].unsqueeze(3)    # in paper this is I_obj_i

        box_predictions = exists_box * (
            bestbox * predictions[..., 26:30] + (1 - bestbox) * predictions[..., 21:25]
        )
        box_targets = exists_box * target[..., 21:25]

        # bbox W, H loss = MSE(pred box, target box)
        # Take sqrt of width, height of boxes to ensure stability
        box_predictions[..., 2:4] = torch.sign(box_predictions[..., 2:4]) * torch.sqrt(
            torch.abs(box_predictions[..., 2:4]) + 1e-6
        )
        box_targets[..., 2:4] = torch.sqrt(box_targets[..., 2:4])

        box_loss = self.mse(
            torch.flatten(box_predictions, end_dim=-2),
            torch.flatten(box_targets, end_dim=-2),
        )

        pred_box = (
            bestbox * predictions[..., 25:26] + (1 - bestbox) * predictions[..., 20:21]
        )
        object_loss = self.mse(
            torch.flatten(exists_box * pred_box),
            torch.flatten(exists_box * target[..., 20:21]),
        )

        no_object_loss = self.mse(
            torch.flatten((1 - exists_box) * predictions[..., 20:21], start_dim=1),
            torch.flatten((1 - exists_box) * target[..., 20:21], start_dim=1),
        )
        no_object_loss += self.mse(
            torch.flatten((1 - exists_box) * predictions[..., 25:26], start_dim=1),
            torch.flatten((1 - exists_box) * target[..., 20:21], start_dim=1),
        )

        class_loss = self.mse(
            torch.flatten(exists_box * predictions[..., :20], end_dim=-2),
            torch.flatten(exists_box * target[..., :20], end_dim=-2),
        )

        loss = (
            self.lambda_coord * box_loss
            + object_loss
            + self.lambda_noobj * no_object_loss
            + class_loss
        )

        return loss
```

**핵심 원리:**

- 이미지를 **그리드로 분할**, 각 그리드 셀에서:
    - Bounding box 좌표,
    - Confidence score,
    - 클래스 확률을 **한 번에 예측**.
- 완전한 end-to-end 구조.
    
**특징:**
- 매우 빠름 (실시간 영상 가능).
- 초기 버전은 정확도가 다소 낮았지만, v3~v8로 오면서 **정확도·속도 모두 크게 향상**.
- 최근엔 **anchor-free**, **Transformer 기반(YOLOv8, YOLOv9)** 구조까지 발전.



##  모델 비교표

|구분|제안 연도|주요 아이디어|Region Proposal 방식|속도|정확도|End-to-End 학습|대표 특징|
|---|---|---|---|---|---|---|---|
|**R-CNN**|2014|후보영역 + CNN + SVM|Selective Search (외부)|❌ 느림|✅ 높음|❌ 불가|3단계 파이프라인|
|**Fast R-CNN**|2015|CNN 한 번, RoI Pooling|Selective Search (외부)|⚙️ 중간|✅ 높음|⚙️ 부분|End-to-end 가능, proposal은 외부|
|**Faster R-CNN**|2016|RPN으로 proposal도 CNN이 처리|RPN (내부 CNN)|⚡ 빠름|✅ 매우 높음|✅ 가능|정확도 높은 2단계 구조|
|**SSD**|2016|Multi-scale feature map 예측|없음 (Single shot)|⚡⚡ 빠름|⚙️ 중간~높음|✅ 가능|작은 객체 다소 약함|
|**YOLO**|2016~|Grid 기반 전체 예측|없음 (Single shot)|⚡⚡⚡ 매우 빠름|✅ 높음 (v8 이상)|✅ 가능|실시간 검출, 간결한 구조|

# CH04-03. Practice_codereivew_bbox_regression

< train.py 코드 일부분>
```python
# VGG의 출력층을 완전연결(FC) 평활화 레이어와 연결.
flatten = vgg.output
flatten = Flatten()(flatten) #https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten

  

# FC층을 밀집층(128)-(64)-(32)-(4)로 연결
# 결론적으로 밀집층(4)가 각 bbox 좌표의 예측값이 되도록, 모델의 출력을 만듬.
# 마지막층은 sigmoid로 활성화시킴.
bboxHead = Dense(128, activation="relu")(flatten)
bboxHead = Dense(64, activation="relu")(bboxHead)
bboxHead = Dense(32, activation="relu")(bboxHead)
bboxHead = Dense(4, activation="sigmoid")(bboxHead)

# 모델 입력은 vgg.input 층 사용.
# bbox 회귀식 계산을 위해, 모델은 미세 조정 될 것임.
# vgg.input.shape = (None, 224, 224, 3)
# output=bboxhead.shape = (None, 4)
model = Model(inputs=vgg.input, outputs=bboxHead)
```
-> 이부분의 코드가 모델 학습하고 만드는 가장 중요한 부분
### <train.py>

경로: notebook-001/4_object_detection/3_bounding-box-regression/train.py
```python


# USAGE
# python train.py

import config
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


# CSV 파일 로딩
print("[INFO] loading dataset...")
rows = open(config.ANNOTS_PATH).read().strip().split("\n")

data = []        # 이미지 데이터 리스트
targets = []     # bbox 좌표
filenames = []   # 각 이미지 파일명

# 훈련 데이터 파일 입력
for row in rows:
    # 파일명 파싱
    row = row.split(",")
    (filename, startX, startY, endX, endY) = row

    # opencv로 파일 로딩
    imagePath = os.path.sep.join([config.IMAGES_PATH, filename])
    image = cv2.imread(imagePath)
    (h, w) = image.shape[:2]        # 이미지 높이 폭 획득

    # 경계 박스 정규화
    startX = float(startX) / w
    startY = float(startY) / h
    endX = float(endX) / w
    endY = float(endY) / h

    # 파일 로딩. 타겟 크기는 224, 224
    image = load_img(imagePath, target_size=(224, 224))
    image = img_to_array(image)  # 이미지를 배열로 변환

    # 이미지를 데이터배열에 추가. targets에 bbox 추가. 파일명 리스트 추가
    data.append(image)
    targets.append((startX, startY, endX, endY))
    filenames.append(filename)

# 데이터를 numpy 형식으로 변환. 255로 나누어 0 - 1 사이값으로 정규화
data = np.array(data, dtype="float32") / 255.0
targets = np.array(targets, dtype="float32")

# 90% 훈련용 데이터 분할. 10%는 테스트용 분할
split = train_test_split(data, targets, filenames, test_size=0.10,
    random_state=42)    # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# 데이터셋 train, test 의 이미지, target label, fname 획득
(trainImages, testImages) = split[:2]           # 224x224 이미지. 720개. 80개
(trainTargets, testTargets) = split[2:4]        # bbox 데이터    
(trainFilenames, testFilenames) = split[4:]     # 파일명

# 저장될 훈련 모델 파일명
print("[INFO] saving testing filenames...")
f = open(config.TEST_FILENAMES, "w")
f.write("\n".join(testFilenames))
f.close()

# 사전 학습된 VGG16 네트워크 로딩. 전이학습. 
# FC 층만 제외하고 전체 레이어 모델 로딩.
vgg = VGG16(weights="imagenet", include_top=False,
    input_tensor=Input(shape=(224, 224, 3)))

# 학습 데이터가 사전학습 데이터와 유사하므로, VGG 모든 층 가중치 조정안되도록 설정
vgg.trainable = False

# VGG의 출력층을 완전연결(FC) 평활화 레이어와 연결.
flatten = vgg.output
flatten = Flatten()(flatten)    # https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten

# FC층을 밀집층(128)-(64)-(32)-(4)로 연결
# 결론적으로 밀집층(4)가 각 bbox 좌표의 예측값이 되도록, 모델의 출력을 만듬. 
# 마지막층은 sigmoid로 활성화시킴.
bboxHead = Dense(128, activation="relu")(flatten)
bboxHead = Dense(64, activation="relu")(bboxHead)
bboxHead = Dense(32, activation="relu")(bboxHead)
bboxHead = Dense(4, activation="sigmoid")(bboxHead)

# 모델 입력은 vgg.input 층 사용. 
# bbox 회귀식 계산을 위해, 모델은 미세 조정 될 것임. 
# vgg.input.shape = (None, 224, 224, 3)
# output=bboxhead.shape = (None, 4)
model = Model(inputs=vgg.input, outputs=bboxHead)    # https://www.tensorflow.org/api_docs/python/tf/keras/Model

# ADAM으로 loss 경계하강, 최적화. 
# loss 함수는 Mean Square Error
opt = Adam(lr=config.INIT_LR)
model.compile(loss="mse", optimizer=opt)
print(model.summary())

# bbox 회귀모델 fitting을 위한 네트워크 훈련
print("[INFO] training bounding box regressor...")
H = model.fit(
    trainImages, trainTargets,
    validation_data=(testImages, testTargets),
    batch_size=config.BATCH_SIZE,
    epochs=config.NUM_EPOCHS,
    verbose=1)  # https://keras.io/api/models/model_training_apis/

# 학습 종료 후 훈련 모델 저장
print("[INFO] saving object detector model...")
model.save(config.MODEL_PATH, save_format="h5")  # https://www.tensorflow.org/guide/keras/save_and_serialize
# https://portal.hdfgroup.org/display/support/Download+HDFView

# 훈련 이력 저장. epoch 별로 H 배열에 저장된 loss, val_loss를 plot. 
N = config.NUM_EPOCHS
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.title("Bounding Box Regression Loss on Training Set")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend(loc="lower left")
plt.savefig(config.PLOT_PATH)

```

### <predict.py>
경로: /notebook-001/4_object_detection/3_bounding-box-regression/predict.py
```python
# USAGE
# python predict.py --input output/test_images.txt

import config
import keras
from tensorflow.keras.preprocessing.image import img_to_array
from keras.utils import load_img
from tensorflow.keras.models import load_model
import numpy as np
import mimetypes
import argparse
import imutils
import cv2
import os

curd = os.path.dirname(os.path.abspath(__file__)) + '\\'

# 파이썬 입력 인자 파싱
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", default=curd + 'dataset/images',
    help="path to input image/text file of image filenames")
args = vars(ap.parse_args())

# 입력 폴더에서 파일명 획득
input_path = args['input']
imagePaths = []
for path in os.listdir(input_path):
    if os.path.isfile(os.path.join(input_path, path)):
        imagePaths.append(input_path + '//' + path)

# 학습 모델 로딩
print("[INFO] loading object detector...")
model = load_model(config.MODEL_PATH)

# 이미지 파일을 로딩해 학습 모델에 입력. prediction 수행
for imagePath in imagePaths:
    # 이미지 로딩 후 정규화
    # 0축 차원 확장해, 학습 모델 입력 텐서 차원과 일치시킴
    image = keras.utils.load_img(imagePath, target_size=(224, 224))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)  # (1,224,224,3)

    # 예측 수행 후, 첫 번째 출력 bbox 값 획득
    preds = model.predict(image)[0]
    (startX, startY, endX, endY) = preds

    # 이미지 로딩 후 width 리사이즈, 이미지 폭과 높이 획득
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=600)
    (h, w) = image.shape[:2]

    # bbox는 0~1 사이값으로 정규화되어 있으므로 실제 크기로 스케일 변환
    startX = int(startX * w)
    startY = int(startY * h)
    endX = int(endX * w)
    endY = int(endY * h)

    # 예측된 bbox를 이미지 위에 표시
    cv2.rectangle(image, (startX, startY), (endX, endY),
        (0, 255, 0), 2)

    # 이미지 출력
    cv2.imshow("Output", image)
    cv2.waitKey(0)

```

# CH04-04. Practice_codereivew_YOLOv1(1)

### <train.py>
경로: /notebook-001/4_object_detection/appendix_4_YOLOv1/train.py
```python
"""
이 코드는 YOLOv1의 구조, 알고리즘을 잘 이해할 수 있도록, 논문을 바탕으로 개발된 PyTorch기반 오픈소스 코드임. 
Pascal VOC 데이터로 학습되며, 클래스는 20개, 격자는 7 * 7, 앵커박스는 2개임. Pascal VOC 데이터셋 사용.
참고 - Aladdin Persson, 2020, Machine Learning Collection, https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO
"""

import os
import torch
import torchvision.transforms as transforms
import torch.optim as optim
import torchvision.transforms.functional as FT
from tqdm import tqdm
from torch.utils.data import DataLoader
from model import Yolov1
from dataset import VOCDataset
from utils import (
    non_max_suppression,
    mean_average_precision,
    intersection_over_union,
    cellboxes_to_boxes,
    get_bboxes,
    plot_image,
    save_checkpoint,
    load_checkpoint,
)
from loss import YoloLoss
from torch.utils.tensorboard import SummaryWriter

cwd = os.getcwd()
curd = os.path.dirname(os.path.abspath(__file__)) + '\\'

# 텐서보드 저장 폴더 설정
writer = SummaryWriter(log_dir=curd + '/runs')  # 훈련 과정 모니터링은 tensorboard에서 확인 가능하도록 수정

seed = 123
torch.manual_seed(seed)

# 하이퍼파라미터 설정
LEARNING_RATE = 2e-5
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 16  # GPU VRAM이 크다면 배치크기를 높일 것. 논문은 64
WEIGHT_DECAY = 0
EPOCHS = 1000
NUM_WORKERS = 2
PIN_MEMORY = True
LOAD_MODEL = False
LOAD_MODEL_FILE = "overfit.pth.tar"
IMG_DIR = "data/images"  # 학습용 이미지, 라벨 폴더
LABEL_DIR = "data/labels"

# 이미지 데이터 변환 클래스 정의
class Compose(object):
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, img, bboxes):
        for t in self.transforms:
            img, bboxes = t(img), bboxes
        return img, bboxes

# 학습용 데이터 전처리 (이미지를 448x448로 리사이즈 후 텐서 변환)
transform = Compose([transforms.Resize((448, 448)), transforms.ToTensor(),])

# 학습 함수 정의
def train_fn(epoch, train_loader, model, optimizer, loss_fn):
    loop = tqdm(train_loader, leave=True)   # 훈련 과정 모니터링
    mean_loss = []

    # 배치 단위 학습
    for batch_idx, (x, y) in enumerate(loop):
        x, y = x.to(DEVICE), y.to(DEVICE)
        out = model(x)                      # Forward pass
        loss = loss_fn(out, y)              # 손실 계산
        mean_loss.append(loss.item())

        optimizer.zero_grad()               # 기존 gradient 초기화
        loss.backward()                     # 역전파 수행
        optimizer.step()                    # 가중치 업데이트

        # 20 epoch마다 모델 저장
        if epoch % 20 == 0 and batch_idx == len(loop) - 1:
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': loss
            }, curd + f'yolo_{epoch}.pth')

        loop.set_postfix(loss=loss.item())

    m_loss = sum(mean_loss) / len(mean_loss)
    print(f"Mean loss was {m_loss}")
    return m_loss

def main():
    # YOLOv1 모델 생성
    model = Yolov1(split_size=7, num_boxes=2, num_classes=20).to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=WEIGHT_DECAY)
    loss_fn = YoloLoss()

    if LOAD_MODEL:
        load_checkpoint(torch.load(LOAD_MODEL_FILE), model, optimizer)

    # 학습용 / 테스트용 데이터셋 정의
    train_dataset = VOCDataset(
        curd + "data/100examples.csv",
        transform=transform,
        img_dir=curd + IMG_DIR,
        label_dir=curd + LABEL_DIR,
    )

    test_dataset = VOCDataset(
        curd + "data/test.csv",
        transform=transform,
        img_dir=curd + IMG_DIR,
        label_dir=curd + LABEL_DIR,
    )

    # 데이터 로더 정의
    train_loader = DataLoader(
        dataset=train_dataset,
        batch_size=BATCH_SIZE,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        shuffle=True,
        drop_last=True,
    )

    test_loader = DataLoader(
        dataset=test_dataset,
        batch_size=BATCH_SIZE,
        num_workers=NUM_WORKERS,
        pin_memory=PIN_MEMORY,
        shuffle=True,
        drop_last=True,
    )

    # 학습 루프
    for epoch in range(EPOCHS):
        # 현재 모델의 예측 bbox와 정답 bbox 계산
        pred_boxes, target_boxes = get_bboxes(
            train_loader, model, iou_threshold=0.5, threshold=0.4
        )

        # mAP 계산
        mean_avg_prec = mean_average_precision(
            pred_boxes, target_boxes, iou_threshold=0.5, box_format="midpoint"
        )
        print(f"Train mAP: {mean_avg_prec}")

        # mAP가 0.99 이상이면 학습 종료
        if mean_avg_prec > 0.99:
            break

        # 한 epoch 학습
        m_loss = train_fn(epoch, train_loader, model, optimizer, loss_fn)

        # TensorBoard 로그 기록
        writer.add_scalar("mAP", mean_avg_prec, epoch)
        writer.add_scalar("Loss/train", m_loss, epoch)

    writer.close()

    # 최종 학습된 모델 저장
    torch.save(model.state_dict(), curd + 'yolo_last.pth')

if __name__ == "__main__":
    main()

```
### <model.py>
경로: /notebook-001/4_object_detection/appendix_4_YOLOv1/model.py
```python
"""
YOLOv1 모델은 이후 개발되는 YOLOv3, v5, x에 영향을 준 주요 개념을 포함하고 있음.
"""

import torch
import torch.nn as nn

""" 
YOLOv1 네트워크 구성을 유연하게 추가하도록, 그 구조를 배열과 튜플로 정의함.
튜플 구조는 (kernel_size, filters, stride, padding) 임.
"M" 문자열은 2x2 max pooling을 의미함.  
리스트 요소는 그 안에 정의된 튜플로 표현된 층의 반복 추가를 정의함.
"""

# YOLOv1 모델 구조를 배열, 튜플로 정의
architecture_config = [
    (7, 64, 2, 3),
    "M",
    (3, 192, 1, 1),
    "M",
    (1, 128, 1, 0),
    (3, 256, 1, 1),
    (1, 256, 1, 0),
    (3, 512, 1, 1),
    "M",
    [(1, 256, 1, 0), (3, 512, 1, 1), 4],
    (1, 512, 1, 0),
    (3, 1024, 1, 1),
    "M",
    [(1, 512, 1, 0), (3, 1024, 1, 1), 2],
    (3, 1024, 1, 1),
    (3, 1024, 2, 1),
    (3, 1024, 1, 1),
    (3, 1024, 1, 1),
]


# Convolution block 정의 (Conv2D + BatchNorm + LeakyReLU)
class CNNBlock(nn.Module):
    def __init__(self, in_channels, out_channels, **kwargs):
        super(CNNBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, bias=False, **kwargs)  # Conv layer
        self.batchnorm = nn.BatchNorm2d(out_channels)  # Batch normalization
        self.leakyrelu = nn.LeakyReLU(0.1)  # Leaky ReLU 활성화 함수

    def forward(self, x):
        return self.leakyrelu(self.batchnorm(self.conv(x)))


# YOLOv1 모델 클래스 정의
class Yolov1(nn.Module):
    def __init__(self, in_channels=3, **kwargs):
        super(Yolov1, self).__init__()
        self.architecture = architecture_config
        self.in_channels = in_channels
        self.darknet = self._create_conv_layers(self.architecture)  # Darknet backbone 생성
        self.fcs = self._create_fcs(**kwargs)  # Fully connected layer 생성

    def forward(self, x):
        x = self.darknet(x)  # Conv layers 통과 (Darknet feature extraction)
        return self.fcs(torch.flatten(x, start_dim=1))  # Flatten 후 FC 층 통과

    def _create_conv_layers(self, architecture):
        layers = []
        in_channels = self.in_channels

        for x in architecture:
            # Conv layer tuple
            if type(x) == tuple:
                layers += [
                    CNNBlock(
                        in_channels,
                        x[1],
                        kernel_size=x[0],
                        stride=x[2],
                        padding=x[3],
                    )
                ]
                in_channels = x[1]

            # MaxPooling layer
            elif type(x) == str:
                layers += [nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))]

            # 반복되는 Conv 블록
            elif type(x) == list:
                conv1 = x[0]
                conv2 = x[1]
                num_repeats = x[2]

                for _ in range(num_repeats):
                    layers += [
                        CNNBlock(
                            in_channels,
                            conv1[1],
                            kernel_size=conv1[0],
                            stride=conv1[2],
                            padding=conv1[3],
                        ),
                        CNNBlock(
                            conv1[1],
                            conv2[1],
                            kernel_size=conv2[0],
                            stride=conv2[2],
                            padding=conv2[3],
                        ),
                    ]
                    in_channels = conv2[1]

        return nn.Sequential(*layers)

    def _create_fcs(self, split_size, num_boxes, num_classes):
        S, B, C = split_size, num_boxes, num_classes

        # Fully Connected Layer 구성
        # 입력: 1024 * 7 * 7 = 50176
        # 출력: S * S * (C + B * 5)
        # 즉, 7x7x(20 + 2*5) = 1470
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(1024 * S * S, 496),  # 중간 FC층
            nn.LeakyReLU(0.1),
            nn.Linear(496, S * S * (C + B * 5)),  # 최종 출력층
            # output 텐서 구조를 똑같이 맞춰야됨
        )
```

### <loss.py>
경로: /notebook-001/4_object_detection/appendix_4_YOLOv1/loss.py
```python
"""
이 구현 소스는 YOLOv1의 논문을 바탕으로, Loss 함수를 정의한 레이어로, 
PyTorch nn.Module에서 파생받아 정의된 것임.
"""

import torch
import torch.nn as nn
from utils import intersection_over_union


class YoloLoss(nn.Module):
    """
    YOLOv1 모델의 손실함수를 정의
    """

    def __init__(self, S=7, B=2, C=20):
        super(YoloLoss, self).__init__()
        self.mse = nn.MSELoss(reduction="sum")

        """
        S: 격자 수 (7x7)
        B: 앵커 박스 개수 (2)
        C: 클래스 수 (VOC 데이터의 경우 20)
        """
        self.S = S
        self.B = B
        self.C = C

        # 논문에 명시된 loss 가중치 (λcoord=5, λnoobj=0.5)
        self.lambda_noobj = 0.5
        self.lambda_coord = 5

    def forward(self, predictions, target):
        """
        predictions: (BATCH_SIZE, S*S*(C + B*5))
        target: 동일한 형태의 라벨 데이터
        """
        predictions = predictions.reshape(-1, self.S, self.S, self.C + self.B * 5)

        # 두 bounding box 각각의 IoU 계산
        iou_b1 = intersection_over_union(predictions[..., 21:25], target[..., 21:25])
        iou_b2 = intersection_over_union(predictions[..., 26:30], target[..., 21:25])
        ious = torch.cat([iou_b1.unsqueeze(0), iou_b2.unsqueeze(0)], dim=0)

        # 두 박스 중 IoU가 더 큰 박스를 선택
        iou_maxes, bestbox = torch.max(ious, dim=0)
        exists_box = target[..., 20].unsqueeze(3)  # object 존재 여부

        # 선택된 박스의 좌표 예측값 계산
        box_predictions = exists_box * (
            bestbox * predictions[..., 26:30]
            + (1 - bestbox) * predictions[..., 21:25]
        )

        # 실제 라벨 데이터의 bbox
        box_targets = exists_box * target[..., 21:25]

        # √W, √H 계산 (논문 방식)
        box_predictions[..., 2:4] = torch.sign(box_predictions[..., 2:4]) * torch.sqrt(
            torch.abs(box_predictions[..., 2:4] + 1e-6)
        )
        box_targets[..., 2:4] = torch.sqrt(box_targets[..., 2:4])

        # 좌표 손실 (MSE)
        box_loss = self.mse(
            torch.flatten(box_predictions, end_dim=-2),
            torch.flatten(box_targets, end_dim=-2),
        )

        # Objectness 예측값 선택
        pred_box = (
            bestbox * predictions[..., 25:26] + (1 - bestbox) * predictions[..., 20:21]
        )

        # Objectness 손실
        object_loss = self.mse(
            torch.flatten(exists_box * pred_box),
            torch.flatten(exists_box * target[..., 20:21]),
        )

        # No Object 손실 (두 박스 모두에 대해)
        no_object_loss = self.mse(
            torch.flatten((1 - exists_box) * predictions[..., 20:21], start_dim=1),
            torch.flatten((1 - exists_box) * target[..., 20:21], start_dim=1),
        )

        no_object_loss += self.mse(
            torch.flatten((1 - exists_box) * predictions[..., 25:26], start_dim=1),
            torch.flatten((1 - exists_box) * target[..., 20:21], start_dim=1),
        )

        # 클래스 손실 (object가 존재하는 경우만 계산)
        class_loss = self.mse(
            torch.flatten(exists_box * predictions[..., :20], end_dim=-2),
            torch.flatten(exists_box * target[..., :20], end_dim=-2),
        )

        # 최종 손실 계산 (가중치 포함)
        loss = (
            self.lambda_coord * box_loss      # 좌표 손실
            + object_loss                     # 객체 존재 손실
            + self.lambda_noobj * no_object_loss  # 객체 없음 손실
            + class_loss                      # 클래스 손실
        )

        return loss  # 총 손실 반환

```

### <dataset.py>
경로: /notebook-001/4_object_detection/appendix_4_YOLOv1/dataset.py
```python
"""
Creates a PyTorch dataset to load the Pascal VOC dataset
"""

import torch
import os
import pandas as pd
from PIL import Image


class VOCDataset(torch.utils.data.Dataset):  # Dataset 파생 클래스 정의
    def __init__(
        self, csv_file, img_dir, label_dir, S=7, B=2, C=20, transform=None,
    ):
        """
        csv_file: 라벨링된 데이터 목록 (csv)
        img_dir: 이미지 데이터 폴더 경로
        label_dir: 라벨 파일 폴더 경로
        S: 격자 수 (7x7)
        B: 격자당 경계 상자 수 (2)
        C: 클래스 수 (20 for Pascal VOC)
        transform: 이미지 변환 함수 (Resize, ToTensor 등)
        """
        self.annotations = pd.read_csv(csv_file)
        self.img_dir = img_dir
        self.label_dir = label_dir
        self.transform = transform
        self.S = S
        self.B = B
        self.C = C

    def __len__(self):
        """전체 데이터 개수 반환"""
        return len(self.annotations)

    def __getitem__(self, index):
        """데이터 1개를 로딩하여 반환 (이미지, 라벨 매트릭스)"""
        # 라벨 파일 경로
        label_path = os.path.join(self.label_dir, self.annotations.iloc[index, 1])

        # 라벨 파일 파싱하여 bbox 리스트 생성
        boxes = []
        with open(label_path) as f:
            for label in f.readlines():
                # class, x, y, width, height 순서로 파싱
                class_label, x, y, width, height = [
                    float(x) if float(x) != int(float(x)) else int(x)
                    for x in label.replace("\n", "").split()
                ]
                boxes.append([class_label, x, y, width, height])

        # 이미지 경로
        img_path = os.path.join(self.img_dir, self.annotations.iloc[index, 0])
        image = Image.open(img_path)
        boxes = torch.tensor(boxes)  # bbox를 tensor로 변환

        # 이미지 및 bbox 변환 (448x448 Resize 및 ToTensor)
        if self.transform:
            image, boxes = self.transform(image, boxes)

        # 라벨 매트릭스 초기화 (SxSx(C + 5*B))
        label_matrix = torch.zeros((self.S, self.S, self.C + 5 * self.B))

        for box in boxes:
            class_label, x, y, width, height = box.tolist()
            class_label = int(class_label)

            # bbox 중심 좌표 (x,y)에 해당하는 격자 인덱스 계산
            i, j = int(self.S * y), int(self.S * x)

            # 격자 내 상대좌표 계산 (0~1)
            x_cell, y_cell = self.S * x - j, self.S * y - i

            # bbox의 폭, 높이를 격자 단위로 변환
            width_cell, height_cell = width * self.S, height * self.S

            # 해당 격자에 객체 정보가 없을 때만 할당
            if label_matrix[i, j, 20] == 0:
                label_matrix[i, j, 20] = 1  # Objectness = 1

                # bbox 좌표 (cx, cy, w, h)
                box_coordinates = torch.tensor([x_cell, y_cell, width_cell, height_cell])

                # bbox 정보 채우기 (21~25 인덱스)
                label_matrix[i, j, 21:25] = box_coordinates

                # 클래스 one-hot 인코딩
                label_matrix[i, j, class_label] = 1

        return image, label_matrix  # 이미지와 라벨 매트릭스 반환

```


# CH04-05. Practice_codereivew_YOLOv1(2)

![[스크린샷 2025-10-10 오전 1.47.56.png]]

```python
arch = [
	(7, 64, 2, 3), # (커널 사이즈, up 채널, swide, padding)
	"M",           # Maxpooling
	(3, 192, 1, 1),
	"M",
	(1, 128, 1, 0),
	(3, 256, 1, 1),
	(1, 256, 1, 0),
	(3, 512, 1, 1),
	"M",
	[(1, 256, 1, 0), (3, 512, 1, 1), 4],
	(1, 512, 1, 0),
	(3, 1024, 1, 1),
	"M",
	[(1, 512, 1, 0), (3, 1024, 1, 1), 2],
	(3, 1024, 1, 1),
	(3, 1024, 2, 1),
	(3, 1024, 1, 1),
	(3, 1024, 1, 1),
]
```

### <4_YOLOv1_model.ipynb>
경로: /notebook-001/4_object_detection/4_YOLOv1_model.ipynb
```python
"""
YOLOv1 모델은 이후 개발되는 YOLOv3, v5, x에 영향을 준 주요 개념을 포함하고 있음.
"""
import torch
import torch.nn as nn

""" 
YOLOv1 네트워크 구성을 유연하게 추가하도록, 그 구조를 배열과 튜플로 정의함.
튜플 구조는 (kernel_size, filters, stride, padding) 임
M 문자열은 2x2 max pooling을 의미함.  
리스트 요소는 그 안에 정의된 튜플로 표현된 층의 반복 추가를 정의함.
"""

# YOLOv1 모델 정보를 배열, 튜플 형식으로 정의함
arch = [
    (7, 64, 2, 3),
    "M",
    (3, 192, 1, 1),
    "M",
    (1, 128, 1, 0),
    (3, 256, 1, 1),
    (1, 256, 1, 0),
    (3, 512, 1, 1),
    "M",
    [(1, 256, 1, 0), (3, 512, 1, 1), 4],
    (1, 512, 1, 0),
    (3, 1024, 1, 1),
    "M",
    [(1, 512, 1, 0), (3, 1024, 1, 1), 2],
    (3, 1024, 1, 1),
    (3, 1024, 2, 1),
    (3, 1024, 1, 1),
    (3, 1024, 1, 1),
]

# conv net block을 정의함. 
class CNNBlock(nn.Module):
    def __init__(self, in_channels, out_channels, **kwargs):
        # YOLO의 conv net 구조는 conv2d, batch normal, leaky relu로 구성됨.
        super(CNNBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, bias=False, **kwargs)
        self.batchnorm = nn.BatchNorm2d(out_channels)
        self.leakyrelu = nn.LeakyReLU(0.1)

    def forward(self, x):
        # 모델 학습시 아래와 같은 구조로 입력 데이터 계산
        return self.leakyrelu(self.batchnorm(self.conv(x)))


# 앞서 정의된 YOLO 구조 리스트 튜플 해석해 모델 레이어 층 생성
class Yolov1(nn.Module):
    def __init__(self, in_channels=3, **kwargs):
        super(Yolov1, self).__init__()
        self.architecture = arch
        self.in_channels = in_channels  # 입력 채널. 디폴트값 3.
        self.darknet = self.darknet_conv_net(self.architecture)  # YOLO 구조 해석해 다크넷 모델 레이어 생성 추가.
        self.fcs = self.create_FC(**kwargs)  # 마지막 FC 연결층 생성

    def forward(self, x):
        x = self.darknet(x)  # 생성된 다크넷 모델에 데이터 입력 및 계산. x 최종 출력층 shape은 입력 (16, 3, 448, 448)에서 (16, 1024, 7, 7)이 되도록 전체 다크넷의 conv 층 파라메터가 구성되어 있음. 
        return self.fcs(torch.flatten(x, start_dim=1))  # 리턴받은 x를 입력받아, 1차원 이후로(0차원은 배치크기임) 평활화(flatten)처리 후, FC 연결층 실행. shape는 (16, 50176)임. 50176=1024*7*7

    def darknet_conv_net(self, architecture):
        # 다크넷 모델 레이어 배열 정의
        layers = []
        in_channels = self.in_channels

        # YOLO 구조 각 튜플, 리스트 열거하며 처리.
        for x in architecture:
            if type(x) == tuple:  # 튜플일 경우, CNNBLOCK 생성
                layers += [
                    CNNBlock(
                        in_channels, x[1], kernel_size=x[0], stride=x[2], padding=x[3],
                    )
                ]
                in_channels = x[1]  # 다음 추가할 레이어를 위해 입력 채널은 최종 채널로 설정. Conv2d()로 생성된 레이어의 이전 채널과 다음 채널수를 서로 일치하도록 함.

            elif type(x) == str:    
                layers += [nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))]  # 2x2 max pooling. https://pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html

            elif type(x) == list:  # 리스트 형식이면. 두개 튜플 입력과 추가 반복횟수 처리함
                conv1 = x[0]
                conv2 = x[1]
                num_repeats = x[2]

                for _ in range(num_repeats):
                    layers += [
                        CNNBlock(
                            in_channels,
                            conv1[1],
                            kernel_size=conv1[0],
                            stride=conv1[2],
                            padding=conv1[3],
                        )  # 각 튜플의 conv 파라메터 입력해, 레이어 생성.
                    ]
                    layers += [
                        CNNBlock(
                            conv1[1],
                            conv2[1],
                            kernel_size=conv2[0],
                            stride=conv2[2],
                            padding=conv2[3],
                        )  # 이전 채널수는 conv1[1]에서 입력받음. 나머지는 동일하게 처리.
                    ]
                    in_channels = conv2[1]

        return nn.Sequential(*layers)  # 시퀀스 모델에 생성된 레이어들 추가.

    def create_FC(self, split_size, num_boxes, num_classes):
        S, B, C = split_size, num_boxes, num_classes

        # 마지막 FC 레이어 생성. 
        # 우선, 바로 이전 출력을 FC처리를 위해 평활화(Flatten)함.
        # 이와 가중치 행렬이 다음층과 밀집 연결되도록 함(Linear 입력=1024 x 7 x 7, 출력=496)
        # LeakyReLu(0.1) 사용.
        # 최종 출력은 7 x 7 x (20 + 2 * 5) 형식임. 
        # Dataset loader에서 생성된 라벨데이터와 다중손실함수로 손실값 계산되어야 하므로, 같은 텐서 차원이 되도록 하여야 함. 
        # 결론적으로, 학습되며 생성되는 특징들이 그리드로 맵핑되어 Loss 함수를 통해, prediction 값과 손실을 줄이도록, 가중치를 업데이트하는 문제로 구현된 것임.
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(1024 * S * S, 4096),
            nn.Dropout(0.0),
            nn.LeakyReLU(0.1),
            nn.Linear(4096, S * S * (C + B * 5)),
        )


# 모델 생성
DEVICE = "cuda" if torch.cuda.is_available else "cpu"
model = Yolov1(split_size=7, num_boxes=2, num_classes=20).to(DEVICE)
print(model)

```
