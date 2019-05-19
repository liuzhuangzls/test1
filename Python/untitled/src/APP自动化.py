# #!/usr/bin/python
# # -*- coding:utf-8 -*-
# #导入appium和web模块
# from appium import webdriver
# from time import sleep
#
# #测试脚本与appium服务器进行连接的参数在appium输入参数json
# d={
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.qk.butterfly",
#   "appActivity": ".main.LauncherActivity"
# }
# #写http://127.0.0.1:4723/wd/hub
# #测试脚本和appium服务器进行连接的过程 dr就是appium服务器
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# sleep(5.0)
# #元素是id 就使用ID定位法
# # dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
# #获取微信文字，先定位上一级，再找下面的元素，没有id找class元素
# # d=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# # c=dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# # f=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# # j=dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# # print(d,f,j,c,)
# #插入等待时间，休眠几秒
# sleep(5.0)
# #什么时候可以用send_keys
# # send_keys() 输入的是字符串
# #  什么时候可以用send_keys？
# # 1 向手机的输入框内输入的数据的时候
# # 2 clickable ---》true
# # 3 enabled ---》 true
# # 4 foucsable --》 true
# #登陆，send_keys
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(5.0)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('17639610060')
# sleep(5.0)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('960514liu')
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(20.0)
# dr.find_element_by_id('com.qk.butterfly:id/iv_live').click()
# sleep(5.0)
# print('成功')
#
# #退出APP，包括后台也关闭
# # dr.quit()


from time import sleep
import unittest
from appium import webdriver
a = {
                  "platformName": "Android",
                  "platformVersion": "5.1.1",
                  "deviceName": "emulator-5554",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity"
            }

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
sleep(5.0)

dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(5.0)

dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('17639610060')
sleep(5.0)
#清空数据
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()


dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('960514liu')
sleep(5.0)

dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(5.0)

b=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
sleep(5.0)
b[3].click()
# #获取当前屏幕的分辩率 模拟手工上滑
size = dr.get_window_size()
x1 = size['width'] * 0.5  # x坐标 50
y1 = size['height'] * 0.25  # 起始y坐标 50
y2 = size['height'] * 0.75  # 150
for i in range(2):
    dr.swipe(x1, y2, x1, y1)

dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
sleep(0.5)
dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()



