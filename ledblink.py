# => led를 1초단위로 깜빡거리게 10번 

import RPi.GPIO as GPIO
import time

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
	for i in range(10):
	GPIO.output(ledPin, True)
	time.sleep(0.5) # 0.5초
	GPIO.output(ledPin, False)
	time.sleep(0.5)
	print(i)

except KeyboardInterrupt:
	GPIO.cleanup()