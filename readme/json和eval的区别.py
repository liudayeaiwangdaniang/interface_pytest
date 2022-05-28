# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :json和eval的区别.py
# @Time      :2022/4/23 14:27
# @Author    :ming
"""
eval 完成表达式里的计算并返回结果
json 是什么样就直接转换，没有计算
"""

import json

sss = '{"member_id":202+1,"title":"借钱实现财富自由","amount":2000,"loan_rate":12.0,"loan_term":3,"loan_date_type":1,"bidding_days":5}'

# s = json.loads(sss)
s = eval(sss)
print(s)
