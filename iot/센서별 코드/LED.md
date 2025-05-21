![[Pasted image 20250327212230.png]]
![[Pasted image 20250327212250.png]]
![[Pasted image 20250327212308.png]]


<led.c>
```c
#include <wiringPi.h>
#include <stdio.h>

#define PIN 7

int main(void) {
    if (wiringPiSetup() == -1) {  // wiringPi 라이브러리 초기화
        printf("Failed to initialize wiring Library\n"); // -1 리턴 실패
        return 1;
    }

    pinMode(PIN, OUTPUT); // PIN을 출력모드로 설정

         int i;

    for (i = 0; i < 30; i++) {
        digitalWrite(PIN, HIGH); // PIN에 전기를 보내 LED를 켜는 명령
        delay(100); // 0.1초 켜짐, 단위는 밀리
        digitalWrite(PIN, LOW); // PIN에 전기를 끊어서 LED를 끄는 명령
        delay(100); // 0.1초 꺼짐, 단위는 밀리
    }

    return 0;
}

```

<led_py>
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

while(True):
GPIO.output(17,False)
time.sleep(2)
GPIO.output(17,True)
time.sleep(2)
```


