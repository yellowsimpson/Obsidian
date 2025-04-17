![[스크린샷 2025-04-17 오후 10.44.56.png]]
![[스크린샷 2025-04-17 오후 11.29.11.png]]
```c
#include <stdio.h>
#include <wiringPi.h>

#define TRIG 28
#define OUT 29

int main(void) {
    int dis = 0, i;
    long start, travel;

    if (wiringPiSetup() == -1) return 1;
    pinMode(TRIG, OUTPUT);
    pinMode(OUT, INPUT);

    for (i = 0; i < 20; i++) {
        // TRIG pin must start LOW
        digitalWrite(TRIG, 0);
        // Wait for sensor to settle
        usleep(2);

        // Send trig pulse
        digitalWrite(TRIG, 1);
        usleep(20);
        digitalWrite(TRIG, 0);

        // Wait for echo start
        while (digitalRead(OUT) == 0);

        start = micros();

        // Wait for echo end
        while (digitalRead(OUT) == 1);

        travel = micros() - start;

        /*
         * Speed of Sound: 340m/s = 29 microseconds/cm
         * Sound wave reflects from the obstacle, so to calculate the distance
         * we consider half of the distance traveled.
         * DistanceInCms = microseconds / 29 / 2
         */
        dis = travel / 58;
        printf("%d\n", dis);
        delay(100);
    }
}
```