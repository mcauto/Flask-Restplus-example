import os
from flask import Flask, current_app, send_file
from app.api import api_blueprint

from logging.config import dictConfig
from app.config import Config
import logging

def create_app(config_filename):
    if 'TRAVIS_CI' not in os.environ:
        dictConfig({
            'version':1,
            'formatters': {
                'default': {
                    'format': '%(asctime)s] [%(levelname)s] [%(module)s:%(lineno)d]\n %(message)s',
                },
            },
            'handlers': {
                'file_handler': {
                    'class': 'logging.FileHandler',
                    'filename': Config.LOG_PATH + '/app.log',
                    'formatter': 'default',
                },
            },
            'root': {
                'level': 'INFO',
                'handlers': ['file_handler']
            }
        })
    
    app = Flask(__name__)
    app.config.from_object(config_filename)
    #db.init_app(app)
    app.register_blueprint(api_blueprint)
    app.logger.info('>>> {}'.format(Config.FLASK_ENV))
    return app


