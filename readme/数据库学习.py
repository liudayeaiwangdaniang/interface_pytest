# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :数据库学习.py
# @Time      :2022/4/14 21:54
# @Author    :ming


"""
各大数据库操作文章：http://www.lemfix.com/topics/306

mysql 数据库：pymysql
pip install pymysql

数据库操作步骤
1、连接数据库，创建游标
2、执行sql语句
3、获取执行的结果
4、关闭数据库连接
"""

import pymysql

# 1、建立连接
conn = pymysql.connect(
    host="api.lemonban.com",
    port=3306,
    user="future",
    password="123456",
    database="futureloan",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# 2、创建游标
cur = conn.cursor()

# 3、执行sql语句
# sql = 'SELECT * FROM member WHERE mobile_phone="13265895752"'
sql = 'SELECT * FROM member LIMIT 3'

count = cur.execute(sql)   # 返回的是，sql语句执行结果的行数

# 4、获取sql语句执行后的数据结果
one = cur.fetchone() #获取结果集当中的一条
print("第一条数据",one)
two = cur.fetchone()
print("第二条数据",two)
print("=================")
all = cur.fetchall() # 获取所有的数据
print("所有数据",all)

# 5、关闭游标，关闭数据库连接
cur.close()
conn.close()