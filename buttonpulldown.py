=> 버튼 누를때 마다 rising 신호일 때 flag 값 제어 -> interrupt 발생 => led 점등

#-*-coding: utf-8-*-
import RPi.GPIO as GPIO
import time

led = 21
switch = 6
flag = False
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  #  내부 풀다운 사용
# 라즈베리파이 내부에 풀다운 저항을 만들어 놓고 sw로 활성화 할수 있다
GPIO.setup(led, GPIO.OUT)  #  led output

def swBlink(channel):   #  callback 함수
	global flag
	if flag == False:
		print("interrupt")
		GPIO.output(led, True)
		time.sleep(0.3)   #  시간지연을 통해 스위치 시그널을 깔끔하게 인식
		flag = True
	else:
		GPIO.output(led, False)
		time.sleep(0.3)
		flag = False
#  인터럽터핀에 라이징 신호가 인가되면 콜백 함수로 리턴되어 실행된다.
GPIO.add_event_detect(switch, GPIO.RISING, callback = swBlink)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()