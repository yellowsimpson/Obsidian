# Chapter 1. 로보틱스 활용 사례
## 1. 로보틱스 활용 사례
1. Figure AI
2. Roomba
3. Bostom Dynamics Spot
4. ABB Robotics
-> 휴머노이드 또는 로봇 청소기 같은 곳에 로보틱스가 사용 될 수 있다.
-> 일상 생활과 산업 현장에서 사용되는 로보틱스 모양은 다를 수 있다.
## 2. 로보틱스 구조
로봇 역할 수행 과정
1. Task Description
	- 물체를 옮기기
	- 물체를 잡기
	- 걷기
	- 달리기
2. Perception
	- 눈 - 카메라
	- 귀 - 가속도계
	- 촉각 - 촉각센서
3. Planning
	- 어떤 각도로 움직일까?
	- 어떤 속도로 움직일까?
	 3_1. Task Planning 
	 - 어떤 일을 먼저 할 것인지?
	 3_2. Motion Planning
	 - 관절을 얼마나 움직일 것인지?
4. Control
	- 근육 - 모터
-> Task는 꼭 순서를 따를 필요는 없음!


## 3. 플래닝 추가 설명
Planning(플래닝)
- __테스크 플래닝(Task Planning)__
	-> 어떤 순서로 일을 수행할 것이닞?
- __모션 플래닝(Motion Planning)__
	-> 어떻게 관절을 움직일 것인지?

모션 플래닝의 사용 사례
	->"로봇"으로 "환경"에서 "작업"을 수행
- 작업
	-> Pick & Place
	-> Driving
	-> Walk
- 로봇
	-> Mainpulator
	-> 자동차
	-> 휴머노이드
- 환경
	-> Workspace
	-> Obstacle
	-> Static vs. Dynamic

## 4. 로보틱스 구조 예시
### 로봇 청소기
1. Task Description
	- 청소
2. Perception
	- 눈 - 카메라, 라이다
	- 귀 - 가속도계
	- 촉각 - 촉각센서
3. Planning
	- 어떤 속도로 움직일까?
4. Control
	- 바퀴를 몇바퀴 돌리까?

### 산업현장에서 사용되는 로봇팔
1. Task Description
	- 용접
2. ~~Perception~~
3. Planning
	- 각 관절을 몇도로 움직일까?
4. Control
	- 각 관절의 모터를 몇바퀴 돌리까?

### 물건을 잡아올리는 로봇암
1. Task Description
	- 물체를 집어 올리기
2. Perception
	- 눈 - 카메라
3. Planning
	- 각 관절을 몇도로 움직일까?
4. Control
	- 각 관절의 모터를 몇바퀴 돌리까?

## 5. 모션 플래닝 소개
__모션 플래닝이 중요한 이유?__
1. 현장에서 실제로 로봇이 움직이도록 만드는 중요한 요소
2. 로봇(그리고 사람)의 안전한 움직임 확보

모션 플래닝이 어려운 이유?
1. 로봇의 움직임을 직관적으로 이해하기 어려움
2. 다양한 조합의 움직임이 가능함
3. 주변의 환경 정보를 종합해야 하는 점

# Chapter 2. 모션플래닝 개요
## 1. 강의 요약

1. Task Description
	- 물체를 옮기기
	- 물체를 잡기
	- 걷기
	- 달리기
2. Perception
	- 눈 - 카메라
	- 귀 - 가속도계
	- 촉각 - 촉각센서
3. Planning
	- 3_1. Task Planning 
	- 3_2. Motion Planning
4. Control
	- 근육 - 모터
## 2. 모션플래닝 개요
*문제1.* 모션 플래닝에서 유명한 문제: __Piano Movers Problem__
->가구와 장애물을 피해 어떻게 피아노를 안전하게 움직일 수 있는가?

1. Task Description
	- 피아노 옮기기
2. Perception
	- 방의 구조
	- 다른 가구들의 배치 등
3. __Planning__
	- 피아노를 돌리고 밀고,,,
4. Control
	- 옮기는 사람의 근육
	- 옮기는 로봇의 모터 구동

모션 플래닝 정의

|          시작점 / 끝점          |            Task             |
| :------------------------: | :-------------------------: |
|          피아노의 모양           |            Robot            |
|           주변 환경            |         Environment         |
|             ⬇️             |             ⬇️              |
| 주변 가구와 부딪히지 않는 <br>피아노의 경로 | 로봇의 경로,<br>로봇의 모션(위치, 방향 등) |


*문제2.* 우주정거장에서 로봇이 움직일 때
->우주정거장 안에서 휴머노이드 로봇이 장애물을 피해 어떻게 목표지점까지 갈 수 있을까?

모션 플래닝 정의

|    walk    |    Task     |
| :---------: | :---------: |
|  Humanoid   |    Robot    |
| Hallway(현관) | Environment |

*문제3.* 로봇암이 물건을 집을 때
->로봇암이 어떻게 장애물을 피해 물건을 집어서 들어 올릴까?

모션 플래닝 정의

|        Pick & Place        |    Task     |
| :-------------------------: | :---------: |
| Robot - 6 Joint Manipulator |    Robot    |
|             Box             | Environment |

## 3. 모션플래닝 구조

1. Task
	- Pick & Place -> 로봇팔의 시작 상태 / 최종 상태
	- Driving -> 자동차의 시작 상태 / 최종 상태
	- Walk -> 휴머노이드의 시작 상태 / 최종 상태
	- ? ->  로봇의 시작 상태 / 최종 상태
2. Robot
	- Manipulator(로봇팔) -> 6개의 모터로 구동, 각 부품들의 길이는...
	- 자동차 -> 4개의 모터로 구동, 바튀 간 거리는
	- 휴머노이드 -> 3개의 모터로 팔을 구성, 4개의 모터로 다리 수어, 팔과 다리의 길이는
	- 로봇 -> N개의 모터로 구동, 각 관절은 x도까지 움직임이 가능, 물체의 길이는...
3. Environment(환경)
	- Workspace(작업 공간) -> 로봇이 움직일 수 있는 공간
	- Obstacles(장애물) -> 상자, 책상, 등 모든 물체 혹은 작업공간 자체
	- Static Environment(정적) -> 환경의 성질이 변하지 않음, 장애물들이 움직이지 않음
	- Dynamic Environment(동적) -> 환경의 성질이 변함. 장애물들이 움직임



