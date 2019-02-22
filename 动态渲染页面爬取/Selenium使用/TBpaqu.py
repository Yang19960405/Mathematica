from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote #编码解释
import time
import pyquery


def index_page(page):
    if page>=1:
        input=browser.find_element(By.CSS_SELECTOR,'#mainsrp-pager .form .input')
        input.clear()
        input.send_keys(page)
        btn=browser.find_element(By.CSS_SELECTOR,'#mainsrp-pager .form .btn')
        btn.click()

        time.sleep(3)

        html = browser.page_source
        doc = pyquery.PyQuery(html)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .m-itemlist .items .item')))
        items = doc('#mainsrp-itemlist .m-itemlist .items .item').items()
        for item in items:
            prodout = {
                '商品名称': item.find('.pic .img').attr('alt'),
                '价格': pyquery.PyQuery(item.find('.price')).text()[1:],
                '商品图片': item.find('.pic .img').attr('data-src'),
                '销量': item.find('.deal-cnt').text(),
                '店铺': item.find('.shop').text(),
                '地址': item.find('.location').text()
            }
            print(prodout)


browser=webdriver.Chrome()
wait=WebDriverWait(browser,2)
Key=input('输入搜索关键词')
url='https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190103&stats_click=search_radio_all%3A1&js=1&imgfile=&q='+quote(Key)+'&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest'
browser.get(url=url)

cookies=[
{'domain': '.taobao.com', 'httpOnly': False, 'name': '_tb_token_', 'path': '/', 'secure': False, 'value': 'e33b34e333073'},
{'domain': '.taobao.com', 'expiry': 1554271681.084378, 'httpOnly': False, 'name': 't', 'path': '/', 'secure': False, 'value': '62546ebe875c57411030383ad4ef2187'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'sg', 'path': '/', 'secure': False, 'value': '%E5%AD%9891'},
{'domain': '.taobao.com', 'expiry': 2177215668, 'httpOnly': False, 'name': 'cna', 'path': '/', 'secure': False, 'value': 'tJS0FAZ/rnUCAX0kdiUHrcx8'},
{'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie2', 'path': '/', 'secure': False, 'value': '170fc20d5e9d07690f0378b75c0628e2'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': '_l_g_', 'path': '/', 'secure': False, 'value': 'Ug%3D%3D'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'v', 'path': '/', 'secure': False, 'value': '0'},
{'domain': '.taobao.com', 'httpOnly': True, 'name': 'unb', 'path': '/', 'secure': False, 'value': '2572640809'},
{'domain': '.taobao.com', 'httpOnly': True, 'name': 'skt', 'path': '/', 'secure': False, 'value': '9412645922ad46d5'},
{'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie1', 'path': '/', 'secure': False, 'value': 'B0b4fA%2FRn7cgp4sOJkvGMPIGr%2BsNiwJBk91CrKeypKw%3D'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'csg', 'path': '/', 'secure': False, 'value': '1e8439d1'},
{'domain': '.taobao.com', 'expiry': 1549087681.084748, 'httpOnly': True, 'name': 'uc3', 'path': '/', 'secure': False, 'value': 'vt3=F8dByRIsSE1WENFyFPc%3D&id2=UU21bWqP8ryeAQ%3D%3D&nk2=0OWOFoiSIHo%3D&lg2=VT5L2FSpMGV7TQ%3D%3D'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'existShop', 'path': '/', 'secure': False, 'value': 'MTU0NjQ5NTY4MA%3D%3D'},
{'domain': '.taobao.com', 'expiry': 1578031681.084847, 'httpOnly': False, 'name': 'tracknick', 'path': '/', 'secure': False, 'value': '%5Cu75F4%5Cu68A6%5Cu72B9%5Cu5B58'},
{'domain': '.taobao.com', 'expiry': 1549087681.084891, 'httpOnly': False, 'name': 'lgc', 'path': '/', 'secure': False, 'value': '%5Cu75F4%5Cu68A6%5Cu72B9%5Cu5B58'},
{'domain': '.taobao.com', 'expiry': 1578031681.084936, 'httpOnly': False, 'name': '_cc_', 'path': '/', 'secure': False, 'value': 'U%2BGCWk%2F7og%3D%3D'},
{'domain': '.taobao.com', 'expiry': 1547100483.533958, 'httpOnly': False, 'name': 'mt', 'path': '/', 'secure': False, 'value': 'ci=54_1'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'dnk', 'path': '/', 'secure': False, 'value': '%5Cu75F4%5Cu68A6%5Cu72B9%5Cu5B58'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': '_nk_', 'path': '/', 'secure': False, 'value': '%5Cu75F4%5Cu68A6%5Cu72B9%5Cu5B58'},
{'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookie17', 'path': '/', 'secure': False, 'value': 'UU21bWqP8ryeAQ%3D%3D'},
{'domain': '.taobao.com', 'expiry': 1600495681.085098, 'httpOnly': False, 'name': 'tg', 'path': '/', 'secure': False, 'value': '0'},
{'domain': '.taobao.com', 'expiry': 1861855681.370006, 'httpOnly': True, 'name': 'enc', 'path': '/', 'secure': True, 'value': 'vfnj%2F228j11zBS82Oyant02kWP6nBG8fcIcVVUSef8ZlFz8VyA7EBaZW4hQLO0aN5BhlalLUe4ViUEaA5lUrjg%3D%3D'},
{'domain': 's.taobao.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'CD92DF78DD870A7E147F28D94EEFD952'},
{'domain': '.taobao.com', 'expiry': 1578031683.410882, 'httpOnly': False, 'name': 'hng', 'path': '/', 'secure': False, 'value': 'CN%7Czh-CN%7CCNY%7C156'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'uc1', 'path': '/', 'secure': False, 'value': 'cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTYMD9TX9vvOA%3D%3D&tag=8&lng=zh_CN'},
{'domain': '.taobao.com', 'expiry': 1577599684, 'httpOnly': False, 'name': 'thw', 'path': '/', 'secure': False, 'value': 'cn'},
{'domain': '.taobao.com', 'expiry': 1578031688, 'httpOnly': False, 'name': 'x', 'path': '/', 'secure': False, 'value': 'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0'},
{'domain': 's.taobao.com', 'httpOnly': False, 'name': 'swfstore', 'path': '/', 'secure': False, 'value': '113776'},
{'domain': '.taobao.com', 'httpOnly': False, 'name': 'whl', 'path': '/', 'secure': False, 'value': '-1%260%260%260'},
{'domain': '.taobao.com', 'expiry': 1562047684, 'httpOnly': False, 'name': 'l', 'path': '/', 'secure': False, 'value': 'aBf0YMCGyuzr32QBoMa52XwrU707snfPAPfK1MaLNTEhNOYG7RXy1j-o-Vw6K_qC5vFy_Kn5F'},
{'domain': '.taobao.com', 'expiry': 1562047683, 'httpOnly': False, 'name': 'isg', 'path': '/', 'secure': False, 'value': 'BBgYtedW8NYondxSpE2NWLZm6UZqqXe41oC1mFIJZdMG7bjX-hAhGZsPIWT4fTRj'}
]

for cookie in cookies:
    browser.add_cookie(cookie)
browser.get(url=url)

index_page(4)

#browser.get(url=url)
# time.sleep(30)
# for ck in browser.get_cookies():#获取cookies
#     print(ck)
