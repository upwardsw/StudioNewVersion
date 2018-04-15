# app's config include test and run

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or '~N`e1w!2@3M#e$d4%i56a&^P&*y86t8780h(0o7n*&())_+'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    # FLASKY_MAIL_SENDER = 'FLASKY ADMIN <flasky@example.com>'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # DEBUG = True
    # MAIL_SERVER = 'smtp.google.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://danchun:shi1912504224@47.95.253.230/my_studio?charset=utf8'
    # SQLALCHEMY_DATABASE_ENCODING = 'UTF-8'
    # SQLALCHEMY_DATABASE_ECHO = True
    # APP_DEBUG = True
    # APP_HOST = '0.0.0.0'
    # APP_PORT = 100
    pass


config = {
    'development': DevelopmentConfig
}
