# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_requests.py
# @Time      :2022/4/11 22:07
# @Author    :ming
import json

import requests

from Common.my_logger import logger
from Common.handle_config import conf

def send_requsets(method,url,data=None,token=None):
    """

    :param method:
    :param url:
    :param data:字典形式的数据
    :param token:
    :return:
    """
    logger.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(token)
    # 得到完整的url
    url = __pre_url(url)
    #将请求数据转换成字典对象
    data = __pre_data(data)

    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))

    # 根据请求类型，
    method = method.upper() # 大写处理
    if method == "GET":
        resp = requests.get(url,data,headers=headers)
    else:
        resp = requests.post(url,json=data,headers=headers)
    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))

    return resp

def __handle_header(token=None):
    """
    {"mobile_phone": "13845467789", "pwd": "1234567890",}
    处理请求头，加上项目当中必带的请求头，如果有token，加上token
    :param token:token值
    :return:处理之后headers字典
    """
    headers = {"X-Lemonban-Media-Type": "lemonban.v2","Content-Type":"application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers

def __pre_url(url):
    """
    拼接接口的url地址
    :param url:
    :return:
    """
    base_url = conf.get("server","base_url")
    if url.startswith("/"):
        return base_url + url
    elif url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return base_url + "/" + url

def __pre_data(data):
    """
    如果data是字符串转换为字典对象
    :param data:
    :return:
    """
    if data is not None and isinstance(data,str):
        # 如果有null，则替换None
        if data.find("null") != -1:
            data = data.replace("null","None")
        # 使用eval转换成字典,eval过程中，如果表达式有计算会进行计算
        data = eval(data)
        # 不为空并且是字符串
        # return json.loads(data)

        # 如果是v3版本，需要加上sign和timetamp两个参数
        # if conf.get("server", "auth_type") == "lemonban.v3" and token is not None:
        #     from Common.handle_rsa import generator_sign
        #     sign,timestamp = generator_sign(token)
        #     data["sige"] = sign
        #     data["timestamp"] = timestamp
    return data


if __name__ == '__main__':
    login_url = "http://api.lemonban.com/futureloan/member/Login"
    login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
    resp = send_requsets("POST",login_url,login_datas)
    token =resp.json()["data"]["token_info"]["token"]

    recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    recharge_datas = {"menmber_id": "20019", "amount": "2000"}
    resp = send_requsets("POST",recharge_url,recharge_datas,token)
    print(resp.json())
