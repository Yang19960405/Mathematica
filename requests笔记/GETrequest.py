import requests

#get和urlopen()完成的是相同的工作
# rq=requests.get('https://www.baidu.com')
# print(type(rq))
# print(rq.status_code)
# print(type(rq.text))
# print(rq.text)
# print(rq.cookies)

#分别使用post(),put(),delete()等方法实现POST,PUT,DELETE等请求



#抓取网页
import re
#加入headers  其中包括User-Agent字段信息，否则知乎会禁止抓取
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get("https://www.zhihu.com/explore",headers=headers)
#使用正则匹配问题
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(pattern,r.text)
print(titles)


#抓取二进制数据
rq=requests.get('https://github.com/favicon.ico')
#以文本形式输出
print(rq.text)
#以二进制形式输出
print(rq.content)
#将图片保存下来
with open('favicon.ico','wb') as f:
    f.write(rq.content)
