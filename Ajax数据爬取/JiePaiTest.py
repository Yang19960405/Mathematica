import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

#获取ajax路径
def _GetUrl(page):
    part_url="https://www.toutiao.com/search_content/?"

    params={
        'offset':page*20,
        'format':'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }

    return part_url+urlencode(params)

#获取请求头
def _GetHeaders():
    return{
        'Host':'www.toutiao.com',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

#获取请求数据
def GetJiePai(page):
    try:
        response=requests.get(url=_GetUrl(page),headers=_GetHeaders())
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('异常',e.args)

#过滤数据
def data_screen(json):
    print(json)
    if json.get('data'):
        for items in json.get('data'):
            title=items.get('title')
            if items.get('image_list'):
                for item in items.get('image_list'):
                    if item!=None:
                        yield {
                            'image':'http:'+item.get('url'),
                            'title':title
                        }

import os
from hashlib import md5

#保存数据
def save_images(image):
    if not os.path.exists(image.get('title')):
        os.mkdir(image.get('title'))
    try:
        response=requests.get(image.get('image'))
        if response.status_code==200:
            image_name=str(md5(response.content).hexdigest)
            file_path='{0}/{1}.{2}'.format(image.get('title'),image_name[1:-1],'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print(file_path)
    except requests.ConnectionError:
        print("Failed to Save Image")

from multiprocessing.pool import Pool

def main (offset):
    json=GetJiePai(offset)
    for item in data_screen(json):
        print(item)
        save_images(item)

if __name__ == '__main__':
    pool=Pool()
    groups=([x for x in range(1,8)])
    pool.map(main,groups)
    pool.close()
    pool.join()