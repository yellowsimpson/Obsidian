Practice Quiz #6: Ultrasonic Sensor, Step Motor, LED, and Buzzer

- 프로그램을 수행하기 시작하면 step motor는 정상 회전으로 계속 돌아가야 한다.  
- Ultrasonic Sensor로 주변과의 거리 x를 0.1s 간격으로 측정한다. 
- 측정된 거리 x가 30cm 미만이면 'xcm < 30cm, Step Motor Stopped.' 라고 출력하고,  step motor를 중지시킨다.

- (예) 25cm < 30cm, Step Motor Stopped.

- Step motor가 중지되어 있다가 거리 x가 30cm 이상이 되면  'xcm >= 30cm, Step Motor Resumed.' 라고 출력하고, 다시 step motor가 돌아간다. 

- (예) 40cm >= 30cm, Step Motor Resumed.

- x가 20cm 미만이면 'xcm < 20cm, LED On.' 라고 출력하고,  LED를 켠다.

- (예) 17cm < 20cm, LED On.

- LED가 켜져 있다가 x가 20cm 이상이 되면  'xcm >= 20cm, LED Off.' 라고 출력하고, 다시 LED를 끈다.

- (예) 24cm >= 20cm, LED Off.

- x가 10cm 미만이면 'xcm < 10cm, Buzzer On.' 라고 출력하고,  buzzer를 울린다.

- (예) 3cm < 10cm, Buzzer On.

- Buzzer가 울리다가 x가 10cm 이상이 되면 'xcm >= 10cm, Buzzer Off.' 라고 출력하고, 다시 buzzer를 끈다.

- (예) 12cm >= 10cm, Buzzer Off.