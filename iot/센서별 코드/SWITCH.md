![[Pasted image 20250327213623.png]]
![[Pasted image 20250327213640.png]]
![[Pasted image 20250327213657.png]]

```c
#include <wiringPi.h>
#include <stdio.h>

#define PIN 3

int main(void){
	int sw, i;

	if(wiringPiSetup() == -1) return 1;
	pinMode(PIN,INPUT);

	for(i=0; i<20; i++){
		sw = digitalRead(PIN);
	printf("%d\n", sw);
	delay(100);
	}
}
```

![[Pasted image 20250327214137.png]]


