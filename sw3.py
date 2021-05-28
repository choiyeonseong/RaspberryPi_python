## 스위치 1개로 점멸하기

#-*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch1 = 6
switcho = 5
state = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switcho, GPIO.OUT)

try:
	while True:
		if GPIO.input(switch1) == True:
			time.sleep(0.3)
			state += 1

		if state % 2 == 0:
			GPIO.output(switcho, True)
			#print("ON")
		elif state % 2 != 0:
			GPIO.output(switcho, False)
			#print("OFF")

except KeyboardInterrupt:
    GPIO.cleanup()