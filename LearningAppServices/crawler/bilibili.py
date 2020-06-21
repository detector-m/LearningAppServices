# *-* coding: utf-8 -*

import re 
import requests

def crawl(url: str) -> dict:
    '''
    imgs, videos
    '''

    data = {}
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Referer': 'https://www.bilibili.com'
    }

    av_number_pattern = r'(BV[0-9a-zA-Z]*)'
    cover_pattern = r"image:'(.*?)',"
    video_pattern = r'"base_url":"(.*?)"'
    title_pattern = r"title\":\"(.*?)\","

    av = re.findall(av_number_pattern, url)
    if av:
        av = av[0]
    else:
        data['msg'] = '链接可能不正确，因为我无法匹配到BV号'
        return data

    url = f'https://www.bilibili.com/video/{av}'

    with requests.get(url, headers=headers, timeout=10) as res:
        if res.status_code == 200:
            cover_url = re.findall(cover_pattern, res.text)
            if cover_url:
                data['cover_url'] = cover_url[0]
            
            video_url = re.findall(video_pattern, res.text)
            title = re.findall(title_pattern, res.text)
            if video_url:
                video_url = video_url[0]
                data['videos'] = video_url
            if title:
                data['title'] = title[0]
        else:
            data['msg'] = '获取失败'

        return data


if __name__ == '__main__':
    print(crawl(input('url:')))