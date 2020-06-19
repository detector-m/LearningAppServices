# *-* coding: utf-8 -*

import os, logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.logging import default_handler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, 'log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_PATH = os.path.join(LOG_DIR, 'log.log')

LOG_FILE_MAX_BYTES = 10 * 1024 *1024
LOG_FILE_BACKUP_COUNT = 10

def init_log(app: Flask):
    app.logger.removeHandler(default_handler)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s] %(message)s')

    file_handler = RotatingFileHandler(
        filename=LOG_PATH,
        mode='a',
        maxBytes=LOG_FILE_MAX_BYTES,
        backupCount=LOG_FILE_BACKUP_COUNT,
        encoding='utf-8'
    )

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.WARNING)

    for logger in (app.logger, logging.getLogger('werkzeug')):
        logger.addHandler(file_handler)

    # for test
    # logging.getLogger('werkzeug').error('eeee')

# if __name__ == '__main__':
#     pass