#!/usr/bin/python
# -*- coding:utf-8 -*-
from wotuyun.funl.duqu2 import wd,xinxi,xc

import unittest
from time import sleep
from appium import webdriver
class qinqiu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
            a = {
                "device": "android",
                "platformName": "Android",
                "platformVersion": "7.1.2",
                "deviceName": "6203e00d",
                "appPackage": "com.alltuu.android",
                "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity",
                "noReset": "True"
            }
            cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
            sleep(8.0)
    # def dengl(self):
    #         d=self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.EditText')
    #         d[0].send_keys('17826808915')
    #         sleep(5.0)
    #         d[1].send_keys('123456')
    #         sleep(5.0)
    #         f=self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.view.ViewGroup')
    #         f[13].click()
    def tiaozsc(self):
        f=self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.ImageView')
        f[8].click()
        sleep(5.0)
    def dianjituichu(self):
        fff=self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
        fff[0].click()
        sleep(2.0)

    def tiaozhuanwod(self):
            ff = self.dr.find_element_by_id('android:id/content').find_elements_by_class_name('android.view.ViewGroup')
            ff[31].click()
            sleep(2.0)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def test_1(self):
        # self.dengl()
        self.tiaozsc()

        text=xc(self.dr)
        self.assertEqual(text,'创建相册')
        sleep(3.0)
        self.dianjituichu()

        sleep(2.0)
        self.tiaozhuanwod()
        sleep(2.0)

    def test_2(self):
        text = xinxi(self.dr)
        self.assertEqual(text, '测试用户')
        sleep(2.0)

    def test_3(self):
        text = wd(self.dr)
        self.assertEqual(text,'云存储')


if __name__ == '__main__':
    unittest.main()



from selenium import webdriver
from lxml import etree
from pyquery import PyQuery
import time
drive=webdriver.Chrome()
drive.get()
drive.implicitly_wait(10)#智能等待
drive.find_element_by_link_text().click()
sleep(3.0)


