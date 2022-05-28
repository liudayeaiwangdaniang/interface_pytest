

import os
import logging
from Common.handle_config import conf
from Common.handle_path import logs_dir

class MyLogger(logging.Logger):

    def __init__(self,file=None):
        # 设置输出级别，输出渠道,输出日志格式
        super().__init__(conf.get("log","name"),conf.get("log","level"))

        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s -%(lineno)d行：%(message)s  '
        formatter = logging.Formatter(fmt)

        #控制台渠道
        # 设置日志输出在哪些渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

# 是否需要写入文件
if conf.getboolean("log","file_ok"):
    file_name = os.path.join(logs_dir,conf.get("log","file_name"))
else:
    file_name = None

logger = MyLogger(file_name)
# logger.info("1111")



# if __name__ == '__main__':
#     mlogger = MyLogger("py30",file="my_logger.log")
#     mlogger.info("测试，我自己封装的日志类")

"""
日志的名字
日志的级别
日志的文件-级别
日志的控制台-级别
日志的文件路径

可配置化？  软编码/硬编码

6个测试环境  -  6个数据库  -  1套代码  -  配置文件 .conf   .ini
1套封装好的日志功能 -3个项目的自动化

.ini
yaml
"""