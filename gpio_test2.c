/*
	초록, 빨강 led 전구 번갈아 가면서 깜빡거리게
*/


#include <stdio.h>
#include <wiringPi.h>
#define LED_GREEN	21	// 핀번호 설정
#define LED_RED		16
void main()
{
   printf("my first LED2\n");
   wiringPiSetupGpio();
   pinMode(LED_GREEN,OUTPUT);	// 핀 초기화
   pinMode(LED_RED,OUTPUT);
   while(1)
   {
	  digitalWrite(LED_GREEN,HIGH);
	  digitalWrite(LED_RED,LOW);
	  delay(100);
	  digitalWrite(LED_GREEN,LOW);
	  digitalWrite(LED_RED,HIGH);
	  delay(100);
   }
}