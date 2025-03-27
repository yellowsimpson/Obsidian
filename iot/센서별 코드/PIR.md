![[Pasted image 20250327133908.png]]

![[Pasted image 20250327133939.png]]

<pir.c>
```c
#include <wiringPi.h>
#include <stdio.h>

#define PIN 2

int main(void) {
        int pir, i;

        if(wiringPiSetup() == -1) return 1;
        pinMode(PIN, INPUT);

        for(i=0; i < 20; i++){
                pir = digitalRead(PIN);
                printf("%d\n", pir);
                delay(100);
                }
}

```