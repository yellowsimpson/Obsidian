2025.10.02(목)
강의 자료
- [[프로젝트 교안(GAZEBO)_1010.pdf]]
사이트 링크
- 로보틱스 링크: https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup 
- yolo 블로그 링크: https://blog.naver.com/jangh13/223409424452 
- roboflow 사이트 링크: https://app.roboflow.com/test-pxiuh
- 강화학습 개념 링크:  https://atmokpo.com/w/40462/
과제
1. roboflow에서 모델을 학습 시켜 object detecting 된 결과 사진 찍어서 올리기
2. gazebo에 urdf 파일을 로드 시켜 모델 출력
3. 과제: 5X5격자에 3개연달아 있는 2개의 벽이 있습니다. 그리고 시작은 (0,0) 이고 골은 (5,5) 있습니다. 이것을 상하좌우로 움직이는 에이전트가 있습니다. 100번의 에피소드를 수행하는 학습 코드를 파이썬 및 gem 페키지를 이용해서 개발하세요. 


![[로봇모델.png]]

![[스크린샷 2025-10-02 오전 9.17.08.png]]

-> 그리퍼가 두산 로보틱스에서 사용하는 그리퍼임

- 카토그래퍼

bashrc.
```
$ source /opt/ros/humble/setup.bash
$ mkdir -p ~/turtlebot3_ws/src       #패키지 만들기
$ cd ~/turtlebot3_ws/src/        
$ git clone -b humble https://github.com/ROBOTIS-GIT/DynamixelSDK.git
$ git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git
$ sudo apt install python3-colcon-common-extensions   #colcon 명령 패키지 설치
$ cd ~/turtlebot3_ws
$ colcon build --symlink-install  
$ echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
#>>는  /.bashrc에다 써라
$ source ~/.bashrc
```

```
$ export TURTLEBOT3_MODEL=burger
# 이것도 계속 치기 어려우면 brashrc에 넣으면 됨!
$ ros2 launch turtlebot3_bringup robot.launch.py
#                    <패키지이름>     <런치 파일>
```


```
 export RMW_IMPLEMENTATION=rmw_fastrtps_cpp  
```
->DDS 를 다른 걸로 바꾸고 싶을 때 사용
->rmw_fastrtps_cpp 이거를 원하는 걸로 바꿔주면 됨!
DDS 별로 특징이 있음!

/scan은 라이더 정보

프로젝트에서

yolo
- object detection
- point key

실습 시간에 yolo 프로젝트 만들어보기!!

labeling


로보플로어로 학습하고 추론한 결과 사진 하나(추론 결과 저장)한 파일을 과제로 오늘 오후 6시까지 DM으로 보내주시기 바랍니다.


[[프로젝트 교안(GAZEBO)_1010.pdf]]
가상환경 파일의 확장자 sdf

< sdf >: 요소

과제1
- [x] yolo로 객체 탐지한거 ✅ 2025-10-02

![[object detection실습 사진 1.png]]

과제2
가제보로 모델만들어서 제출
가제보 환경에서 자동차 만들면 됨!!!!

ws_car
파일 참조

pg 32 

라이다는 빼

p52
gazebo에는 2개의 버전이 있다.
1. Gazebo Classic(구버전)
	-> 명령어가 $gazebo... 로 시작한다.
2. Igntition Gazebo(신버전)
	->명령어가 $ign gazebo...  또는 $gz sim으로 시작한다.


구버전 gazebo 설치 방법
$sudo apt install gazebo11 -y
: gazebo classic 11 설치
$sudo apt install ros-humble-gazebo-ros-pkgs -y
:ros2 gazebo 패키지 설치
$echo "source /opt/ros/humble/setup.bash ">>~/.bashrc source~/.bashrc
:ros2 설정 source
$sudo apt install python3-colcon-common-extensions -y
:install additional tools (optional but recommended)

  Igntition Gazebo   명령어
  $ign gazebo --versions
  :Igntition Gazebo 버전 확인 명령어
$ign gazebo
:단독 실행 명령어
$ign gazebo /usr/share/gz-fortress/worlds/shapes.sdf
:예제 월드

