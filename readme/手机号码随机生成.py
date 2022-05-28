# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :手机号码随机生成.py
# @Time      :2022/4/15 22:15
# @Author    :ming
"""
1、随机生成11位手机号码 前3位+8位
2、进行数据校验
"""

prefix = [134,135,136,137,138,139,147,136,
          137,138,139,147,150,138,139,147,
          150,151,152,157]

import random
from day4.Common.handle_db import HandleDB

def get_new_phone():
    db = HandleDB()
    while True:
        #1、生成
        phone = __generator_phone()
        #2、校验
        count = db.get_count('select * from member where mobile_phone="{}"'.format(phone))
        if count == 0: # 如果手机号没有在数据库查到，表示未注册的号码
            db.close()
            return phone

def __generator_phone():
    index = random.randint(0,len(prefix)-1)
    phone = str(prefix[index]) # 前3位
    for _ in range(0,8):  # 生成后8位
        phone += str(random.randint(0,9))
    return phone


print(get_new_phone())
