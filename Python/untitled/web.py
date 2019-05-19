#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from time import sleep
dr=webdriver.Chrome()
# dr.get('https://www.douban.com/') #一号
# print(dr.title)
# #获取第一个窗口的字符串
# print(dr.current_window_handle)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click() #二号窗口
# sleep(3.0)
# #获取所有窗口标识
# ww=dr.window_handles
# #切换窗口
# dr.switch_to.window(ww[-1])
# print(dr.title)


#切换窗口 浏览器本身无法决定打开是那个窗口
#按照打开的窗口顺序给窗口标号 ———标识这个窗口的字符串
# dr.switch_to_window()
# #网页框架  iframe 有ID class直接定位 ID就是login——frame
# dr.switch_to.frame('login_frame')
# #先定位框架 如果没有ID和class 先可以定位路径
# w=dr.find_element_by_xpath('//*[@id="web_qr_login"]')
# dr.switch_to_frame(w)
# #退出框架 也是退出到最开始的页面
# dr.switch_to_default_content()
# #切换到上一级框架
# dr.switch_to.parent_frame()
# dr.get('file:///C:/Users/lz/Desktop/abc.html')
# time.sleep(5.0)
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2.0)
# #将控制器切换到弹出框
# ww=dr.switch_to_alert()
# #获取弹出框上的文本
# print(ww.text)
# #输入
# ww.send_keys('1234')
# # 点击确定
# ww.accept()
# #点击取消
# # ww.dismiss()

# dr.find_element_by_id('switcher_plogin').click()
# sleep(2.0)
# dr.find_element_by_id('u').send_keys('1746147518')
# sleep(2.0)
# dr.find_element_by_id('p').send_keys('liuzhuang960514')
# dr.find_element_by_id('login_button')

# dr.switch_to.frame('login_frame')
# dr.find_element_by_id('kw').send_keys('python')
# time.sleep(2.0)

# dr.find_element_by_id('su').click()
#通过class定位
# dr.find_element_by_class_name('manv').click()
#t通过name定位
# dr.find_element_by_name('tj_trnews').send_keys()
# dr.get('https://www.jd.com')
# time.sleep(2.0)
# dr.back()
# time.sleep(2.0)
# dr.forward()
# print(dr.title)
# print(dr.current_url)
# dr.set_window_size(400,400)
# dr.set_window_position(400,400)
# dr.maximize_window()
# dr.minimize_window()
#文本定位
# dr.find_element_by_link_text('新闻').click()
# #模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()
# #通过标签页定位
# dr.find_element_by_tag_name('')
#xpath路径标记语言 路径定位
# dr.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
#css 定位
# dr.find_element_by_css_selector('#u1 > a:nth-child(1)').click()
# dr.find_element_by_id('appLoginTab').click()
# sleep(2.0)

# dr.find_element_by_id('1bApp').click()
#定位多个元素
# dr.find_elements_by_id('su')
#层级定位
#  层级定位 先定位一个顶层元素，在定位一个子元素 用于复杂的场景
# w=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in w:
#     i.click()
#     sleep(1.0)
# dr.get('https://qzone.qq.com/')
# dr.find_element_by_id('tb_logout').click()
# w=dr.switch_to.alert()
# w.accept()
dr.get('https://mail.163.com/')
dr.switch_to.frame('//*[@id="x-URS-iframe1558180896435.8828"]')
sleep(5.0)
w =dr.find_element_by_xpath('//*[@id="auto-id-1558170493980"]')
dr.switch_to_frame(w)
sleep(5.0)
dr.find_element_by_id('auto-id-1558170493982').send_keys('liuzhuangzls')
sleep(2.0)
dr.find_element_by_xpath('//*[@id="auto-id-1558170493934"]').send_keys('960514liu')
sleep(2.0)
dr.find_element_by_id('//*[@id="dologin"]').click()


# dr.get('https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fhome.jd.com%2F')
# sleep(2.0)
# dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
# sleep(5.0)
# dr.find_element_by_id('loginname').send_keys('17639610060')
# sleep(2.0)
# dr.find_element_by_name('nloginpwd').send_keys('960514liu')
# dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
sleep(5.0)

# dr.find_element_by_xpath('//*[@id="ttbar-home"]/a').click()
# sleep(5.0)
# ww=dr.window_handles
# sleep(2.0)
# dr.switch_to.window(ww[-1])
# sleep(2.0)
# dr.find_element_by_id('key').send_keys('钻石')
# sleep(3.0)
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
# sleep(2.0)
#
# dr.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[5]').click()
# sleep(5.0)
# dr.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[5]').click()
# sleep(3.0)
#
# dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(3.0)
#

