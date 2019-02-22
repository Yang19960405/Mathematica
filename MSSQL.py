import pymssql

class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    # 连接SQLServer数据库
    def _GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    # 查询条件
    def ExecQuery(self, sql):
        cur = self._GetConnect()
        # 接收SQL语句
        cur.execute(sql)
        # 返回查询结果
        resList = cur.fetchall()
        self.conn.close()
        return resList

    # 非查询操作
    def ExecNotQuery(self, sql, data):
        cur1 = self._GetConnect()
        cur1.execute(sql, tuple(data.values()))
        self.conn.commit()
        self.conn.close()

    # 拼接添加数据的SQL语句
    def _GetSQL(self,data, table):
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        return 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

    def _Test(self):
        print("成功调用")

