#!/usr/bin/python
# -*- coding:utf-8 -*-
# from src.funl.duqu1 import foo
from src.funl.duqu1 import wx,qq,weibo,mima
import unittest
from time import sleep
from appium import webdriver
from src.testcase import HTMLTestRunner
# from src.until.aaaa import REPORT_DIR
from src.testcase.a import get_logger

#给日志一个变量
g=get_logger(name='test_1.py')


#测试脚本
class Text(unittest.TestCase):
  @classmethod
  def setUpClass(cls):

      d={
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity"
      }
      sleep(10.0)
      g.info('app建立成功')
      cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
  @classmethod
  def tearDownClass(cls):
    cls.dr.quit()
    g.info('关闭')

#测试用例
  def test_1(self):
        g.info('执行测试用例')
        #验证微信用例
        g.info('执行第一条用例')
        text=wx(self.dr)
        #断言
        self.assertEqual(text,'微信')
  def test_2(self):
        g.info('执行第二条用例')

        text=qq(self.dr)

        self.assertEqual(text,'QQ')
  def test_3(self):
        g.info('执行第三条用例')

        text=weibo(self.dr)

        self.assertEqual(text,'微博')

  def test_4(self):
        text=mima(self.dr)
        g.info('执行第四条用例')
        self.assertEqual(text, '密码')


if __name__== '__main__':
      # unittest.main()
      # #创建一个测试套件
      suit=unittest.TestSuite()
      #将测试用例添加到测试套件中
      suit.addTest(Text('test_1'))
      suit.addTest(Text('test_2'))
      suit.addTest(Text('test_3'))
      suit.addTest(Text('test_4'))
      #将qwe类中所有test开头的函数都添加到测试套件中
      #将路径写死
      # r_path=r'E:\PycharmProjects\untitled\src\testcase\abc.html'
      #卸货
      # r_path1=REPORT_DIR+'HTMLTestRunner'

      #打开一个空文件
      f=open(r'abc.html','wb')
      #定义一个测试报告的信息
      runner= HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='刘壮', description='结果如下',verbosity=2)
      #verbosity默认是0，2使控制台更加详细
      runner.run(suit)
      f.close()


