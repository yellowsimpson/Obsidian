2025.10.14(화)
강의 자료
- [[두산 로봇교육 강의자료_1014.pdf]]
- [[Doosan_Robotics_Programming_Manual_V2.10.3_v2.10_KR.pdf]]

Task Builder
- Sync(동기): 신호를 주고 다시 받을 때까지 __기다림__
- Async(비동기): 모션 명령어가 시작함과 동시에 다음 명령어로 이동
- 반경
- Duplicate
- Override

IO 관련


시스템 명령어
- waite()
- exit()
- sub_program_run()
- drl_report_line()
- set-fm()
- get-robot_model()
- get_robot_serial_num()
- check_robot_jts()
- check_robot_fit()
- start_timer()
- end_timer()

이번주 금요일 세미 프로젝트??


DART-Platfrom 
- home
- workcell manager
- Task Builder
- Task Writer


모든 명령어
- Move
- Move J
- Move L
- Move SX
- Move SJ
- Move C
- Move B
- Move Spiral
- Move Periodic
- Move JX
- Stop Motion
- Wait Motion

흐름 제어 명령
- If
- Else If
- Repeat
- Continue
- Break
- Exit
- Sub
- Call Sub
- Thread
- Run Thread
- Kill Thread
- Sub
-  Task
- Call Sub Task
- Wait
- User Input
- Watch Smart Pendant

힘 제어 명령
- Compliance
- Force

기타 명령
- Comment
- Custom Code
- Define
- Popup
- Set
- Gloabal/Variables

고급 명령어
- Set_Digital_IO_v2
- Door_OpenClose_v2


금요일날 프로젝트 할때 
task writer를 사용하기 바람!


custom 코드는 여기 작성하고 이름을 설정해준다

시스템 표시는 앞에 $ 표시


flow control
순차적으로 진행되는 코드

순응 제어 
pg 82
Compliance(ON)
안에 스프링? 이 있어서 힘을 줘서 움직이면 다시 원래 자리로 돌아옴


Compliance(ON)
Compliance(OFF)
-> ON , OFF 쌍으로 움직임

FORCE(ON)
FORCE(OFF
-> 이것도
-> z 축으로 밀거나 땡겨준다.

weight을 조절해줌


힘 감지
- Force 명령어로 일정한 방향으로 이동중, 힘 모니터링 함수를 화용하여 접촉이 감지되면 다음 동작을 실행
- 다양한 높잎에서 작업물의 높이를 감지
	->로봇암이 내려오다 바닥에 붙이치면 다음 동작!

pg87
__오늘 오전 과제: pick and place 
문법을 사용해서!!
가능한 문법적인 것을 사용해서!!

moveL



평가자들이 질문을 할 수 있는 껀덕지를 줘야된다!
과정 중에 어떤 에러 사항이 있었는지

면접 질문
1. ai 활용도가 얼마나되나?
2. 나를 채용 했을 때 ai 보다 좋은점은??

xyz 인턴 종류
1. 피지컬
2. 인공지능
3. 임베디드

김병조


내가 가는 길을 가라!!