__ign 명령어 옵션__
```
shim@shim-Lenovo-Y520-15IKBN:~/github/XYZ_robot$ ign --version The 'ign' command provides a command line interface to the ignition tools. ign <command> [options] 

List of available commands: 
help: Print this help text. 
fuel: Manage simulation resources. 
gazebo: Run and manage Gazebo. 
gui: Launch graphical interfaces. 
launch: Run and manage executables and plugins. 
model: Print information about models. 
msg: Print information about messages. 
plugin: Print information about plugins. 
sdf: Utilities for SDF files. 
topic: Print information about topics. 
service: Print information about services. 
log: Record or playback topics. 
param: List, get or set parameters. 
Options: 
--force-version <VERSION> Use a specific library version.
--versions Show the available versions. 
--commands Show the available commands. 
Use 'ign help <command>' to print help for a command.
```

강화학습 강의자료 링크: https://atmokpo.com/w/40462  
## 1. 강화학습의 정의
강화학습은 __에이전트__ 가 환경과 상호작용하며, __보상을 최대화하는 방향으로 행동을 학습하는 방법론__ 입니다. 에이전트는 다양한 상태에서 행동을 선택하고, 그 행동의 결과로 보상을 받습니다. 이 보상을 이용하여 에이전트는 향후 의사결정을 개선할 수 있도록 학습하게 됩니다.

## 2. 강화학습의 주요 구성 요소
강화학습은 다음의 주요 구성 요소로 이루어져 있습니다:

- **에이전트 (Agent)**: 환경과 상호작용하여 행동을 결정하고, 이를 통해 학습하는 주체입니다.
- **환경 (Environment)**: 에이전트가 상호작용하는 대상이며, 에이전트의 행동에 대한 반응을 제공합니다.
- **상태 (State)**: 환경의 특정 시간에서의 시점으로, 에이전트가 현재 어떤 상황에 처해 있는지를 나타냅니다.
- **행동 (Action)**: 에이전트가 선택할 수 있는 다양한 움직임이나 결정입니다.
- **보상 (Reward)**: 에이전트가 특정 행동을 취한 후에 환경이 에이전트에게 주는 값으로, 행동의 유용성을 평가하는 기준이 됩니다.
- **정책 (Policy)**: 특정 상태에서 어떤 행동을 취할지 결정하는 전략입니다.
- **가치 함수 (Value Function)**: 특정 상태가 얼마나 좋은지를 평가하는 함수로, 장기적인 보상을 예측합니다.

->에이전트의 행동에 따라서 보상함수를 준다
ex) 1번 움직일 때마다 - 점수를 줌, 길을 잘못 들면 0-점수 줌

## 3. 강화학습의 기본 과정
강화학습의 기본 과정은 다음과 같습니다:

1. 에이전트는 현재 상태를 관찰합니다.
2. 정책에 따라 행동을 선택합니다.
3. 선택한 행동을 환경에 적용합니다.
4. 환경은 새로운 상태와 보상을 에이전트에게 반환합니다.
5. 에이전트는 보상을 통해 정책을 업데이트하고, 다음 에피소드로 넘어갑니다.

## 4. 강화학습 알고리즘
강화학습에는 여러 알고리즘이 존재합니다. 그 중 몇 가지를 소개합니다:

- **Q-러닝 (Q-Learning)**: 오프라인 학습 방법으로, 가치 함수 기반의 방법입니다. 에이전트는 경험을 통해 Q-값(상태-행동 값)을 업데이트하며, 최적의 정책을 학습합니다.
- **정책 경사법 (Policy Gradient)**: 직접적으로 정책을 최적화하는 방법으로, 정책을 연속적으로 업데이트하여 강화학습을 진행합니다. 이 방법은 복잡한 행동 공간을 처리하는 데 유리합니다.
- **심층 Q-네트워크 (DQN)**: 신경망을 사용하여 Q-러닝의 강화 버전으로, 대규모 상태 공간을 처리할 수 있습니다. 경험 재플레이와 목표 네트워크의 개념이 포함되어 있습니다.

-> Q 러닝에 대해 이해하면 좋음!!
## 5. 강화학습의 응용
강화학습은 다양한 분야에서 활용됩니다:

- **게임 AI**: 바둑, 체스, 비디오 게임 등의 AI를 개발하는 데 사용됩니다.
- **로봇공학**: 로봇의 행동을 제어하고 최적화하는 데 적용됩니다.
- **자율주행차**: 도로 상황을 인식하고 최적의 주행 경로를 찾아내는 데 도움을 줍니다.
- **금융 분야**: 투자 전략을 학습하여 수익을 극대화하는 데 이용됩니다.

