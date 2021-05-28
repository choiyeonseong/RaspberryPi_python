from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def home():
        return render_template("index.html")

# 웹에서 버튼으로 조작
@app.route("/data", methods = ['POST']) # post방식
def data():
    data = request.form['led']
    if data == 'on':
        GPIO.output(ledPin, True)
        return home()   # 새로운 창이 아닌 첫 화면으로 돌아감
    elif data == 'off':
        GPIO.output(ledPin, False)
        return home()
    else :
        GPIO.cleanup()
        return "CLEANUP"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")