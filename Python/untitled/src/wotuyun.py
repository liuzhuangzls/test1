#!/usr/bin/python
# -*- coding:utf-8 -*-
# from appium import webdriver
# from time import sleep
# import unittest
# class wo(unittest.TestCase):
#     a={
#       "platformName": "Android",
#       "platformVersion": "5.1.1",
#       "deviceName": "emulator-5554",
#       "appPackage": "com.alltuu.android",
#       "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity"
#     }
#     def ww(self,user,password):
#         dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.a)
#         sleep(10.0)
#     def kaishi(self,user,password):
#         d=self.dr.find_element_by_id('android:id/content').find_element_by_class_name('android.widget.EditText')
#         print(d)
#         sleep(5.0)
#         self.dr.find_element_by_id('android:id/content').find_element_by_class_name('android.widget.EditText').send_keys(password)
#         sleep(5.0)
#     def test_1(self):
#         self.ww('17639610060','960514liu')
#         sleep(10.0)
# if __name__ == '__main__':
#     unittest.main()
#模拟器
# from appium import webdriver
# from time import sleep
# import unittest
# class wo(unittest.TestCase):
#     a={
#       "platformName": "Android",
#       "platformVersion": "5.1.1",
#       "deviceName": "emulator-5554",
#       "appPackage": "com.alltuu.android",
#       "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity"
#     }
#     dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
#     sleep(8.0)
#     d=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.EditText')
#     d[0].send_keys('17826808915')
#     sleep(5.0)
#     d[1].send_keys('123456')
#     sleep(5.0)
#     f=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.view.View')
#     f[16].click()
    # print(f)
    #
    # print(len(f))
from appium import webdriver
from time import sleep
import unittest
class wo(unittest.TestCase):
       a= {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "6203e00d",
            "appPackage": "com.alltuu.android",
            "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity",
            "noReset": "True"
       }
       dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
       sleep(8.0)
       # d=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.EditText')
       # d[0].send_keys('17826808915')
       # sleep(5.0)
       # d[1].send_keys('123456')
       # sleep(5.0)
       # f=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.view.ViewGroup')
       # # print(len(f))
       # f[13].click()
       # sleep(3.0)
       #点击我的
       ff=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.view.ViewGroup')
       ff[31].click()
       sleep(2.0)
       fff=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       print(fff[4].text)
       fff=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       print((fff[17]).text)
       sleep(2.0)
       ffff=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       print((ffff[16]).text)
       fff=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       print((fff[15]).text)
       sleep(2.0)

        #我的
       # a=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       # a[4].click()
       # sleep(2.0)
       #个人信息
       # b=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       # b[4].click()
       # sleep(5.0)
       # bb=dr.find_element_by_id('android:id/content').find_element_by_class_name('android.widget.TextView')
       # bb[0].click()
       # sleep(3.0)
       # #点击订单
       # c=dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
       # c[9].click()






