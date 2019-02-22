import re

#match()函数，
# 向他传入要匹配的字符串以及正则表达式，就可以检测这个正则表达式是否匹配字符串

str='ashdjh_12312 a0231 ajhf2  352'
result=re.match('(\w{12})\s\w\d{4}\s',str)
print(result)
#返回所有匹配值
print(result.group())
#返回指定括号序列内的值
print(result.group(1))
print(result.span())

#贪婪匹配 尽可能匹配多的字符
result2=re.match('.*(\d{4}).*352$',str)
print(result2.group(1))

#非贪婪匹配 尽可能匹配少的字符
result3=re.match('.*?(\d{4}).*352$',str)
print(result3.group(1))


#修饰符
#re.I   使匹配对大小写不敏感
#re.L   做本地化识别匹配
#re.M 多行匹配  影响^和$
#re.S  使.匹配包括换行符在内的所有字符
#re.U  根据Unicode字符集解析字符，这个标识影响\w\W\b\B
#re.X  更灵活的格式

