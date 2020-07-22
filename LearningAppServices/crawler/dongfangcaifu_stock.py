# *-* coding: utf-8 *-

import requests
import re
from bs4 import BeautifulSoup
import traceback

def crawl():
    print('hello')
    stock_index_url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
    stock_info_base_url = 'https://gupiao.baidu.com/stock/'

    stock_code_list = get_stock_list(stock_index_url)
    if (stock_code_list is None) or len(stock_code_list) == 0:
        return
    
    stock_code = stock_code_list[0]
    stock_url = stock_info_base_url + stock_code + '.html'
    stock_info = get_stock_info(stock_url)

    # for stock_code in stock_code_list:
        # stock_url = stock_info_base_url + stock_code + '.html'
        # stock_info = get_stock_info(stock_url)



# 获取股票页面信息
def get_html_content_text(url, encode='utf-8'):
    try:
        res = requests.get(url)
        res.raise_for_status()
        res.encoding = encode
        return res.text
    except:
        return ''

# 获取股票列表
def get_stock_list(stock_index_url):
    index_html = get_html_content_text(stock_index_url, 'utf-8')
    soup = BeautifulSoup(index_html, 'html.parser')
    tag_a_list = soup.find_all('a')
    stock_list = []
    for tag_a in tag_a_list:
        try:
            href = tag_a.attrs['href']
            stock_list.append(re.findall(r'[s][hz]\d\{6\}', href)[0])
        except:
            continue

    return stock_list

# 获取股票的信息
def get_stock_info(stock_url):
    stock_html = get_html_content_text(stock_url)

    try:
        if stock_html == '':
            return None
        
        return {}
    except:
        return None

if __name__ == '__main__':
    crawl()