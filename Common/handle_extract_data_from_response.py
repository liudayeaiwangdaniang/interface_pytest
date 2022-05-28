# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_extract_data_from_response.py
# @Time      :2022/4/22 22:12
# @Author    :ming
#  详情  根据excel中表达式获取响应当中的值
"""

"""
import jsonpath

from Common.handle_data import EnvData
from Common.my_logger import logger


def extract_data_from_response(extract_exprs,response_dict):
    """
    根据jsonpath提取表达式，从响应结果当中，提取数据并设置为全局变量EnvData类的类属性，并作为全局变量储存
    :param extract_exprs: excel当中读取出来的，提取表达式的字符串
    :param response_dict: http请求之后的响应结果
    :return:
    """
    # 将提取表达式转换为字典
    extract_dict = eval(extract_exprs)
    logger.info("要从响应结果当中提取的数据集为：\n{}".format(extract_dict))
    # 遍历字典，key作为全局变量名，value是jsonpath提取表达式
    for key,value in extract_dict.items():
        # 提取
        res = str(jsonpath.jsonpath(response_dict,value)[0])
        # 设置环境变量
        logger.info("设置环境变量.key:{},value:{}".format(key,res))
        setattr(EnvData,key,res)


if __name__ == '__main__':
    ss = '{"member_id":"$..id"}'
    response = {'code': 0, 'msg': 'OK',
                'data': {'id': 34324947, 'reg_name': 'ming123456', 'mobile_phone': '14564567789'},
                'copyright': 'Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved'}

    extract_data_from_response(ss,response)
    print(EnvData.__dict__)