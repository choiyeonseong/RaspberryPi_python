# => 무한으로 깜빡거리게

#! /usr/bin/env python  # 셔뱅으로 파이썬 버전 설정
                        # 스크립트를 실행시켜줄 프로그램의 경로 지정

import RPi.GPIO as GPIO
import time

ledPin = 21
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        GPIO.output(ledPin, True)
        time.sleep(0.5) # 0.5초
        GPIO.output(ledPin, False)
        time.sleep(0.5)
    
except KeyboardInterrupt:
    GPIO.cleanup()