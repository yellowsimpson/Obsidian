
# Chapter 1. ROS2 개요

## 1. ROS2개요
- *AGV(바퀴 4개 달린 자동차)*
1. Task Description
	- 네비게이션
2. Perception
	- 카메라, 라이다
	- Encoder
	- IMU
3. Planning
	- 경로 계획
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용

- *다리 4개 달린 강아지 로봇*
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
2. Perception
	- 카메라, 라이다
	- Encoder
	- IMU
3. Planning
	- 경로 계획(dynamics & kinematics)
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용

- *3축 로봇암*
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
	- 물체를 집어 올리기
2. Perception
	- 카메라 -> 외부 카메라를 통해 상황 파악하는 경우가 많음
	- Encoder
3. Planning
	- 경로 계획(dynamics & kinematics)
	- 모션 플래닝
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용

- *휴머노이드 로봇*
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
	- 물체를 집어 올리기
2. Perception
	- 카메라, 라이다
	- Encoder
	- 촉각 센서
	- IMU
3. Planning
	- 경로 계획(dynamics & kinematics)
	- 모션 플래닝
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용
	- 사람과의 상호작용

## 2. ROS2의 필요성
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
	- 물체를 집어 올리기
__-> 외부에서 주어짐__

2. Perception
	- 카메라, 라이다
	- Encoder
	- 촉각 센서
	- IMU
3. Planning
	- 경로 계획(dynamics & kinematics)
	- 모션 플래닝
4. Control -> PID 제어를 많이 사용
	- 로봇 구동
	- 외란(미끄럼)의 작용
	- 사람과의 상호작용
__-> 상황에 맞게 변형
- 센서의 종류, 알고리즘의 종류, 컨트롤러의 종류
- 고려할 사항이 매우 많고 구현이 어려움



## 3. ROS2의 필요성2
1. 센서
	- 카메라 패키지
	- 라이다 패키지
	- IMU 패키지
2. 플래닝 알고리즘
	- 서치 알고리즘
	- 모션 프래닝 알고리즘
	- 경로 계획 알고리즘
	- 네비게이션 알고리즘
3. 필터링 알고리즘
	- 몬테 카를로
	- 칼만 필터

__-> ROS가 여러 패키지를 한번에 모아서 사용할 수 있게 해준다.__


- 하드웨어와 소프트웨어를 모듈화하고 연결하는 미들웨어
- 복잡한 로봇 제어 시스템을 구성 가능하게 해주는 프레임워크
- 기업(개인)과의 협업
- 패키지 확장성

1. 제조사 제공 드라이버
	- 복잡한 low-level 소프트웨어
2. ROS 플랫 폼
	- movite2, nav2, driver
3. 사용이 편리한 high-level 소프트웨어
4. Head

## 4. ROS2 특징

### ROS1 ROS2 차이점
- ROS1
	-  중앙 집중형: 병령 처리의 한계 존재
	- 신시간성 부족: 제어 주기를 맞추기 어려움(TCPROS)
	- 다양한 로봇을 위한 환경 구성의 어려움: IP 설정, 로봇 ID 수작업 등
	- XML 기반 실행

- ROS2
	-  중앙 집중형: 병령 처리의 한계 존재 -> __병렬 구조__
	- 신시간성 부족: 제어 주기를 맞추기 어려움(TCPROS)->  __우선순위 기반, 시간 제약 고려한 통신(RTOS)
	- 다양한 로봇을 위한 환경 구성의 어려움: IP 설정, 로봇 ID 수작업 등 -> __로봇 ID 작업 자동화__
	- XML 기반 실행 -> __Python 기반 실행__

## 5. 마무리
1. ROS의 특징 및 필요성
	- 하드웨어와 소프트웨어 모듈화 및 연결
	- 기업과의 협업
2. ROS1 vs ROS2
	- 구조
	- 실시간성
	- 로봇 ID
	- PYTHON 기반

