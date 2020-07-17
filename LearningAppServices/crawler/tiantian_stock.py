# *-* coding: utf-8 -*
# 参考 https://github.com/shengqiangzhang/examples-of-web-crawlers

import requests
import random
import re 
import queue
import threading
import json

# user_agent列表
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]

# referer 列表
referer_list = [
    'http://fund.eastmoney.com/110022.html',
    'http://fund.eastmoney.com/110023.html',
    'http://fund.eastmoney.com/110024.html',
    'http://fund.eastmoney.com/110025.html'
]

# 返回一个可用代理，格式为ip:端口
# 该接口直接调用github代理池项目给的例子，故不保证该接口实时可用
# 建议自己搭建一个本地代理池，这样获取代理的速度更快
# 代理池搭建github地址https://github.com/1again/ProxyPool
# 搭建完毕后，把下方的proxy.1again.cc改成你的your_server_ip，本地搭建的话可以写成127.0.0.1或者localhost
def get_proxy():
    data_json = requests.get('http://proxy.1again.cc:35050/api/v1/proxy/?type=1').text
    data = json.loads(data_json)
    return data['data']['proxy']

# 获取基金代码
def get_fund_code():
    # 获取一个随机user_agent和Referer
    header = {
        'User-Agent': random.choice(user_agent_list),
        'Referer': random.choice(referer_list)
    }

    # 访问网页接口
    req = requests.get('http://fund.eastmoney.com/js/fundcode_search.js', timeout=4, headers=header)

    # 获取所有基金代码
    fund_code = req.content.decode(encoding='utf-8-sig')
    fund_code = fund_code.replace('var r = [', '').replace('];', '')

    # 正则批量提取
    fund_code = re.findall(r"[\[](.*?)[\]]", fund_code)

    # 对每行数据进行处理
    fund_code_list = []
    for fund_code_line in fund_code:
        fund_code_info = fund_code_line.replace('\"', '').replace('\'', '')
        line_list = fund_code_info.split(',')
        fund_code_list.append(line_list)

    return fund_code_list

# 获取基金数据
def get_fund_data():
    # 当队列不为空时
    while not fund_code_list_queue.empty():
        # 读取时阻塞操作
        fund_code = fund_code_list_queue.get()
        fund_data = get_fund_data_with_code(fund_code)
        

# 根据基金code获取基金信息
def get_fund_data_with_code(fund_code):
    # 获取一个代理
    proxy = get_proxy()

    # 获取一个随机的
    header = {
        'User-Agent': random.choice(user_agent_list),
        'Referer': random.choice(referer_list)
    }

    try:
        # 使用代理访问
        url = 'http://fund.eastmoney.com/pingzhongdata/'+ str(fund_code) + '.js'
        # req = requests.get(url, proxies={"http": proxy}, timeout=3, headers=header)
        req = requests.get(url, timeout=3, headers=header)


        # 获取返回数据
        data = req.content.decode(encoding='utf-8-sig')
        print(data)
        return data
    except Exception:
        fund_code_list_queue.put(fund_code)
        print("访问失败，尝试使用其他代理访问")
        return None


if __name__ == '__main__':
    print('天天基金')
    # print(get_proxy())
    fund_code_list = get_fund_code()

    # 将所有基金代码放入先进先出FIFO队列中
    # 队列的写入和读取都是阻塞的，故在多线程情况下不会乱
    # 在不使用框架的前提下，引入多线程，提高爬取效率
    # 创建一个队列
    fund_code_list_queue = queue.Queue(len(fund_code_list))
    for index in range(len(fund_code_list)):
        fund_code_list_queue.put(fund_code_list[index][0])

    # test
    fund_data = get_fund_data_with_code(fund_code_list_queue.get())

    # # 创建一个线程锁，防止多线程写入文件时发生错乱
    # mutex_lock = threading.Lock()
    # # 线程数为50， 在一定范围内，线程越多，速度越快
    # for i in range(50):
    #     t = threading.Thread(target=get_fund_data, name='FundCodeThread'+str(i))
    #     t.start()

    