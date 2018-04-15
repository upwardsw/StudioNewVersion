from flask import Flask
from flask_cors import *
from flask_login import LoginManager
from sqlalchemy import *
from sqlalchemy.orm import *


def create_app():
    app=Flask(__name__)
    app.config.secret_key='~N`e1w!2@3M#e$d4%i56a&^P&*y86t8780h(0o7n*&())_+'
    CORS(app, supports_credentials=True)

    # database setting
    engine = create_engine('mysql+pymysql://danchun:shi1912504224@47.95.253.230/my_studio?charset=utf8', encoding="utf-8", echo=True)
    DBSession = sessionmaker(bind=engine)

    # login模块设置：
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.session_protection = "strong"
    login_manager.login_message = "Please login to access this page."
    login_manager.login_message_category = "info"

    # reload login-user
    @login_manager.user_loader
    def load_user(user_id):
        pass


    # import blueprint auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # import blueprint main
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # import blueprint public
    from .public import public as public_blueprint
    app.register_blueprint(public_blueprint)

    return app


