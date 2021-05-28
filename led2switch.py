** on스위치 1개와 off스위치 1개로 LED 조작
import RPi.GPIO as GPIO
import time

switch1 = 5     //입력핀 설정
switch2 = 6
led = 21

GPIO.setmode(GPIO.BCM)       //BCM 모드 설정(핀의 번호만 가져오는 모드)
GPIO.setup(switch1, GPIO.IN) //핀모드 설정(입력)
GPIO.setup(switch2, GPIO.IN) //핀모드 설정(입력)
GPIO.setup(led, GPIO.OUT)    //핀모드 설정(출력)

try:
	while True:
		if GPIO.input(switch1) == True: //5V를 흐르게 해주면(switch1의 핀번호 5에 전류를 흐르게 해준다)
			print("ON")
			time.sleep(0.3)
			GPIO.output(led, True)      //led의 핀번호 21에 전류를 흐르게 해준다 → led ON
		elif GPIO.input(switch2) == True:
			print("OFF")
			time.sleep(0.3)
			GPIO.output(led, False)
except KeyboardInterrupt:               //예외처리 구문
    GPIO.cleanup()