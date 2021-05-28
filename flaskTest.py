# =>flask서버 실행, 동적 
# 웹에 192.168.0.9:5000

from flask import Flask

app = Flask(__name__)   # __name__이름을 이용한 Flask 객체를 생성

@app.route('/')         # 클라이언트가 uri로 /를 요청하면
def hello():            # 뷰 함수가 실행된다.
    return "Hello Flask!!"  #뷰 함수는 반드시 return이 있어야 한다.

@app.route('/name') # 210.119.12.110:30922/name
def name():
    return "<h1> My name is Choi Yeon Seong </h1></br>I'm 25years old"

@app.route('/job')  # 210.119.12.110:30922/job
def job():
    return "<h1>Welcome!</h1></br><h2> I'm gardener </h2>"



if __name__ == "__main__":  # 직접 실행을 위한 조건
    #1 외부포트 설정 전
    app.run(host = '0.0.0.0')    # 192.168.0.9:5000
    #2 외부포트 설정 후
    app.run(host = '0.0.0.0', port = '8080')    # 210.119.12.110:외부포트