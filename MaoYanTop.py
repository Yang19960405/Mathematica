import requests
import re
import json
#抓取url页面



def get_maoyantop_page(url):
    headers={
        'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    request=requests.get(url,headers=headers)
    request.encoding='utf-8'
    if request.status_code==200:
        return request.text

    return None;

#正则过滤页面
def parse_maoyan_page(html):
    pattern= re.compile(
        '<dd>.*?board-index.*?>(.*?)'
        '</i>.*?data-src="(.*?)"'
        '.*?name.*?a.*?>(.*?)'
        '</a>.*?star.*?>(.*?)'
        '</p>.*?releasetime.*?>(.*?)'
        '</p>.*?integer.*?>(.*?)'
        '</i>.*?fraction.*?>(.*?)'
        '</i>.*?</dd>',
        re.S)
    items= re.findall(pattern,html)

    for item in items:
        #yield  简单介绍：yield常见用法：该关键字用于函数中会把函数包装为generator。然后可以对该generator进行迭代: for x in fun(param).
        # 在一个函数中，程序执行到yield语句的时候，程序暂停，返回yield后面表达式的值，在下一次调用的时候，
        # 从yield语句暂停的地方继续执行，如此循环，直到函数执行完。
        yield {
            '排名':item[0],
            '评分':item[5].strip()+item[6].strip(),
            'image':item[1],
            '片名':item[2].strip(),
            '主演':item[3].strip()[3:] if len(item[3])>3 else '',
            '上映时间':item[4].strip()[5:] if len(item[4])>5 else '',
        }

#将数据存入文件中
def write_to_file(content):
    with open('maoyanTop.txt','a',encoding='utf-8') as f:

        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html= get_maoyantop_page(url)
    for item in parse_maoyan_page(html):
        write_to_file(item)

    pass

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
