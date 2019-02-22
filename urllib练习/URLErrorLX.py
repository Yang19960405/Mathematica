from urllib.error import URLError,HTTPError
from urllib import request
try:
    response=request.urlopen('https://cuiqingcai.com/indxe.htm')
except HTTPError as e:
    #code:返回HTTP状态码
    #reason:返回错误原因
    #headers:返回请求头
    print(e.reason,e.code,e.headers,sep='\n')



#更好的异常捕获
try:
    response=request.urlopen('https://asdsadsadw.com/index.htm')
except HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except URLError as e:
    print(e.reason)
else:
    print('未知异常')
