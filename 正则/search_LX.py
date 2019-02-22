import re
import requests
#search()  他会扫描整个字符串 然后返回第一个成功匹配的结果


#过滤天软首页
request=requests.get('https://www.tjise.edu.cn/')
request.encoding='utf-8'
print(request.text)