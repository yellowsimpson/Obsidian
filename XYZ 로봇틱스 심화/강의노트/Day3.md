2025.10.01(수)

[[ㅗ을 가지고 협동-1_1차시_자료.pdf]]
협동 로봇은 위험 저감 조치로 활용할 수 있는 다양한 안전기능과 안전기기 연결 인터페이스를 제공합니다.

설치 프로그램:
https://robotlab.doosanrobotics.com/ko/Index 

1번 DART- PLatfrom

.drl : 두산에서 사용하는 언어 

주요 구성품
1.티치펜던트
2.컨트롤러
3.매니플레이터


[[ROS2_기초강의_250930_FINAL.pdf]]
- ros1은 tcp/ip 프로토콜을 사용한다
- ros2는 udp 프로토콜을 사용한다

![[스크린샷 2025-10-01 오후 2.18.21.png]]

pg4.
ZeroMQ(Message Que)
:처음에 온놈이 처음에 나간다

websockets에 대해서는 한번 알아볼 필요가 있다.

강사님 조언
-> 기술은 모두 연계가 되 있다.
->기술은 다 연결 연결 되어 있다는걸 알아야됨!!
-> 내가 배워야하는걸에 대한 리스트를 적어 놓고 하나씩 지워가며 공부할것!!
-> thread를 알아야함
-> 공부 할때 작은 거라도 놓치지 말고 공부할것!! 특히 소프트웨어 세계에서는!!
민감할줄 알아야됨!!

pg5.
python에서는 API라는 용어 보다 modul이라는 말이 더 적합함
API(Applicationi Program Interface)

프로그램을 
sink
asink

MQTT는 tcp, ip 방식으로 작동 되는 방식

ros 버전으로 clcon build  가 안 될때 해결책
1. 똑같은 이름으로 humble colcon build해
2. 기존에 있는 소스코드를 humble 에 가져다 놓고 다시 colon build 하면 됨 (진짜??)
3. 


오늘 수업 하면서 계속 해볼것 
어제 배웠던 ros 명령어 하나하나 쳐가면서 익숙하게 만들고 모두 외워

tutulsim  가지고 놀아








[[패스트캠 - 프로젝트 교안(RVIZ2)_김루진_1001.pdf]]

rqt_
두산 로보틱스에서 사용하는 확장자 .drl
우리가 하는일 두산 로보틱스 로봇을 제어하기 위한 파이썬 코드를 짜는 것

우리는 일단 잘 만들어진 걸 잘 가져와야한다.

pg 8
std_msgs/msg/

이거는 ros에서 제공하는 거임 굳이 건드리지 말고 그냥 쓰면 되


topic으로 카메라 데이터가 오면 다른 곳에서 subscribe 해서 데이터 출력하면 됨

TF(Transfrom Frames): 각 좌표계의 변환을 자동으로 변환해줘 publish 해줌
지속적으로 로봇의 변환 상태를 알려주는 것이다.

로봇이 어디에 있는지 아는것이 로봇의 상태를 아는 것!!

point cloud2: 
ex) 사과를 집을 때 
1. 사과의 위치를 확인
2. 사과에서 인식된 point cloud의 데이터를 받아옴
3. depth 카메라에서는 rgb, depth 2개의 데이터를 얻을 수 있음

pg 23
방향을 오일러 각도로 변환

인간이  이해 할때 알아볼때: 오일러
프로그램 상에서 계산하거 보여줄 때: 쿼터니엄



pg 43

대부분 조인트는 revolute로 되어 있음

prismatic : 직선 운동


SDF


urdf 파일 해석할 줄 알아야되

