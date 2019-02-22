import requests
import pymssql
import Mathematica.MSSQL
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
from Mathematica.MSSQL import MSSQL



base_url='https://m.weibo.cn/api/container/getIndex?'

#请求头
headers={
    'Host':'m.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}



#将数据存入MongoDB中
# def save_to_mongodb(results):
#     client = MongoClient()
#     db = client['weibo']
#     collection = db['weibo']
#     if collection.insert(result):
#         print("OK")

#将数据存入SqlServer中
# def save_to_SQLServer(results):
#     db=MSSQL(host="192.144.149.176",user="sa",pwd="SQLServer2014",db="PYTest")
#     db.ExecNotQuery(db._GetSQL(_getData(results),'weiboText'),_getData(results))


#获取ajax数据
def get_page(page):
    params={
        'type':'uid',
        'value':'2830678474',
        'containerid':'1076032830678474',
        'page':page
    }
    url=base_url+urlencode(params)                     #urlencode()函数  将键值对类型的数据转换成a=1&b=2这样的字符串
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

#数据过滤
def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo_data = {}
            if item!=None:
                weibo_data['id'] = item.get('id')
                weibo_data['comments'] = item.get('comments_count')
                weibo_data['attitudes']=item.get('attitudes_count')
                weibo_data['text']=pq(item.get('text')).text()
                weibo_data['reposts']=item.get('reposts_count')
                yield weibo_data

def _getData(json):
    return {
        "id":json['id'],
        "comments":json['comments'],
        "attitudes":json['attitudes'],
        "text":json['text'],
        "reposts":json['reposts']
    }

if __name__ == '__main__':
    for page in range(1,11):
        json=get_page(page)
        for result in parse_page(json):
            #save_to_SQLServer(result)
            #save_to_mongodb(json)
            pass


