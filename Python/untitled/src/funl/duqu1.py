#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml
from time import sleep
import time
with open(r'E:\PycharmProjects\untitled\src\element\a.yaml','r',encoding='utf-8') as f:
#    a=yaml.load(f)  使用yaml模块的load方法yaml文件中的数据转换为Python字典格式
    item_data=yaml.load(f,Loader=yaml.CFullLoader)
    print(item_data)
def wx(driver):
    time.sleep(2)
    text1 = driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    return text1

def qq(driver):
    time.sleep(2)
    # driver = dr
    text2 = driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
    return text2

def weibo(driver):
    time.sleep(2)
    # driver = dr
    text3 = driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
    return text3

def mima(driver):
    time.sleep(2)
    # driver = dr
    text4 = driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
    return text4



