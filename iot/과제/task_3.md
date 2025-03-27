
- Write a C program for a Raspberry Pi using the wiringPi numbering to control four LEDs (D1 ~ D4) connected to GPIO pins. This program truns all LEDs on and off in a loop with a 1-second delay.
- The LEDs are connected to GPIO pins(0,1,2,3)
- The wiringPi library is used for GPIO control.

- Combine the PIR sensor and LED projects so that the LED turns on when the PIR sensor detects motion. The LED will turn off once the motion is no longer detected.

<led_pir_combine.c>
```c
#include <wiringPi.h>
#include <stdio.h>

#define PIR_PIN 2    // PIR 센서 핀
#define PIN7    7    // LED1
#define PIN12   12   // LED2
#define PIN13   13   // LED3
#define PIN14   14   // LED4

int main(void) {
    // wiringPi 초기화
    if (wiringPiSetup() == -1) {
        printf("Failed to initialize wiringPi Library\n");
        return 1;
    }

    // LED 핀을 출력 모드로 설정
    pinMode(PIN7, OUTPUT);
    pinMode(PIN12, OUTPUT);
    pinMode(PIN13, OUTPUT);
    pinMode(PIN14, OUTPUT);

    // PIR 센서 핀을 입력 모드로 설정
    pinMode(PIR_PIN, INPUT);

    // 모든 LED를 처음에 꺼진 상태로 초기화
    digitalWrite(PIN7, LOW);
    digitalWrite(PIN12, LOW);
    digitalWrite(PIN13, LOW);
    digitalWrite(PIN14, LOW);

    printf("PIR Sensor Test Starting...\n");

    while (1) {  // 무한 루프
        int pir = digitalRead(PIR_PIN);  // PIR 센서 값 읽기

        if (pir == HIGH) {  // 움직임이 감지되었을 때
            // 모든 LED 켜기
            digitalWrite(PIN7, HIGH);
            digitalWrite(PIN12, HIGH);
            digitalWrite(PIN13, HIGH);
            digitalWrite(PIN14, HIGH);
            printf("Motion detected! LEDs ON\n");
        } else {  // 움직임이 감지되지 않을 때
            // 모든 LED 끄기
            digitalWrite(PIN7, LOW);
            digitalWrite(PIN12, LOW);
            digitalWrite(PIN13, LOW);
            digitalWrite(PIN14, LOW);
            printf("No motion detected. LEDs OFF\n");
        }

        delay(100);  // 0.1초 대기 (센서 읽기 주기)
    }

    return 0;
}

```


