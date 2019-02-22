import requests

#不维护会话session
#请求网址设置cookies
requests.get('http://httpbin.org/cookies/set/number/123456')
#请求网址获取cookies
r=requests.get('http://httpbin.org/cookies')
print(r.text)


#维护会话session

s=requests.session()
s.get('http://httpbin.org/cookies/set/number/123456')
print(s.get('http://httpbin.org/cookies').text)