
![[스크린샷 2025-04-17 오후 11.30.23.png]]![[스크린샷 2025-04-17 오후 11.32.06.png]]

```c
#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>

#define SPI_CH 0
#define ADC_CH 1
#define ADC_CS 29
#define SPI_SPEED 500000

int readADC(int adcChannel){
	unsigned char buf[3];
	int value;

	buf[0] = 0x06 | ((adcChannel &0x04) >> 2);
	buf[1] = ((adcChannel * 0x03) << 6);
	buf[2] = 0x00;

	digitalWrite(ADC_CS, 0);
	wiringPiSPIDataRW(SPI_CH, buf, 3);
	digitalWrite(ADC_CS, 1);

	buf[1] = 0x0F & buf[1];
	value = (buf[1] << 8) | buf[2];

	return value;
}

int main(void){
	int i, value;

	if(wiringPiSetup() == -1)
		return 1;
	if(wiringPiSPISetup(SPI_CH, SPI_SPEED) == -1)
		return -1;

	pinMode(ADC_CS, OUTPUT);

	for(i = 0; i < 20; i++){
		value = readADC(ADC_CH);
		printf("%d\n", value);
		delay(100);
	}
	return 0;
}
```

