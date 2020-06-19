# *-* coding: utf-8 -*

import os

class Config():
    ENV = os.getenv('ENV') or 'development'
    DEBUG = os.getenv('DEBUG') or True
    SECRET_KEY = os.getenv('SECRET_KEY') or 'LearningAppServices'

    # 在浏览器请求接口正常显示中文，而不是字节码
    JSON_AS_ASCII = False