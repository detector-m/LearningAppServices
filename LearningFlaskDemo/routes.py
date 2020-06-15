# *-* coding: utf-8 *-

from flask import Flask, request, redirect, url_for
from werkzeug.routing import BaseConverter
import json

def add_route_root(app: Flask):
    @app.route('/')
    def root():
        return 'this is nothing.'

def add_route_login(app: Flask):
    # @app.route('/user/<int:user_id>')
    # def login(user_id):
    #     return f"user_id ={user_id}"

    # 自定义正则转换器
    class RegexConverter(BaseConverter):
        def __init__(self, url_map, *args):
            super(RegexConverter, self).__init__(url_map)
            # 将接受的第1个参数当作匹配规则进行保存
            self.regex = args[0]

    # 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: re
    app.url_map.converters['test'] = RegexConverter

    @app.route('/user/<test("[0-9]{3}"):user_id>')
    def login(user_id):
        return f"user_id ={user_id}"

def add_route_hello1(app: Flask):
    @app.route('/hello1')
    def hello1():
        json_dic = {
            'user_id': 10,
            'user_name': 'riven'
        }
        return json.dumps(json_dic)

def add_route_hello2(app: Flask):
    @app.route('/hello2')
    def hello2():
        json_dic = {
            'user_id': 10,
            'user_name': 'riven'
        }
        return json.loads(json.dumps(json_dic))

def add_route_redirect(app):
    @app.route('/redirect')
    def redirect_test():
        return redirect(url_for('test_request_method'))

def add_route_test_request_method(app):
    @app.route('/test', methods=['GET', 'POST'])
    def test_request_method():
        return request.method



