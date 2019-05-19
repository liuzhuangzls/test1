#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml
from time import sleep
import time
with open(r'E:\PycharmProjects\untitled\wotuyun\element\a.yaml','r',encoding='utf-8') as f:
    item_data=yaml.load(f,Loader=yaml.CFullLoader)

def wd(add):
    text1 = add.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
    return text1[4].text
def xinxi(aa):
    text2=aa.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
    return text2[1].text
def xc(cc):
    text3=cc.find_element_by_id('android:id/content').find_elements_by_class_name('android.widget.TextView')
    return text3[7].text