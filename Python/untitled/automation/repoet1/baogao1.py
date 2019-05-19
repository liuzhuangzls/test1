#!/usr/bin/python
# -*- coding:utf-8 -*-
from automation.repoet1 import HTMLTestRunner
import unittest
# from interface_test.jiekou_test.test_denglu import qwe
def Baogao():
    suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(qwe))
    #两个参数 1.路径 2.通配符
    # for i in name:
    dis=unittest.defaultTestLoader.discover(r'e:\PycharmProjects\untitled\automation\jiekou_test',pattern='test_*.py')
    for j in dis:
            suit.addTest(j)
            print(j)
    f = open('ab.html', 'wb')
    # 定义一个测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='刘壮', description='结果如下')
    runner.run(suit)
    f.close()
Baogao()