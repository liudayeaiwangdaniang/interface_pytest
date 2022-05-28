# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :利用正则表达式替换.py
# @Time      :2022/4/17 21:27
# @Author    :ming
from Common.handle_data import EnvData
from Common.handle_config import conf

setattr(EnvData,"member_id","12345678900000")
setattr(EnvData,"user_money","2500")

import re

# data = '{"member_id":#member_id#,"amount":600,money:#user_money#,username:"#user#}'
#
# res = re.findall("#(.*?)#",data) # 如果没有找到，返回的是空列表
# print(res)
#
# # 标识符对应的值， 来自于 1、环境变量 2。配置文件
# if res:
#     for item in res:
#         # 得到标识符对应的值
#         try:
#             vaule = conf.get("data",item)
#         except:
#             vaule = getattr(EnvData,item)  # 反射
#         print(vaule)
#         # 再去替换原字符串
#         data = data.replace("#{}#".format(item),vaule)
#     print(data)

def replace_by_regular(data):
    res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表
    # 标识符对应的值， 来自于 1、环境变量 2。配置文件
    if res:
        for item in res:
            # 得到标识符对应的值
            try:
                vaule = conf.get("data", item)
            except:
                vaule = getattr(EnvData, item)  # 反射
            # 再去替换原字符串
            data = data.replace("#{}#".format(item), vaule)
        return data

data = '{"member_id":#member_id#,"amount":600,money:#user_money#,username:"#user#}'
res = replace_by_regular(data)
print(res)
