from pyquery import PyQuery as pq
import re
import requests

def get_maoyantop_page():
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML,like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }
    result=requests.get('http://www.zhihu.com/explore',headers=headers)
    result.encoding='utf-8'
    if result.status_code==200:
        return result.text
    return None

print(get_maoyantop_page())

doc=pq(get_maoyantop_page())
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item.find('h2').text()
    author=item.find('.author-link-line').text()
    answer=pq(item.find('.content').html()).text()
    print(answer)
    with open('explore.txt','a',encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')
