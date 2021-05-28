from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

#p = GPIO.PWM(ledPin, 255)  # duty 값을 조절하기 위해 PWM 사용

@app.route('/')
def flask():
    return "Hello Flask"

@app.route('/led/on')
def ledOn():
    #p.start(50)   # duty값을 줘서 조명 밝기조절
    GPIO.OUTPUT(ledPin, True)  # led on  
    return "<h2> Led ON </h2>"

@app.route('/led/off')
def ledOff():
    #p.stop()
    GPIO.OUTPUT(ledPin, False)  # led off
    return "<h2> Led OFF </h2>"
    
@app.route('/led/clean')
def Clean():
    GPIO.cleanup()    # 핀을 cleanup()해야 점유된 리소스 해제
    return "<h1> GPIO Clean </h1>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")