from pyquery import PyQuery as pq
import requests
import re

def get_maoyantop_page():
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    result=requests.get('http://maoyan.com/board/4',headers=headers)
    result.encoding='utf-8'
    if result.status_code==200:
        return result.text
    return None

doc=pq(get_maoyantop_page())
print(doc('li'))