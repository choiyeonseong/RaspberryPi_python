## 평가용 코드

#-*-coding: utf-8-*-
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

ledPin = 21
pinPiezo = 13
triggerPin = 4
echoPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pinPiezo, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(triggerPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 255)
Buzz = GPIO.PWM(pinPiezo, 440)

@app.route('/')
def home():
    return render_template("test.html")

@app.route('/data', methods = ['POST'])
def data():
    data = request.form['func']
    if data == 'on':
        p.start(50)
        return home()

    elif data == 'off':
        p.stop()
        return home()

    elif data == 'light':
        moodlight()
        return home()

    elif data == 'music':
        music()
        return home()

    elif data == 'ultra':
        ultra()
        return home()

    elif data == 'clean':
        GPIO.cleanup()
        return "ALL CLEAN UP"

    else :
        return "잘못된 경로입니다."

def ultra():

    while True:
        GPIO.output(triggerPin, GPIO.LOW)   #GPIO.FALSE
        time.sleep(0.00001)
        GPIO.output(triggerPin, GPIO.HIGH)  #GPIO.TRUE

        while GPIO.input(echoPin) == 0:
            start=time.time()   # 시간 측정 시작
        while GPIO.input(echoPin) == 1:
            stop=time.time()    # 시간 측정 끝

        rtTotime = stop - start
        distance = rtTotime * 34000 / 2 # 거리구하는 식
        print("distance : %.2f cm" % distance)

        if distance <= 5:
            Buzz.start(50)
            time.sleep(0.1)
            Buzz.stop()
            time.sleep(0.1)

        elif distance > 5 and distance <= 10:
            Buzz.start(50)
            time.sleep(0.3)
            Buzz.stop()
            time.sleep(0.3)

        elif distance > 10 and distance <= 20:
            Buzz.start(50)
            time.sleep(0.5)
            Buzz.stop()
            time.sleep(0.5)
        else:
            Buzz.stop()
            time.sleep(0.5)

def music():

    Melody=[261, 294, 329, 349, 392, 440, 493, 523]

    while True:
        Buzz.start(50)
        for i in range(0, len(Melody)):
            Buzz.ChangeFrequency(Melody[i])
            time.sleep(0.5)
        Buzz.stop()
        time.sleep(0.3)

def moodlight():

    p.start(0)

    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in reversed(range(100)):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")
