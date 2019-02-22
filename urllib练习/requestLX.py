import socket
import urllib.request
import urllib.error

#request()基本使用
# request=urllib.request.Request("https://www.python.org")
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))


#request()参数使用
# from urllib import parse
# from urllib import request
# url="http://httpbin.org/post"
# headers={
#     'user-Agent':'mozilla/4.0 (compatible;MSIE 5.5; Windows NT)',
#     'Host':'httpbin.org'
# }
# dict={
#     'name':'yanghhhh'
# }
# data=bytes(parse.urlencode(dict),encoding='utf-8')
# req=request.Request(url=url,data=data,headers=headers,method='POST')
# response=urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))



#request()打开带用户验证的页面
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username='18222043061'
userpass='z1981975143'
url='http://zckj.tjise.edu.cn/view/index/index'

p=HTTPPasswordMgrWithDefaultRealm()
#利用add_password()方法添加用户名密码
p.add_password(None,url,username,userpass)
#实例化HTTPBasicAuthHandler对象  参数类型HTTPPasswordMgrWithDefaultRealm
auth_handler=HTTPBasicAuthHandler(p)
#利用build_opener()和handler构建出一个opener  这样发送的请求就是已经验证过得请求
opener=build_opener(auth_handler)

try:
    result=opener.open(url)
    html=result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)