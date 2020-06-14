from flask import Flask
from multiprocessing import Process
import time

# import os
# pwd = os.getcwd()

# 配置全局app
app = Flask(__name__)
# 直接设置
# app.debug = True
# app.env = 'development'
# 以字典的形式
# app.config['DEBUG'] = True
# app.config['ENV'] = 'development'
# 从对象中加载配置
# from config import Config
# app.config.from_object(Config)
# 从文件中加载配置
app.config.from_pyfile('config.ini')

'''
设置返回的错误信息，异常处理
'''
@app.errorhandler(500)
def internal_server_error(e):
    return '服务器错误'

'''
请求钩子是通过装饰器的形式实现，Flask支持四种请求钩子；
before_first_request: 在处理第一个请求前执行
before_request: 在每次请求前执行，如果在某修饰的函数中返回了响应，视图函数将不再调用
after_request: 如果没有抛出异常， 在每次请求后执行
teardown_request: 在每次请求后执行，接受一个参数：错误信息，如果有则抛出相关错误
'''

# 可以带动一个异步执行的函数，进行一些健康指标的检查，如果发现有异常，则截断后续的请求，将整个Flask应用停止。
@app.before_first_request
def before_first_request():
    print('before_first_request')

# 共享session的鉴权函数、请求黑白名单过滤、根据endpoint进行请求j等
@app.before_request
def before_request():
    print('before_request')

# 一般用于格式化响应结果，包括响应请求头，响应的格式等。
@app.after_request
def after_request(response):
    print('after_request')
    response.headers['Content-Type'] = 'application/json'
    return response
    
# 销毁DB连接等
@app.teardown_request
def teardown_request(e):
    print('teardown_request')

def run_server():
    import routes
    routes.add_route_root(app)
    routes.add_route_login(app)
    routes.add_route_hello1(app)
    routes.add_route_hello2(app)
    routes.add_route_test_request_method(app)
    routes.add_route_redirect(app)
    # 启动服务器
    # app.run(host='0.0.0.0', port=5000, threaded=True)
    app.run(host='0.0.0.0', port=5000)


def run_orders():
    while True:
        print('执行相应的交易程序')
        time.sleep(3)

def multiprocessing_main():
    # 主程序
    # 创建子进程
    jobs = []
    jobs.append(Process(target=run_server))
    jobs.append(Process(target=run_orders))

    # 启动子进程
    for job in jobs:
        job.start()
    
    # 等待子进程结束
    for job in jobs:
        job.join()

def main():
    run_server()

if __name__ == '__main__':
    main()