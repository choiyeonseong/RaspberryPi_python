/*
	wiringPi를 이용해서 GPIO 사용
	led 전구 깜빡거리게
*/

#include <stdio.h>
#include <wiringPi.h>
#define LED 21	// 핀번호 정의
void main()
{
	printf("my first LED\n");
	wiringPiSetupGpio();
	pinMode(LED,OUTPUT);	// 초기화
	while(1)
	{ 
		digitalWrite(LED,HIGH);	// led on
		delay(100);
		digitalWrite(LED,LOW);	// led off
		delay(100);
	}
}

// gcc gpio_test.c -o gpio_test -lwiringPi	// 실행문
