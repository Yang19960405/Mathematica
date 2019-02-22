from lxml import etree

#XPath提供强大的路径选择表达式
#XPath常用规则
#nodename           选取此节点的所有子节点
#/                  从当前节点选取直接子节点
#//                 从当前节点选取子孙节点
#..                 选取当前节点的父节点
#.                  选取当前节点
#@                  选取属性

text='''
<div>
<ul>
<li class="C001"><a href="link1.html">1</a></li>
<li class="C002"><a href="link2.html">2</a></li>
<li class="C003"><a href="link3.html">3</a></li>
<li class="C004"><a href="link4.html">4</a></li>
<li class="C005"><a href="link5.html">5</a></li>
</ul>
</div>
'''


#将TEXT格式转换成HTML格式
html=etree.HTML(text)
result=etree.tostring(html)
print(result.decode('utf-8'))

#将HTML文件解析
result=etree.parse('./etreeTest.html',etree.HTMLParser())
print(etree.tostring(etree.parse('./etreeTest.html',etree.HTMLParser())).decode('utf-8'))
print(result.xpath('//*'))
print(result.xpath('//li'))
#选择子节点
print(result.xpath('//li/a'))
#选择父节点
print(result.xpath('//a[@href="link2.html"]/../@class'))
#选择属性
print(result.xpath('//li[@class="C002"]'))
#获取属性
print(result.xpath('//li/@class'))
#text()获取节点文本
print(result.xpath('//li/a[@href="link3.html"]/text()'))

#属性多值匹配  contains()  第一个参数属性名  第二个参数属性值  只有有一个匹配就会成功
print(result.xpath('//li[contains(@class,"C001")]/a/text()'))

#多属性匹配  and

#按序选择
print(result.xpath('//li[last()]/a/text()'))
print(result.xpath('//li[position()<4]/a/text()'))
print(result.xpath('//li[2]/a/text()'))

#节点轴选择
#ancestor轴可以获取所有祖先元素  ::后面表示限制条件
#attribute轴可以获取所有属性
#descendant轴可以获取所有子孙节点
#following轴可以获取所有当前节点之后的所有子节点

print(result.xpath('//li[1]/ancestor::*'))




