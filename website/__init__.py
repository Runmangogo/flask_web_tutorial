from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjsdmifjgksm'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # 导入 views.py 里面 的 blueprint 实例
    from .views import views
    from .auth import auth

    # 注册 这个 blueprint， 并且 给它 url的前缀
    app.register_blueprint(views, url_prefix='/')

    # 如果 auth的 url_prefix 是 '/auth', 并且 auth.py 里面的 route 是 '/hello'
    # 则要到达 route 下面的函数，url 需要是： http://localhost/auth/hello
    app.register_blueprint(auth, url_prefix='/')

    # import models
    from .models import User, Note
    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')