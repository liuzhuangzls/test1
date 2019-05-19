#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
#查看当前文件的绝对路径
# a= os.path.dirname(os.path.abspath(__file__))
# print(a)
#项目根目录
BASE_DIR=os.path.splitdrive(os.path.abspath(__file__))
#日志目录
LOG_DIR=BASE_DIR+r'\logs'
#报告目录
REPORT_DIR=BASE_DIR+r'\repotr'
#原文件目录
SRC_DIR=BASE_DIR+r'\src'
#测试用例目录
TEST_CASE=BASE_DIR+r'\testcase'
#页面方法目录
FUNC=BASE_DIR+r'\element'

UNTIL=BASE_DIR+r'\until'
