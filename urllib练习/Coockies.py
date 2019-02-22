import http.cookiejar,urllib.request
from urllib.parse import quote #编码解释
#声明一个CookieJar对象
cookie=http.cookiejar.CookieJar()

#利用HTTPCookieProcessor构造一个handler
handler=urllib.request.HTTPCookieProcessor(cookie)
#利用build_opener()构建Opener
opener=urllib.request.build_opener(handler)
#open()指定网址
response=opener.open('https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190103&stats_click=search_radio_all%3A1&js=1&imgfile=&q=1070%E6%98%BE%E5%8D%A1+8g&suggest=0_2&_input_charset=utf-8&wq=1070xianka&suggest_query=1070xianka&source=suggest')
#循环输出cookies的属性和值
for item in cookie:
    print(item.name+'='+item.value)



#将Cookies保存到TXT文本里面

filename='TaoBaoCookies.txt'
#声明一个MozillaCookieJar对象 他是CookieJar的子类  处理cookies和文件的相关操作
cookie2=http.cookiejar.MozillaCookieJar(filename)
#保存成LWP格式
cookie2=http.cookiejar.LWPCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie2)
opener=urllib.request.build_opener(handler)
response=opener.open('https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190103&stats_click=search_radio_all%3A1&js=1&imgfile=&q=1070%E6%98%BE%E5%8D%A1+8g&suggest=0_2&_input_charset=utf-8&wq=1070xianka&suggest_query=1070xianka&source=suggest')

cookie2.save(ignore_discard=True,ignore_expires=True)
#
#从文件中读取cookies

cookie=http.cookiejar.LWPCookieJar()
#使用load()方法读取本地cookies文件  获得其内容  这里使用的是LWP格式
cookie.load('TaoBaoCookies.txt',ignore_expires=True,ignore_discard=True)
handler=urllib.request.HTTPCookieProcessor(cookie);
opener=urllib.request.build_opener(handler)
response=opener.open('https://s.taobao.com/search?p='+quote('1070'))
print(response.read())
