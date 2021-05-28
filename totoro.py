=> 토토로 악보
#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

C = 262
D = 294
E = 330
F = 349
G = 392
A = 440
B = 494
Cc = 523
T = 1

pinPiezo = 21
Melody = [E,G,Cc,1,G,A,G,T,C,E,G,Cc,B,A,G]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)  # pwm 초기화

try:
    while True:
        Buzz.start(50)
        for i in range(0, len(Melody)):
            Buzz.ChangeFrequency(Melody[i]) # 주파수 변경
            time.sleep(0.3)
        Buzz.stop()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()