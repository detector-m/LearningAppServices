import re

from flask import current_app

from _response import response

# URL_PATTERN = r"https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]\.[-A-Za-z]+[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"
URL_PATTERN = r'^https?:/{2}\w.+$'

def extract(url: str):
    url = re.findall(URL_PATTERN, url)
    if not url:
        return response(404, msg='无法匹配到链接')
    
    return response(msg=f'{url}')