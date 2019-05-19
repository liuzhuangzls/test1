#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest
#
# class DS(unittest.TestCase):
#     #连接参数
#     d = {
#             "platformName": "Android",
#             "platformVersion": "5.1.1",
#             "deviceName": "emulator-5554",
#             "appPackage": "com.qk.butterfly",
#             "appActivity": ".main.LauncherActivity"
#     }
#     #初始化环境变量
#     # def setUp(self):
#     #
#     #
#     # # def __init__(self):
#     #     self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
#     #     sleep(5.0)
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
#         sleep(5.0)
#
#
#     # @classmethod
#     # def tearDownClass(cls):
#     #     cls.dr.quit()
#     #     sleep(5.0)
#
#     def test_1(self):
#     #检查那四个文字的函数方法
#     # def check_text(self):
#         #获取微信文字
#         w = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#     #断言
#         self.assertEqual(w,'微信')
#         print(w)
#         # return w
#         sleep(10.0)
#     def test_2(self):
#         q=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(q,'微博')
#         print(q)
#         sleep(10.0)
#     def test_3(self):
#         a=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(a,'QQ')
#         print(a)
#         sleep(10.0)
#     def test_4(self):
#         d=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(d,'密码')
#         print(d)
#         sleep(10.0)
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#         sleep(5.0)
# #关闭app函数
#     # def close_app(self):
#     # def tearDown(self):
#     #     self.dr.quit()
#
# if __name__=='__main__':
#     unittest.main()

# unittest.main(verbosity=2,warnings=True)
#     go=DS()
#     #创建一个DS类的实例，赋予go
#     #调用DS类
#     go.check_text()
#     go.close_app()


from time import sleep
import unittest
from appium import webdriver
class ce(unittest.TestCase):
    a = {
                  "platformName": "Android",
                  "platformVersion": "5.1.1",
                  "deviceName": "emulator-5554",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity"
            }
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)


    def join(self,name,password):
        sleep(10)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(10)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        sleep(10.0)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        sleep(5.0)
        print('准备登陆')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(10.0)


    def test_1(self):
        self.join('17639610060','960514liu')
        sleep(10.0)
        print('开始断言')
        text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
        self.assertEqual(text,'热门')
    def shouye(self):
        # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
        # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
        self.dr.find_element_by_id('android:id/tabs').find_element_by_class_name('android.widget.RelativeLayout')




    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
if __name__ == '__main__':
    unittest.main()



