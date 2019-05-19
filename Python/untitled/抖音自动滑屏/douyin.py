#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
import time
from time import sleep

a = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "6203e00d",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": ".main.MainActivity"
}
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
sleep(10.0)
while True:
      size = dr.get_window_size()
      x1 = size['width'] * 0.5
      y1 = size['height'] * 0.25
      y2 = size['height'] * 0.75
      for i in range(2):
            dr.swipe(x1, y2, x1, y1)
      time.sleep(20)
