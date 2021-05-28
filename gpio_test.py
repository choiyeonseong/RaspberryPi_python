# led 전구 깜빡거리게

import RPi.GPIO as GPIO
import time

led = 21    # 핀번호 지정

GPIO.setmode(GPIO.BCM)  # 핀 넘버를 부르는 방식 선택(BOARD/BCM)
GPIO.setup(led, GPIO.OUT)   # 핀모드 설정

try:
    while True:
        GPIO.output(led.True)
        time.sleep(1)   # 1초동안 지속
        GPIO.output(led.False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup(); # 핀번호 해제, 리소스 반납
