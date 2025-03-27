![[Pasted image 20250327213238.png]]
![[Pasted image 20250327213300.png]]
![[Pasted image 20250327213318.png]]
![[Pasted image 20250327213337.png]]


```c
#include <wiringPi.h>

#define PIN 15

int main(void){
	if(wiringPiSetup() == -1) return 1;

	pinMode(PIN, OUTPUT);

	digitalWrite(PIN,HIGH);
	delay(500);
	digitalWrite(PIN,LOW);
}

```
