import re

from urllib import parse
from flask import current_app

from _response import response

from crawler import (bilibili)

# URL_PATTERN = r"https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]\.[-A-Za-z]+[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"
URL_PATTERN = r'^https?:/{2}\w.+$'

def extract(url: str):
    url = re.findall(URL_PATTERN, url)
    if not url:
        return response(404, msg='无法匹配到链接')

    url = url[0]

    if 'bilibili.com' in parse.urlparse(url).hostname:
        f = bilibili
    else:
        return response(code=400, msg="不支持的链接")
    
    try:
        data = f.crawl(url)
        msg = data.get('msg', None)
        return response(data=data, msg=msg)
    except Exception as e:
        current_app.logger.error(e)
        current_app.logger.exception(e)
        return response(500, error=e, msg='服务器错误')
    
    return response(msg=f'{url}')