#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest

class DS(unittest.TestCase):
    #连接参数
    d = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity"
    }

    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
    sleep(5.0)


    def tiao_zhuan(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(5.0)
    def login(self,phone,password):
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        sleep(10.0)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
    def denglu(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(10.0)
    def close_app(self):
        self.dr.quit()
        sleep(5.0)

if __name__ == '__main__':
    go=DS()
    go.tiao_zhuan()
    go.login('15103819460','13137246872zls')
    go.denglu()
