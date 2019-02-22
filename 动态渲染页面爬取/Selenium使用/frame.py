import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser=webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException as nee:
    print('错误',nee)
browser.switch_to.parent_frame()
logo=browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)