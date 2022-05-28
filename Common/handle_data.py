# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_data.py
# @Time      :2022/4/15 23:19
# @Author    :ming
"""
1、一条用例涉及到数据当中有 url request_data  check_sql
2
"""
import re
import json

from Common.handle_config import conf
from Common.my_logger import logger


class EnvData:
    """
    存储用例要使用到的数据
    动态设置类属性 setattr , hasattr , getattr ,delattr
    """
    pass
def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)

def replace_case_by_regular(case):
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            case[key] = replace_by_regular(value)
    logger.info("正则表达式替换之后的请求数据：\n{}".format(case))
    return case

    # #把case字典（从excel读取出来的一条用例数据）转换成字符串
    # case_str = json.dumps(case)
    # #替换
    # new_case = replace_by_regular(case_str)
    # #把替换的字符串，转换成字典
    # case_dict = json.loads(new_case)
    # return case_dict

def replace_by_regular(data):
    """
    将字符串当中，匹配#(.*?)#"部分，替换对应的真实数据
    真实数据只从2个地方去获取 一是配置文件当中data区域另一个是EnvData的类属性(在这两个地方都是字符串类型)
    :param data: 字符串
    :return:返回的是替换之后的字符串
    """
    res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表
    # 标识符对应的值， 来自于 1、环境变量 2。配置文件
    if res:
        for item in res:
            # 得到标识符对应的值
            try:
                value = conf.get("data",item)
            except:
                try:
                    value = getattr(EnvData,item)  # 反射
                except AttributeError:
                    # value = item
                    continue
            # 再去替换原字符串
            data = data.replace("#{}#".format(item), value)
    return data

def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，需要替换的会替换
    :param case: excel 当中读取出来的一条数据 是个字典
    :param mark:  数据当中标记的占位符 #值#
    :param real_data:  要替换mark的真实数据
    :return:
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case

if __name__ == '__main__':
    # case = {
    #     "method":"POST",
    #     "url":"http://api.lemonban.com/futureloan/#phone#/member/register",
    #     "request_data":'{"mobile_phone": "#phone#", "pwd": "1234567890","type":1,"reg_name":"ming123456"}'
    # }
    # if case["request_data"].find("#phone#") != -1: # != -1 说明能找到下标
    #     case = replace_mark_with_data(case,"#phone#","12398745600")
    # for key,value in case.items():
    #     print(key,value)
    case = '{"code": 0, "msg": "OK", "data": {"id": 34325120, "leave_amount": #money#}}'
    print(replace_case_by_regular(case))