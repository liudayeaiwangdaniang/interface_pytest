# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :正则表达式学习.py
# @Time      :2022/4/17 16:46
# @Author    :ming

"""
字符串：正则表达式
http://www.lemfix.com/topics/393

字符串匹配，提取
regular

单个匹配表达式
    。    匹配除”\n“之外的任何单个字符
    \d   匹配一个数字字符，等价于[0-9]
    \D   匹配一个非数字字符，等价于[^0-9]
    \w   匹配包括下划线的任何单词字符，等价于[A-Za-z0-9_]
    \W   匹配特殊字符，等价于[A-Za-z0-9_]
    [xyz] 字符集合 匹配到集合中包含的所有字符
    [a-z] 字符范围，匹配范围内的任意字符
    x|y 匹配x或者y
数量上的匹配
    {m} n是一个非负整数，匹配前一个字符的n次
    {n,m}匹配前一个字符至少n次，最多m次
    {n,}匹配前一个字符至少n次，

    *  匹配前一个字符，0次或多次
    +  匹配前一个字符，1次或多次
    ?  匹配前一个字符，0次或1次

    res = re.findall("\d{3,5}",s)默认贪婪模式：尽可能匹配更多更长
    res = re.findall("\d{3,5}？",s)加?非贪婪模式：尽可能匹配更少
边界字符
    ^ 匹配输入字符串的开始位置
    $ 匹配输入字符串的结束位置
（）匹配分组，将括号里的匹配出来
"""
import re

s = "{'id': 1, 'interface': 'recharge', 'title': '充值成功-整数', 'method': 'post', 'url': 'member/recharge', 'request_data': '{'member_id':34325120,'amount':600}', 'expected': '{'code': 0, 'msg':'OK','data':{'id':34325120,'leave_amount':#money#}}', 'check_sql': 'SELECT CAST(member.leave_amount AS CHAR) as leave_amount FROM member WHERE ID=34325120'}"
res = re.findall("#(.*?)#", s)
print(res)
# s = "hjkfdhskhf15465431sdfd12!$#$#%sgfsd明"
#
# # 数量上的匹配
# # res = re.findall(".{3}",s)
# # print(res)
# res = re.findall("\d+",s)
# print(res)
# res = re.findall("1.*",s)
# print(res)

# 单字符匹配
# res = re.findall(".",s)
# print(res)
# res = re.findall("\d",s)
# print(res)
# res = re.findall("\D",s)
# print(res)
# res = re.findall("\w",s)
# print(res)
# res = re.findall("\W",s)
# print(res)
# res = re.findall("[abcd]",s)
# print(res)
# res = re.findall("[A-Za-z0-9]",s)
# print(res)