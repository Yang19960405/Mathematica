from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


browser=webdriver.Chrome()  #声明浏览器
try:
    browser.get('https://www.baidu.com')   #使用get访问页面
    input=browser.find_element_by_id('kw')   #使用find_element_by_id定位到输入框
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)   #延时加载
    wait.until(ec.presence_of_all_elements_located((By.ID,'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)
    browser.get('https://www.taobao.com')
finally:
    #browser.close()
    pass


#查找单个节点
input_1=browser.find_element_by_id('q')  #通过id查找
input_2=browser.find_element_by_css_selector('#q')  #通过css查找
input_3=browser.find_element_by_xpath('//*[@id="q"]')   #通过Xpath查找
input_4=browser.find_element(By.ID,'q')  #等价于browser.find_element_by_id('q')


#查找多个节点
lis=browser.find_elements(By.CSS_SELECTOR,'.service-bd li')

#节点交互
input_1.send_keys('1080ti')  #输入文字
time.sleep(1)
input_1.clear()               #清空文字
input_1.send_keys('1070ti')
button=browser.find_element_by_class_name('btn-search')  #获取搜索节点
button.click()                #单击按钮事件

#动作链  用户验证  滑动拼图会用到
from selenium.webdriver import ActionChains
browser=webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
sou=browser.find_element_by_css_selector('#draggable')
tar=browser.find_element_by_css_selector('#droppable')
actions=ActionChains(browser)
actions.drag_and_drop(sou,tar)
actions.perform()
browser.close()

# js代码注入 execute_script()
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #下拉进度条
browser.execute_script('alert("注入成功")')

#后退
browser.back()

time.sleep(1)
#前进
browser.forward()