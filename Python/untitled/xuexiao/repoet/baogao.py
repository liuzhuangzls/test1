#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from src.testcase import HTMLTestRunner


def Baogao(name):
    suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(qwe))
    #两个参数 1.路径 2.通配符
    for i in name:
        dis=unittest.defaultTestLoader.discover(r'e:\PycharmProjects\untitled\xuexiao\jiekou_test',pattern='test_{}.py'.format(i.strip()))

        for j in dis:
             suit.addTest(j)
    f = open('abc.html', 'wb')
    # 定义一个测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='刘壮', description='结果如下')
    runner.run(suit)
    f.close()
# Baogao('*')
