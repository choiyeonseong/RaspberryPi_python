# => 밝기조절

import RPi.GPIO as GPIO

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin,255)

p.start(0)

while True:
	d = input("Enter Brightness(0 to 100) : ")
	duty = int(d)
	
	if(duty == 100):
		p.stop()
		GPIO.cleanup()
		break
	else:
		p.ChangeDutyCycle(duty) # 출력값 변경