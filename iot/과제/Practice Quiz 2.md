Practice Quiz #2: Interrupt-Based Touch Sensor and Led

§ Touch 센서가 눌릴 때 "Pressed"라고 출력하고, Led를 1초 동안 킨다. 

§ 센서는 인터럽트로 읽는다(digtalRead() 함수 사용하면 안 됨, wiringPiISR() 함수는 사용해야 함). 센서가 눌릴 때만 "Pressed"라고 출력한다.

§ 제출: C 소스 코드

참고 코드: 한백 전자에서 제공한 코드: wiringPiISR을 한  핀에 대해서 여러 번 부르면 부를 때 마다 쓰레드가 생성되므로 바람직하지 않음}