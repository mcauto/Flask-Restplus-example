"""
Global Flask Application Setting

set FLASK_CONFIG to 'development
 """

import os

class Config:
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)

    HOST = '0.0.0.0'
    PORT = '5000'
    DEBUG = True

    LOG_PATH = os.path.abspath(APP_DIR)+"/log"

    MYSQL_DATABASE_USERNAME='user'
    MYSQL_DATABASE_PASSWORD='userpassword'
    MYSQL_DATABASE_NAME='database'
    MYSQL_DATABASE_HOST='localhost'
    MYSQL_PORT=os.getenv('MYSQL_PORT','33306')

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.format(DB_USER=MYSQL_DATABASE_USERNAME,
                                                             DB_PASS=MYSQL_DATABASE_PASSWORD,
                                                             DB_ADDR=MYSQL_DATABASE_HOST,
                                                             DB_PORT=MYSQL_PORT,
                                                             DB_NAME=MYSQL_DATABASE_NAME)
