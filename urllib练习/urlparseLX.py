#使用urlparse()进行URL解析
from urllib.parse import urlparse, urlunparse, parse_qsl

result=urlparse('https://www.baidu.com/index.html;user?id=5#comment')
#返回类型包含六个部分
print(type(result),result)

#urlparse()组合成URL
date=['http','www.baidu.com','index.html','user','s=4','comment']
print(urlunparse(date))

#urlsplit()返回的远足类型  可以通过属性获得相应的值
#urlunsplit() 与urlsplit()对立
#urljoin()和urlunsplit()，urlparse()一样  不过他可以自动补全缺失的部分


#常用的urlencode()
#构造get请求时常常会用到
from urllib.parse import urlencode,parse_qs
#创建一个字典，并赋值
params={
    'name':'yangheng',
    'age':22
}
base_url='http://www.baidu.com?'
#用urlencode()将字典类型转换成URL参数
url=base_url+urlencode(params)
print(url)

#parse_qs()将参数转关成字典类型
query='name=yanggg&site=22'
paramss=parse_qs(query)
print(paramss)

#parse_qsl()将参数转关成元组类型
query='name=yanggg&site=22'
paramss=parse_qsl(query)
print(paramss)

#quote()可以将中文转换成URL编码
from urllib import parse
keywork="健健"
url='https://www.baidu.com/index?name='+parse.quote(keywork)
print(url)

#unquote()可以解码
print(parse.unquote(parse.quote(keywork)))