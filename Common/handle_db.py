# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_db.py
# @Time      :2022/4/14 23:01
# @Author    :ming

"""
1、连接数据库，创建游标 conn  cur
2、获取一条数据
3、获取条数
4、获取所有的数据
5、关闭数据库连接
"""

import pymysql

from Common.handle_config import conf

class HandleDB:

    def __init__(self):
        # 连接数据库，创建游标 conn  cur
        # 1、建立连接
        self.conn = pymysql.connect(
            host=conf.get("mysql","host"),
            port=conf.getint("mysql","port"),
            user=conf.get("mysql","user"),
            password=conf.get("mysql","password"),
            database=conf.get("mysql","database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

        # 2、创建游标
        self.cur = self.conn.cursor()


    def get_one_data(self,sql):
        self.conn.commit()   # 数据库保持同步
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all_data(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        return self.cur.execute(sql)

    def update(self,sql):
        """
        对数据库进行增、删、改的操作
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    sql = 'SELECT * FROM member LIMIT 3'
    db = HandleDB()
    count = db.get_count(sql)
    print("结果个数为",count)
    data = db.get_one_data(sql)
    print("一条数据",data)
    all = db.get_all_data(sql)
    print("所有的数据",all)
    db.close()
