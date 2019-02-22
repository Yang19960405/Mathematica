import pymssql
import requests
import re
import json


#连接数据库
class MSSQL:

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    #连接SQLServer数据库
    def _GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn=pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
        cur=self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    #查询条件
    def ExecQuery(self,sql):
        cur=self._GetConnect()
        #接收SQL语句
        cur.execute(sql)
        #返回查询结果
        resList=cur.fetchall()
        self.conn.close()
        return resList

    def ExecNotQuery(self,sql,data):

        cur1 = self._GetConnect()
        cur1.execute(sql,tuple(data.values()))
        self.conn.commit()
        self.conn.close()




def get_maoyantop_page(url):
    headers={
        'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    request=requests.get(url,headers=headers)
    request.encoding='utf-8'
    if request.status_code==200:
        return request.text

    return None;

#正则过滤页面
def parse_maoyan_page(html):
    pattern= re.compile(
        '<dd>.*?board-index.*?>(.*?)'
        '</i>.*?data-src="(.*?)"'
        '.*?name.*?a.*?>(.*?)'
        '</a>.*?star.*?>(.*?)'
        '</p>.*?releasetime.*?>(.*?)'
        '</p>.*?integer.*?>(.*?)'
        '</i>.*?fraction.*?>(.*?)'
        '</i>.*?</dd>',
        re.S)
    items= re.findall(pattern,html)

    for item in items:
        #yield  简单介绍：yield常见用法：该关键字用于函数中会把函数包装为generator。然后可以对该generator进行迭代: for x in fun(param).
        # 在一个函数中，程序执行到yield语句的时候，程序暂停，返回yield后面表达式的值，在下一次调用的时候，
        # 从yield语句暂停的地方继续执行，如此循环，直到函数执行完。
        yield {
            '排名':item[0],
            '评分':item[5].strip()+item[6].strip(),
            'image':item[1],
            '片名':item[2].strip(),
            '主演':item[3].strip()[3:] if len(item[3])>3 else '',
            '上映时间':item[4].strip()[5:] if len(item[4])>5 else '',
        }


def _GetDAta(TopList):
    return {
        "Tops":TopList['排名'],
        "Score":TopList['评分'],
        "Image":TopList['image'],
        "MovieName":TopList['片名'],
        "ToStar":TopList['主演'],
        "ReleaseTime":TopList['上映时间']
    }

def _GetSQL(TopList,table):
    data=_GetDAta(TopList)
    keys=','.join(data.keys())
    values=','.join(['%s']*len(data))
    return 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)


# ms=MSSQL(host="192.144.149.176",user="sa",pwd="SQLServer2014",db="WDMSDB")
# reslist=ms.ExecQuery("select * from W_Order")
# for i in reslist:
#     print(i)

def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html= get_maoyantop_page(url)
    for item in parse_maoyan_page(html):
        sql=_GetSQL(item,'MaoYanTop')

        ms=MSSQL(host="192.144.149.176",user="sa",pwd="SQLServer2014",db="PYTest")
        ms.ExecNotQuery(sql,_GetDAta(item))
    pass

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)