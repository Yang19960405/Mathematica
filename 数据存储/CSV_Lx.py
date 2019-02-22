import csv

#存
# with open('biaoge2.csv','a',encoding='utf-8') as biaoge:
#     writer=csv.writer(biaoge)
#     fieldnames=['id','name','age']
#     writer=csv.DictWriter(biaoge,fieldnames=fieldnames)
#     #writeheader()先写入头数据
#     writer.writeheader()
#     writer.writerow({'id': '1001','name':'yangheng1','age':'22'})
#     writer.writerow({'id': '1002', 'name': 'yangheng2', 'age': '22'})
#     writer.writerow({'id': '1003', 'name': 'yangheng3', 'age': '22'})
#     writer.writerow({'id': '1004', 'name': 'yangheng4', 'age': '22'})



#读取
with open('biaoge2.csv','r',encoding='utf-8') as bg:
    reader=csv.reader(bg)
    for re in reader:
        print(re)
