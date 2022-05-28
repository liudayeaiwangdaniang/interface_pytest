# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RSA加密签名处理.py
# @Time      :2022/4/28 19:11
# @Author    :ming


"""
RSA加密： http://www.lemfix.com/topics/355
调用接口加密处理参考方案
https://www.cnblogs.com/Simple-Small/p/11284110.html

加密方法：
"""

import rsa
import base64
from time import time

def rsaEncrypt(msg):
    """
    公钥加密
    :param msg: 要加密的内容    str格式
    :return: 加密之后的密文
    """
    server_pub_key = """ 
    -----BEGIN PUBLIC KEY-----
    开发那获取到的公钥
    -----END PUBLIC KEY-----

    """

    # 生成公钥对象
    pub_key_byte = server_pub_key.encode("utf-8")
    pub_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_byte)

    # 要加密的数据转成字节对象
    content = msg.encode("utf-8")

    # 加密，返回加密文本
    cryto_msg = rsa.encrypt(content,pub_key_obj)
    # base64编码
    cipher_base64 = base64.b64encode(cryto_msg)
    # 转成字符串
    return cipher_base64.decode()

def generator_sign(token):
    #获取token的前50位
    token_50 = token[:50]
    # 生成时间戳
    timestamp = int(time())
    # 拼接token前50位和时间戳
    msg = token_50 + str(timestamp)

    sign = rsaEncrypt(msg)
    return sign,timestamp