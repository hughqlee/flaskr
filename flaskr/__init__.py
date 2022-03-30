from flask import Flask, render_template # flask 프레임워크에서 Flask 클래스, render_template 함수를 불러온다 (쓰려고).

app = Flask(__name__) # 플라스크 앱을 만든다.

@app.route('/') # 라우트
def index(): # 함수명
    return render_template('index.html') # index.html을 렌더링 한다 (불러와 화면에 깐다).