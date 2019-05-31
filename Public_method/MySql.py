# user/python3
# encoding:utf-8

import pymysql,json

with open("E:\\H5_AutoTest\\Public_file\\control.json", "r", encoding="UTF-8") as f:
    dict_load = json.load(f)


    def db_Query(self,database,sql):
        # 链接数据库
        self.db = pymysql.connect(
            host=dict_load['mysql']['host'],
            user=dict_load['mysql']['user'],
            password=dict_load['mysql']['pwd'],
            database=database
        )
        try:
            self.db
        except:
            print('数据库连接失败！请检查！')
        # 获取数据库列表
        self.cursor = self.db.cursor()
        self.cursor.execute('SHOW DATABASES')
        # 查询
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.db.close()
        return result


    def db_NotQuery(self,database,sql):
        # 链接数据库
        self.db = pymysql.connect(
            host=dict_load['mysql']['host'],
            user=dict_load['mysql']['user'],
            password=dict_load['mysql']['pwd'],
            database=database
        )
        try:
            self.db

        except:
            print('数据库连接失败！请检查！')
        # 获取数据库列表
        self.cursor = self.db.cursor()
        self.cursor.execute('SHOW DATABASES')
        # 查询
        self.cursor.execute(sql)
        self.db.commit()
        try:
            self.cursor.execute(sql)
        except:

            print('SQL执行失败，请检查！')
        self.db.close()

