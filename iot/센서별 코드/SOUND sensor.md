![[스크린샷 2025-04-21 오후 9.38.22.png]]
![[스크린샷 2025-04-21 오후 9.38.33.png]]
![[스크린샷 2025-04-21 오후 9.38.44.png]]


```c
#include <stdio.h>
#include <wiringPi.h>

#define SPI_CH 0
#define ADC_CH 2
#define ADC_CS 29
#define SPI_SPEED 500000

int main(void) {
	int value = 0;
	unsigned char buf[3];

	// wiringPi 초기화
	if (wiringPiSetup() == -1) return 1;

	if (wiringPiSPISetup() == -1) return -1;

	// ADC_CS 핀과 LED 핀을 출력 모드로 설정
	pinMode(ADC_CS, OUTPUT);
	  
	// 무한 루프에서 polling
	for(i = 0; i < 20; i++){
	// SPI 통신을 위한 버퍼 설정
		buf[0] = 0x06 | ((ADC_CH & 0x04) >> 2);
		buf[1] = ((ADC_CH & 0x03) << 6);
		buf[2] = 0x00;

	// ADC 데이터 읽기
	digitalWrite(ADC_CS, 0); // CS 활성화
	wiringPiSPIDataRW(SPI_CH, buf, 3);

	// 읽은 데이터 처리
	buf[1] = 0x0F & buf[1];
	
	value = (buf[1] << 8) | buf[2];
  
	digitalWrite(ADC_CS, 1);

	printf("%d\n", value);

	delay(100);
	}
}
```

