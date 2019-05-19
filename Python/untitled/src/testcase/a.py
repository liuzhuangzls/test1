#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import logging
import datetime
logs=os.path.join(r'E:\PycharmProjects\untitled\src\logs',str(datetime.datetime.now().date())+".out")
print(logs)
#创建一个日志文件
formatter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formatter)
#日志输出到控制台
con_handler=logging.StreamHandler()
#加载日志格式
con_handler.setFormatter(formatter)
#将日志输出到文本
Fil_handler=logging.FileHandler(logs,encoding='utf-8')
#加载日志格式
Fil_handler.setFormatter(formatter)
#定义一个函数
def get_logger(name):
    #获取脚本的名字传入日志中
    logger=logging.getLogger(name)
    #加入一个手柄
    logger.addHandler(con_handler)
    logger.addHandler(Fil_handler)
    #设置日志等级,INFO代表四级，包含以上三级，不包含四级
    logger.setLevel(logging.INFO)
    return logger