## 6. 파이썬으로 강화학습 구현하기
강화학습을 실제로 구현하기 위해, 파이썬의 `gym` 라이브러리를 사용하는 예제를 소개하겠습니다. `gym`은 강화학습 환경을 쉽게 설정할 수 있는 라이브러리입니다.

```python
import gym
import numpy as np

# 환경 설정
env = gym.make('CartPole-v1')
num_episodes = 1000

# Q-테이블 초기화
Q = np.zeros((env.observation_space.shape[0], env.action_space.n))

# 학습 과정
for episode in range(num_episodes):
    state = env.reset() #환경을 다시 초기화
    done = False

    while not done:
        action = np.argmax(Q[state])  # 현재 상태에서 가장 큰 Q 값 선택
        next_state, reward, done, _ = env.step(action)  # 행동 수행
        # 다음 동작,   보상값,   끝남
        Q[state, action] += 0.1 * (reward + np.max(Q[next_state]) - Q[state, action])  # Q 값 업데이트
        state = next_state

env.close()    
```
## 결론
강화학습은 기계학습의 한 분야로, 에이전트가 환경과 상호작용하며 스스로 학습하는 과정입니다. 다양한 알고리즘과 응용 분야가 있으며, 파이썬을 통해 쉽게 구현할 수 있습니다. 앞으로도 강화학습 기술이 발전하여 더욱 많은 분야에 활용되기를 기대합니다.



과제3
과제는: 5X5격자에 3개연달아 있는 2개의 벽이 있습니다. 그리고 시작은 (0,0) 이고 골은 (5,5) 있습니다.
이것을 상하좌우로 움직이는 에이전트가 있습니다.
100번의 에피소드를 수행하는 학습 코드를 파이썬 및 gem 페키지를 이용해서 개발하세요.


가 있는 벽이 있는 곳에서 처음 시작하는 부분에서 끝나는 곳으로 강화학습을 통해 

어떻게 했는지 레포트에 
ppt에 


이벤트 안내



다음 주 금요일까지
첫번째 두번째 세번째 


<q_learning 5 * 5 코드>
```python
import numpy as np
import random

# 5x5 미로 정의 (0: 통로, 1: 벽)
maze = np.array([
[0, 0, 0, 0, 0],
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 0]
])

SIZE = maze.shape[0]
START = (0,0)
GOAL = (4,4)

# 상태 개수: (x,y) 좌표 → 정수로 변환
def coord_to_state(x,y): return y*SIZE+x
def state_to_coord(s): return (s%SIZE, s//SIZE)

# 행동 정의 (상, 우, 하, 좌)
ACTIONS = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}

# 환경 step 함수
def step(pos, action):
x,y = pos
dx,dy = ACTIONS[action]
nx,ny = x+dx,y+dy

# 경계 및 벽 체크
if 0<=nx<SIZE and 0<=ny<SIZE and maze[ny][nx]==0:
new_pos = (nx,ny)
else:
new_pos = (x,y) # 못 가면 제자리

# 보상
if new_pos == GOAL:
	reward, done = 100.0, True
else:
	reward, done = -1.0, False
	return new_pos, reward, done

# Q-learning 학습
N_STATES = SIZE*SIZE
N_ACTIONS = 4
Q = np.zeros((N_STATES,N_ACTIONS))

alpha,gamma = 0.2,0.99
epsilon,eps_min,eps_decay = 1.0,0.05,0.95
rng = np.random.default_rng(0)

for ep in range(100):
	pos = START
	s = coord_to_state(*pos)
	total = 0
	done = False

while not done:
# ε-greedy 선택
if rng.random() < epsilon:
	a = rng.integers(N_ACTIONS)
else:

a = np.argmax(Q[s])
pos2,r,done = step(pos,a)
s2 = coord_to_state(*pos2)
# Q 업데이트
Q[s,a] += alpha*(r + gamma*np.max(Q[s2]) - Q[s,a])
pos, s = pos2, s2
total += r

epsilon = max(eps_min, epsilon*eps_decay)
if (ep+1)%10==0:
	print(f"Episode {ep+1} | Return {total} | epsilon {epsilon:.3f}")

# 학습된 정책으로 주행
pos = START
path = [pos]
total=0
done=False

while not done:
	s = coord_to_state(*pos)
	a = np.argmax(Q[s])
	pos,r,done = step(pos,a)
	path.append(pos)
	total += r
	print("\n최종 경로:", path)
	print("총 보상:", total, " | 목표 도달:", done)
```

코드 설명

