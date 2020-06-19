# *-* coding: utf-8 -*

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

import app

def response(code=200, data=None, error=None, msg=None):
    '''
    :param code: 状态码
    :param data: 返回数据
    :param error: 错误信息
    :param msg: 提示信息
    '''

    if code is not None and code >= 400:
        error = HTTP_STATUS_CODES.get(code, "unknown error")

    pay_load = {
        "code": code, 
        "data": data, 
        "err": error,
        "message": msg or HTTP_STATUS_CODES.get(code, "unknown error")
    }

    # with ttt_app.app_context():
    _res = jsonify(pay_load)
    _res.status_code = code

    return _res

# if __name__ == '__main__':
    # ttt_app = app.create_app()
    # res = response(400)
    # print(res)
    # ttt_app.run()
    
