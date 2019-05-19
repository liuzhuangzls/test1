#!/usr/bin/python
# -*- coding:utf-8 -*-
# import day3
# day3.xai.打电话()
# class 小爱():
#    def 打电话(self,name):
#       print('打电话{}'.format(name))
#       # self.播放音乐()
#       # self.发信息()
#    def 发信息(self,name):
#       print('发信息{}'.format(name))
#    def 播放音乐(self):
#       print('播放音乐')
class 小爱():
   # name='小强'
   def __init__(self,a):
     self.name=a
   def 打电话(self):
      print('打电话{}'.format(self.name))
      # self.播放音乐()
      # self.发信息()
   def 发信息(self):
      print('发信息{}'.format(self.name))
   def 播放音乐(self):
      print('播放音乐{}'.format(self.name))
xai=小爱('明明')
xai.发信息()
xai.打电话()
# 小爱().打电话()
da=小爱('231')
da.发信息()