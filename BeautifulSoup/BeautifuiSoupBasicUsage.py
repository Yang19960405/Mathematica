import requests
import re
from bs4 import BeautifulSoup


def get_maoyantop_page():
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    result=requests.get('http://maoyan.com/board/4',headers=headers)
    result.encoding='utf-8'
    if result.status_code==200:
        return result.text
    return None

soup=BeautifulSoup(get_maoyantop_page(),'lxml')
#prettify()以标准的缩进格式输出
#print(soup.prettify())
#print(soup.title.string)

#find_all() 查询所有符合条件的元素
# print(soup.find_all(name='li'))
# #find_all() 查询符合下标条件的元素
# print(soup.find_all(name='li')[2])
#find()  查询符合条件的第一个元素

#嵌套查询
# for a in soup.find_all(name='li'):
#     print(a.find_all(name='a'))
#     for b in a.find_all(name='a'):
#         print(b.string)

#attrs 根据属性查询
# for a in soup.find_all(name='li'):
#     for b in a.find_all(attrs={"data-act":"subnav-click"}):
#         print(b.string)


#css选择器
for a in soup.select('ul li'):
    for b in a.find_all(attrs={"data-act": "subnav-click"}):
        print(a.get_text())

for a in soup.select('ul'):
    print(a['class'])

