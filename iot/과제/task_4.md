가변 저항으로 LED 불빛 제어하기

```c
#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>

#define SPI_CH 0 // SPI channel (CE0)
#define ADC_CH 1 // ADC Channel connected to potentiometer
#define ADC_CS 29 // GPIO pin used as Chip Select (CS) for MCP3008
#define SPI_SPEED 500000 // SPI speed in Hz
#define PWM_PIN 1 // WiringPi pin 1 = GPIO 18 (hardware PWM)

int readADC(int adcChannel) {
	unsigned char buf[3];
	int value;

	buf[0] = 0x06 | ((adcChannel & 0x04) >> 2); // Start bit + single-ended
	buf[1] = ((adcChannel & 0x03) << 6); // Channel bits
	buf[2] = 0x00;

	digitalWrite(ADC_CS, LOW); // Pull CS low before communication
	wiringPiSPIDataRW(SPI_CH, buf, 3); // SPI data exchange
	buf[1] = 0x0F & buf[1]; // Mask to get lower 4 bits
	value = (buf[1] << 8) | buf[2]; // Combine to 10-bit value
	digitalWrite(ADC_CS, HIGH); // Pull CS high after transaction

	return value;
}

int main(void) {
	int value;
	
	if (wiringPiSetup() == -1) return 1;
	if (wiringPiSPISetup(SPI_CH, SPI_SPEED) == -1) return 1;

	pinMode(ADC_CS, OUTPUT);
	digitalWrite(ADC_CS, HIGH); // Default CS to high (inactive)
	pinMode(PWM_PIN, PWM_OUTPUT); // instead of OUTPUT use PWM_OUTPUT

	while (1) {
		value = readADC(ADC_CH); // Read potentiometer value (0–1023)
		value= value/4;
		pwmWrite(PWM_PIN, value); // digitalWrite() is replaced with pwmWrite()
	delay(50); // Smooth updates
	}
	return 0;
}

```
```c
#include <stdio.h>
#include <stdio.h>

#define SPI_CH 0
#define ADC_CH 4
#define SPI_CS 29
#define SPI_SPEED 500000

int main(void){
	int value = 0, i;
	unsigned char buf[3];
}
```

