import json
str='''
[{
"name":"yangheng",
"age":"22"
},{
"name":"hansiyuan",
"age":"21"
}]
'''

print(str)
print(type(str))

data=json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('age'))

#读取json
# with open('data.json','r',encoding='utf-8') as file:
#     str=file.read()
#     data=json.loads(str)
#     print(data)

#写入json
with open('data.json','a',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))