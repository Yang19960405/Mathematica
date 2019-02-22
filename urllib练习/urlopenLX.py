import socket
import urllib.request
import urllib.error

# urlopen()最基本的使用
response=urllib.request.urlopen('http://zckj.tjise.edu.cn/view/space_show/space_show')
print(response.read().decode('utf-8'))
print(type(response))

#urlopen()中data参数练习
# data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

#urlopen()中timeout参数说明  超过请求指定时间报异常
# try:
#     response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print("time out")