# => 초음파 센서로 거리측정, 피에조 부저로 거리별 알림음 설정

#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

triggerPin = 14
echoPin = 4
buzzPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(buzzPin, GPIO.OUT)

Buzz = GPIO.PWM(buzzPin,440)

try:
    while True:
        GPIO.output(triggerPin, GPIO.LOW)   #GPIO.FALSE # 초음파를 송신 트리거 발생
        time.sleep(0.00001)                 # 10us동안 트리거 펄스 송신
        GPIO.output(triggerPin, GPIO.HIGH)  #GPIO.TRUE  # 트리거 펄스 중단
            
        while GPIO.input(echoPin) == 0: # 초음파 전송이 끝나는 전송시간
            start=time.time()           # 시간 측정 시작
        while GPIO.input(echoPin) == 1: # 초음파 수신이 완료될때까지 수신시간
            stop=time.time()            # 시간 측정 끝
           
        rtTotime = stop - start         # 수신시간에서 전송시간을 빼서 총 도달시간 산정
        distance = rtTotime * 34000 / 2 # 거리구하는 식
        print("distance : %.2f cm" % distance)
        time.sleep(1)
        
        if distance <= 5 :
            Buzz.start(50)      # 듀티비 설정
            time.sleep(0.1)    # 소리가 나오는 시간
            Buzz.stop()
            time.sleep(0.1)     # 반복되는 소리를 위해서 sleep 설정
            
        elif distance > 5 and distance <= 10 :
            Buzz.start(50)
            time.sleep(0.3)
            Buzz.stop()
            time.sleep(0.3)
            
        elif distance > 10 and distance <= 20 :
            Buzz.start(50)
            time.sleep(0.5)
            Buzz.stop()
            time.sleep(0.5)
           
        else:   # 20cm 이상은 else로 처리(반복되는 소리를 위해서)
            Buzz.stop()
            time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()