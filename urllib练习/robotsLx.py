#robots.txt规定了哪些可以爬哪些不可以爬
#User-agent规定了对哪些爬虫有效
#Disallow指定了不允许抓取的目录
#Allow通常和Disallow一起使用，用来排除某些限制


#禁止所有爬虫访问
#User-agent:*
#Disallow:/

#允许所有爬虫访问
#User-agent:*
#Disallow:

#禁止爬虫访问某一目录下的代码
#User-agent:*
#Disallow:/mmp/

#只允许某一爬虫访问代码
#User-agent:WebCrawler
#Disallow:


#使用robotparser()来解析robots.txt
#mtime() 返回抓取和分析robots.txt的时间


from urllib import robotparser,request
#创建RobotFileParser()对象
rp=robotparser.RobotFileParser('http://www.jianshu.com/robots.txt')
# print(rp.parse(request.urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n')))
#使用set_url设置robots.txt链接
#rp.set_url('http://www.jianshu.com/robots.txt')
#使用read()读取robots.txt文件
rp.read()

#使用can_fetch()判断是否可以抓取这个URL  第一个参数是User-agent  第二个是URL
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.mtime())
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&qage=1&type=collections'))



