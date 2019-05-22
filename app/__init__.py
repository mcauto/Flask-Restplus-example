import os
from flask import Flask

from logging.config import dictConfig
from app.repository.database import db
from app.config import config_by_name
import logging

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    if 'TRAVIS_CI' not in os.environ:
        # https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
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
                    'filename': app.config['LOG_PATH'] + '/app.log',
                    'formatter': 'default',
                },
                'console':{
                    'class':'logging.StreamHandler',
                    'formatter':'default',
                    'stream':'ext://sys.stdout',
                },
            },
            'root': {
                'level': 'INFO',
                'handlers': ['file_handler', 'console']
            }
        })
    app.logger.info('>>> {}'.format(config_name))
    return app
