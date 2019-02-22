import requests
r=requests.get("https://www.baidu.com")
print(r.text)
print(r.cookies)
for key, value in r.cookies.items():
    print(key+"="+value)

headers={
    'Cookie': '_zap=c35b3c98-c121-40f0-ae9f-f6a35b63dd33; d_c0="AADo-HJzbw6PTm7fwwSVuC_y0dduf3Ep5QI=|1540777516";'
             ' q_c1=5161328a06d24ec1b326be9f4898cdce|1540777518000|1540777518000; _xsrf=LpHgdoWsABgmawLg0TXCTnB5CNQRF1l4; '
             'capsion_ticket="2|1:0|10:1542029397|14:capsion_ticket|44:ZGEwY2E4MDc1NjRlNDQwZDlkYTc0NjY4NTYyMTJjNzA=|ba5844602d5f29cbc25df4f135a88ab4e739daf3fcc3f44cdd59bd1209bcb3ef"; '
             'z_c0="2|1:0|10:1542029425|4:z_c0|92:Mi4xRVQ4VkJnQUFBQUFBQU9qNGNuTnZEaVlBQUFCZ0FsVk5jYzdXWEFCclJVdUFYNS1tcXFuelFVVXRiaHZSQXpJSEhR|53d7383c52065638901f6b1a48ff3fb0777e731f5761a2c1770d40778badf01f";'
             ' __gads=ID=8b2ee9fc4815ec61:T=1542029633:S=ALNI_MafwCgu2NyN7lLGiZ4TELX188hu0A; tst=r; __utma=51854390.1949033655.1542029874.1542029874.1542029874.1;'
             ' __utmz=51854390.1542029874.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/;'
             ' __utmv=51854390.100--|2=registration_date=20171001=1^3=entry_date=20171001=1; '
             'tgw_l7_route=29b95235203ffc15742abb84032d7e75',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2743.116 Safari/537.36',
}

r=requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
print(r.cookies)