urdf 코드 예시
```xml
<?xml version="1.0"?>
<robot name="simple_robot">

  <!-- 첫 번째 링크 (base) -->
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.5 0.5 0.1"/>
      </geometry>
      <material name="gray">
        <color rgba="0.7 0.7 0.7 1.0"/>
      </material>
    </visual>
  </link>

  <!-- 두 번째 링크 (arm) -->
  <link name="arm_link">
    <visual>
      <geometry>
        <cylinder radius="0.05" length="1.0"/>
      </geometry>
      <origin xyz="0 0 0.5" rpy="0 0 0"/>
      <material name="blue">
        <color rgba="0.0 0.0 1.0 1.0"/>
      </material>
    </visual>
  </link>

  <!-- 조인트 (base_link ↔ arm_link) -->
  <joint name="base_to_arm" type="revolute">
    <parent link="base_link"/>
    <child link="arm_link"/>
    <origin xyz="0 0 0.05" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
    <limit lower="-1.57" upper="1.57" effort="10" velocity="1"/>
  </joint>

</robot>
```


이번 프로젝트에서는 moveit2를 사용하지 않을 수 있음
	-> 두산 로보틱스에서 제공하는 api가 있음

moveit2 특징
- c++로 만 제공
- mauel planing을 해주는것

forward 키네메틱스
-> 로봇을 설계된 내용을 가지고 
transfor matrix  가각의 관절읠 각도를 설정하는거에 따라서 

invers 키네메틱스
-> 역을 로봇암을 움직일지 
내가 원하는데로 가! 라고 해도 답이 안나올 수 도 있어
     =>	답이 여러개 일 수 도 있다.
		-> 사과를 집을 때 어떻게 집는게 가장 효율적일까?
해답을 찾아는걸 solbur(쏠버)라고 한다.
쏠버 중에서 가장 적절한 거를 선택해 주는 건 우리의 선택


end effector 설정

urdf와  srdf 파일의 차이점

## 🔹 URDF (Unified Robot Description Format)

- 로봇의 **기구학적/물리적 구조**를 기술하는 파일
    
- XML 기반
    
- 주로 ROS에서 RViz, Gazebo 시뮬레이션, 로봇 모델 정의에 사용됨
    

📌 URDF 안에 들어가는 것들

- **링크(link)**: 로봇의 각 부품 (몸통, 팔, 바퀴 등)
    
- **조인트(joint)**: 링크들을 연결하는 관절 (회전, 슬라이드 등)
    
- **기하학(geometry)**: 모양(박스, 원통, 메쉬)
    
- **관성/질량**: 물리 시뮬레이션용
    
- **시각적 요소(visual), 충돌 요소(collision)**
    

👉 쉽게 말하면: **"로봇이 어떻게 생겼고, 어떻게 움직이는가?"** 를 정의

---

## 🔹 SRDF (Semantic Robot Description Format)

- 로봇의 **추가 의미적 정보(semantics)** 를 정의하는 파일
    
- 보통 MoveIt! (로봇 경로 계획, IK, 제어 등)에서 사용
    
- URDF를 기반으로 **고급 기능을 정의**할 때 필요
    

📌 SRDF 안에 들어가는 것들

- **로봇 그룹(group)**: 여러 관절/링크를 묶어서 "팔", "다리" 같은 의미 단위로 정의
    
- **엔드이펙터(End-effector)**: 손이나 그리퍼 같은 부분 지정
    
- **가상 조인트(Virtual joint)**: 로봇 전체를 외부 세계(World)에 고정하는 정보
    
- **자유도 제한(disabled collision pairs)**: 충돌 체크에서 무시해도 되는 링크 쌍 정의
    
- **IK Solver 설정**: 역기구학 풀 때 어떤 그룹을 쓸지 정의
    

👉 쉽게 말하면: **"로봇을 어떻게 사용할 것인가?"** 를 정의
![[스크린샷 2025-10-01 오후 4.26.24.png]]



__moveit 설치 명령어__
$sudo apt update
$sudo apt install ros-humble-moveit

__실행__
$ros2 launch moveit setup assistant setup_assistant.launch.py


moveit2 실습해 볼 수 있는 깃허브 링크
https://github.com/ros-industrial/universal_robot

[[1장 인공지능 이해.pdf]]
인공지능에서 97%정도 맞으면 맞았다고함
-> 완벽한 답은 못찾지만 유사한 값은 찾을 수 있음


두 종류의 활성화 영역



[[2장 개발환경 구축.pdf]]

