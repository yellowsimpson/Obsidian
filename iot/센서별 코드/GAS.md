
![[스크린샷 2025-04-17 오후 11.23.00.png]]
![[스크린샷 2025-04-17 오후 11.23.10.png]]
![[스크린샷 2025-04-17 오후 11.23.17.png]]

```c
#include <stdio.h>
#include <wiringPi.h>

#define SPI_CH 0         //`SPI_CH`: 사용할 SPI 채널 (보통 0 또는 1)
#define ADC_CH 4         //`ADC_CH`: ADC의 입력 채널 번호 (0~7 중 하나, 여기선 채널 4)
#define SPI_CS 29        //`SPI_CS`: Chip Select 핀 번호
#define SPI_SPEED 500000 //`SPI_SPEED`: SPI 통신 속도 (단위: bps)

int main(void){
	int value = 0, i;
	unsigned char buf[3];                //SPI통신에 사용할 3바이트 버퍼

	if(wiringPiSetup() == -1) return 1;  //wiringPi 라이브러리 초기화

	pinMode(ADC_CS, OUTPUT);

	for(i = 0; i < 20; i++){
		buf[0] = 0x06 | ((ADC_CH & 0x04) >> 2);
		buf[1] = ((ADC_CH & 0x03)<<6);
		buf[2] = 0x00;
	
		//`buf[0]`: start bit (1), single/diff bit (1), D2 비트
	    //`buf[1]`: D1, D0 비트가 들어가며 나머지는 0
	    //`buf[2]`: dummy byte (데이터 받기 위한 자리)

		digitalWrite(ADC_CS, 0);            //CS LOW 통신 시작

		wiringPiSPIDataRW(SPI_CH, buf, 3);  //SPI 송수신

		buf[1] = 0x0F & buf[1];             //상위 4비트 마스킹

		value = (buf[1] << 8) | buf[2];     //12비트 결과 조합

		digitalWrite(ADC_CS, 1);            //CS high: 통신 종료

		printf("%d\n", value);

		delay(100);
	}
}
```

