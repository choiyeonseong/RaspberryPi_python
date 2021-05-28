from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def flask():
    return "<h1>LED Control WepPage</h1>"

# 주소에서 매개변수를 받아서 조작
@app.route('/led/<state>')   # <> : 매개변수, 동적 라우팅 함수
def led(state):
    if state == "on":
        GPIO.output(ledPin, True)  # led on
    else:
        GPIO.output(ledPin, False)  # led off

    return "LED" + state

@app.route('/led/clean')
def Clean():
    GPIO.cleanup()    # 핀을 cleanup()해야 점유된 리소스 해제
    return "<h1> GPIO CLEANUP </h1>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")