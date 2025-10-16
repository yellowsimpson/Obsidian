

코드 형식

__GlobalVariables

---

__Main Sub

---

__End Main Sub


drl은 while이랑 for 문 없이
repeat으로 다 사용 가능!


두산 로보틱스 ros2를 깔아야됨

시스템 명령어
- tp_popup() : 메시지 제공
- wait()
- posj ()
	posj(j1 = 0, j2 = 0, j3 = 0, j4 = 0, j5 = 0, j6 = 0 )
- posx()
	posx(x = 0, y = 0, z = 0, a = 0, b = 0, c = 0)
- set_velj()
	set_velj(vel)
	->조인트 모션에서 전역 속도를 설정
- set_accx()
	set_accx(acc1, acc2)
	->작업 공간 모션의 가속도를 설정합니다.
- set_velx()
	set_velx(vel1, vel2, clamp)
	->작업 공간 모션의 속도를 전역적으로 설정합니다. 

- movej()
	movej(pos, vel, acc, time, radius, mod, ra, ref, velx)
	->로봇이 현재 관절 위치에서 목표 관절 위치(pos)로 이동합니다.
- movel()
	movel()
- amovej()
	->비동기방식의 movej로 블렌딩을 위한 radius 인자를 갖지 않는 점을 제외하고 movej와 동일하게 작동합니다. 그러나 해당 명령어는 async 방식의 모션 명령어로 모션 시작과 동시에 다음 명령어를 수행합니다.
- servoj()
	servoj(pos, vel, acc, time, mod)
	->비동기 방식의 모션 시작과 동시에 다음 명령어를 수행합니다. 