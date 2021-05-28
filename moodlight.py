## 무드등
import RPi.GPIO as GPIO
import time

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
 
try:
    p.start(0)

    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in reversed(range(100)):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

