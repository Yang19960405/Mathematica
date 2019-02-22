import requests
url='http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2743.116 Safari/537.36'
}
data={
    'name':'yangheng',
    'age':'22',
}
#会话维持
s=requests.Session()
#构造Request对象
req=requests.Request('POST',url=url,data=data,headers=headers)
#调用session的prepare_request方法转换成Prepared Ruquest对象
prepped=s.prepare_request(req)
#send()页面请求
print(s.send(prepped).text)