## 1) 판 깔기 (미로 만들기)
- 바둑판 같은 **6×6 칸**이 있어요. 
- **시작점 S**는 (0,0), **목표 G**는 (5,5).
- **벽[#]** 은 막혀 있어서 지나갈 수 없어요.
- 주인공 **에이전트 A**가 **위·오른쪽·아래·왼쪽**으로 한 칸씩 움직일 수 있어요.
## 2) 점수 규칙
- 칸을 **한 번 움직일 때마다 -1점** (괜히 돌아다니면 손해!)
- **목표 지점에 도착하면 +100점!**  
    → 빨리, 안전하게 **G**에 도착하는 길을 찾는 게 최고 점수를 받는 길이에요.
## 3) 연습 게임 100번 (에피소드 100개)
- 한 번의 연습을 **에피소드**라고 불러요.
- 처음엔 길을 몰라서 **아무 방향**으로도 가 봐요(탐험).
- 점점 **점수(보상)**를 보고 “어? 이쪽이 더 좋네!” 하며 **좋은 길을 기억**해요.
- 이 기억장을 **Q-테이블(일종의 지도 메모장)**이라고 부릅니다.
    - “이 칸에서는 오른쪽이 좋다!” 같은 정보를 숫자로 저장해요.
## 4) 똑똑해지는 방식(아주 쉽게)
- 좋은 일이 생기면(점수가 높으면) **그때 했던 선택을 더 좋게 평가**해요.
- 나쁜 일이 생기면(점수가 낮으면) **그때 했던 선택 점수를 깎아요.**
- 이렇게 **좋은 선택 점수는 올리고, 나쁜 선택 점수는 내리며** 똑똑해져요.
## 5) 처음엔 모험, 나중엔 실력발휘
- 초반엔 **모험(랜덤)**을 많이 해요: 여러 길을 다 가봐야 뭐가 좋은지 알죠.
- 점점 **모험을 줄이고**(ε가 줄어듦) **제일 점수 높은 선택**만 하게 돼요.

---

# 실행 결과를 보면?

### 학습 중 출력
`Episode  10 | Return:   62.00 | epsilon: 0.599 ... Episode 100 | Return:   87.00 | epsilon: 0.050`
- `Return`은 한 에피소드에서 받은 **총점**이에요.
- 숫자가 점점 좋아지는 건 **길을 점점 더 잘 찾는다**는 뜻!
- `epsilon`은 **모험 정도**예요. 1에 가까울수록 막 가보고, 0에 가까울수록 **가장 좋은 선택**만 골라요.

### 마지막 “롤아웃”(실전 주행) 화면
- 콘솔에 보드가 **여러 장** 찍힌 건, A가 **한 칸씩 움직일 때마다 판을 보여준 것**이에요.
- `S`에서 시작해서 벽을 피해 **G까지 착착 이동**하죠.
### 최종 경로/점수
`경로: [(0,0) → (0,1) → ... → (5,5)] 총 보상: 91.0 | 목표 도달: True`
- **한 칸 움직일 때마다 -1점**을 내면서도, 마지막에 **+100점**을 받아서 **총 91점**이 된 거예요.
- 즉, **10번 움직여서** 도착했다는 뜻(100 - 9 또는 100 - 10 부근).
- `목표 도달: True`니까 **성공!**

---
# 한 줄 요약
- 이 코드는 “**미로에서 목표까지 최단·안전 경로를 배우는 로봇**”이에요.
- 100번 연습하면서 **좋은 길을 기억(Q-테이블)**하고, 마지막엔 **그 기억대로 척척 이동**해서 골인!

---

# 더 궁금할 수 있는 것들

- **왜 벽을 뚫지 않지?**  
    → 벽 좌표는 이동 금지라서, 그 칸으로는 **아예 못 가요**(가려다 제자리).
    
- **왜 돌아가기도 하지?**  
    → 초반엔 모험 때문에 돌아갈 수 있어요. 나중엔 최적 경로로 바뀝니다.
    
- **점수를 바꿔보면?**  
    → 이동 벌점을 더 크게 하면 **더 빠른 길**을 더 강하게 배우고, 작게 하면 **돌아가도 덜 손해**라 경로가 달라질 수 있어요.
    

필요하면 **벽 위치**나 **보상 규칙**, **학습 횟수**를 살짝 바꿔서 실험해보세요. 어떤 설정이 가장 빨리·안전하게 가는지 바로 느껴질 거예요!

