# 스위치를 사용한 점멸 회로
# 스위치 안눌렀을 때 : 단선상태 -> 회로 동작x
#  --> 0v값이 인가되게 회로 구성해야함
# 풀다운 : 평소 0v, 스위치 누르면 5v -> 그라운드 쪽에 저항
# 풀업 : 평소 5v, 스위치 누르면 0v -> 전원 쪽에 저항

#-*- coding: utf-8-*- #주석설정
import RPi.GPIO as GPIO
import time

switch = 6      #입력핀설정

GPIO.setmode(GPIO.BCM)  #BCM 모드

GPIO.setup(switch, GPIO.IN) #핀모드(입력)

try:
	while True:
		if GPIO.input(switch) == True:
			print("Pushed")
			time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()