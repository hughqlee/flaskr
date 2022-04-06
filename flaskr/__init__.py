import os

from flask import Flask, render_template # flask 프레임워크에서 Flask 클래스, render_template 함수를 불러온다 (쓰려고).
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/') # 라우트
    def index(): # 함수명
        return render_template('index.html') # index.html을 렌더링 한다 (불러와 화면에 깐다).

    db.init_app(app)

    return app