![[스크린샷 2025-04-21 오후 7.49.29.png]]
![[스크린샷 2025-04-21 오후 7.49.57.png]]
![[스크린샷 2025-04-21 오후 7.50.10.png]]


```c
#include <wiringPi.h>

#define PIN_INA 26
#define PIN_INB 23

int main(){
	if(wiringPiSetup() == -1) return 1;  //wiringPi 라이브러리 초기화

	pindMode(PIN_INA, OUTPUT);
	pindMode(PIN_INB, OUTPUT);

	digitalWrite(PIN_INA, HIGH);
	delay(2000);
	digitalWrite(PIN_INA, LOW);
	digitalWrite(PIN_INB, HIGH);
	delay(2000);
	digitalWrite(PIN_INB, LOW);
}
```
