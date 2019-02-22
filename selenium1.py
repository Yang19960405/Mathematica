#未使用PhantomJS  会打开对应浏览器
# from selenium import webdriver
# from selenium.webdriver.common.by import  By
#
# browser=webdriver.Chrome()
#
# browser.get("http://www.baidu.com")
# input_first=browser.find_element(By.ID,"q")
# print(input_first)

# 使用PhantomJS  不会打开对应浏览器网站 但会在后台运行
# from selenium import webdriver
# browser=webdriver.PhantomJS()
# browser.get("http://www.baidu.com")
# print(browser.current_url)

# from bs4 import BeautifulSoup
# soup=BeautifulSoup('<p>HHHHHH</p>','lxml')
# print(soup.p.string)
import urllib.request
response=urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))