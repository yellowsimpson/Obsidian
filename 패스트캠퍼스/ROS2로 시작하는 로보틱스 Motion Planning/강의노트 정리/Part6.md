
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



## 2. ROS2의 필요성2
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

![[스크린샷 2025-10-04 오후 7.55.01.png]]