# Chapter 2. ROS2 기본 개념
## 1, 2, 3. ROS2 개념
![](https://miro.medium.com/v2/resize:fit:1400/0*aNw-2q1Azw5QpAuN.gif)

- 노드 (Node)
    - ROS2에서 실행되는 프로그램의 최소 단위
    - 노드끼리는 서로 통신하면서 협업
    - 메시지를 주고 받으면서 상호작용을 함
        
- 토픽 (Topic)
    - 노드끼리 데이터를 주고받는 __채널__ 같은 것
    - __서비스와 다르게 계속해서 신호를 보냄__
        
- 메시지 (Message)
    - 통신의 기본 단위
    - 토픽에 실려 나르는 데이터의 형식 -> Structure 정의
    - Publish–Subscribe 방식
        - 퍼블리셔 노드(Publisher node) : 데이터를 보냄.
			->방송국에 정보를 보냄!
        - 서브스크라이버 노드(Subscriber node) : 데이터를 받음.
			->방송국에서 정보를 받고 있음!
        
- 서비스 (Service)
    - 정보 요청(Request) - 응답 구조(Response)
    - Server와  Client가 있음
    - __필요할 때만 보내는 단발성 통신__ , 짧고 즉각적인 통신에 적합
    - 진행상황을 알 수 없고 취소 불가능

- 파라미터(Parameter)
    - ROS2 노드 내부에서 사용하는 전역적인 설정 값
    - 토픽 메시지처럼 계속 주고받는 데이터가 아니라 한 번 설정해두고 노드 실행 중에 참조
    - 각 노드들에 필요한 중요 정보
        
- 액션(Action)
    - 서비스와 비슷하지만 시간이 오래 걸리는 작업에 특화
    - Server와 Client가 있음
    - __진행상황을 알 수 있고 취소 가능__
    - 흐름 : Goal -> Feedback -> Result

![](https://docs.ros.org/en/rolling/_images/Action-SingleActionClient.gif)


## 4. ROS2 패키지 및 워크스페이스
- 패키지(Package)
    - 기능별 프로젝트를 관리하는 폴더
    - 기능 통합, 분리 등 단위에 제약이 없음
        
	- Package (Python)
		![[스크린샷 2025-10-04 오후 9.17.18.png]]
	        - package.xml : 패키지 정보
	        - setup.py : Python 모듈로 설정하기 위한 스크립트
	        - setup.cfg : setup.py 보조파일
	        - resource/my_robot_pkg : 패키지 리소스 관리
	        - my_robot_pkg/_init_.py : Python 패키지로 인식하기 위한 설정 파일
	        - launch : 패키지 실행 파일
	            
	- Package (C++)
		![[스크린샷 2025-10-04 오후 9.17.26.png]]
	        - CMakeLists.txt : C++ 핵심 빌드 설정 파일
	        - package.xml : 패키지 정보
	        - include : C++ 헤더파일
	        - src : 사용자가 작성한 실행코드
	        - launch : 패키지 실행 파일

		- 워크 스페이스 (Workspace)
		![[스크린샷 2025-10-04 오후 9.17.37.png]]
		    - ROS2 전체 프로젝트 구조
		        - ros2_ws : 워크스페이스 최상단
		        - src : 패키지를 포함하는 폴더
		        - 패키지
		        - install : 빌드된 실행 파일(빌드 결과물)
		        - build : 중간 빌드 결과물


[[ROS 명령어]]


# Chapter 3. ROS2 기본 개념 학습

## 1. 강의 개요

## 2. ROS2 설치

## 3. turtlesim 설치

## 4. node

## 5. rqt

## 6. topic

## 7. publish

## 8. 중간점검

## 9. service

## 10. parameter 도입부

## 11. parameter

## 12. action

## 13. 중간점검2

##  14. 마무리


# Chapter 4. ROS2 패키지 분석2

## 1. 패키지 개요

## 2. Robot Description
#### **my_robot_description**

로봇의 외형과 구조를 정의하는 패키지. 

**URDF** - 로봇의 기구학적 구조를 정의하는 파일

**Mesh** - 로봇의 3D 모델링 파일

**Launch** - URDF를 ROS2 시스템에 로드하는 **robot_state_publisher** 노드를 실행함


## 3. driver
#### **my_robot_driver**

ROS2 시스템과 실제 로봇 하드웨어를 연결하는 역할. 

**ROS2 명령어 -> 하드웨어 제어** - 표준 명령어를 받아서 모터 제어기가 알아들을 수 있는 저수준 신호로 변환

**하드웨어 센서값 -> ROS2 메시지** - 바퀴 엔코더 값이나 IMU 센서 데이터를 읽어서 표준 메시지로 변환하고 발행

#### **my_robot_bringup**

로봇을 구동하는 데 필요한 모든 노드를 한 번에 실행하는 역할. 대부분 launch 파일로만 이루어져 있음.

## 4. driver Repository

## 5. 추가 패키지
## **확장 패키지**

**gazebo_ros** - 시뮬레이션

**moveit2** - 모션 플래닝 / 로봇팔의 경로를 계획하고 충돌을 회피하는 기능을 제공함

**nav2** - 자율주행 / SLAM으로 지도를 만들고, 목적지까지 스스로 경로를 탐색하여 이동하는 기능을 제공함

**rviz2** - 3D 시각화 / 현재 상태, 센서 데이터, 경로 계획 등을 3D 환경에서 직관적으로 보여줌


## 6. Gitub Respository

## 7. Gitub Respository2

## 8. Build 예시

## 9. Build 예시2

## 10. 마무리





