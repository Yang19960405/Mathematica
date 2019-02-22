from selenium import webdriver
from selenium.webdriver import ActionChains

#获取节点信息

browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

#获取属性get_attribute()
logo=browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('data-za-a'))

#获取文本值
print(logo.text)

#获取id
print(logo.id)

#获取节点在页面中的相对位置
print(logo.location)

#获取标签名
print(logo.tag_name)

#获取节点大小
print(logo.size)