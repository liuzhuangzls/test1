#!/usr/bin/python222
# -*- coding:utf-8 -*-
# def xx(b=10):
#     a=0
#     for i in range(b+1):
#         a=a+i
#         print(a)
# xx()
# a= lambda x,y:x*y
# print(a(12,19999900080000002000000070000600004000000000040))
# a=0;b=0
# while b<101:
#     a=a+b
#     b=b+1
# print(a)
# a=[1,4,2,3,5,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#
# for j in range(1,len(b)):
#     for x in range(len(b)-1):
#         if b[x]>b[x+1]:
#             b[x],b[x+1]=b[x+1],b[x]
# print(a.count(min(b))),'个',min(b)
#
# print(a.count(max(b))),'个',max(b)
# print(a.count(b[-1]),'个',b[-1])
# f= open('a.txt','w',encoding='utf-8')
# with open('a.txt','r',encoding='utf-8')as f:
#     print(f.read)
# import day2
# print(day2.qwe(50))
# from day2 import *
# print(qwe(50))
# n=1
# while n<=100:
#     if n > 10:
#          break
#     print(n)
#     n+=1
# print('hello')
# n=0
# while n<=100:
#     n+=1
#     if n%2==0:
#      continue
#     print(n)
# a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# while True:
#     b=int(input('请输入一个十进制数'))
#     if b<0:
#         break
#     f=''
#     while True:
#         c=b%16
#         b=b//16
#         f+=a[c]
#         if b==0:
#             break
# #     print(f[::-1])
# a=input('请输入三条边')
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
#     c.sort()
# if c[0]+c[1]>c[2]:
#     if c[0]**2+c[1]**2==c[2]**2:
#         print('直角')
#     elif c[0]**2+c[1]**2<c[2]**2:
#         print('钝角')
#     elif c[0]**2+c[1]**2>c[2]**2:
#         print('锐角')
# else:
#     print('输入错误')
# n=0
# while n <10:
#     n+=1
#     if n%2==0:
#      continue
#     print(n)
# account=int(input("请输入您的资产:"))
# i=0
# dic={}
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998}]
#
# for el in goods:
#     i+=1
#     dic.setdefault(str(i)+el["name"],el["price"]) #使用字符串拼接,把序号加到键前面
# print(dic)
#
# lst=[] #创建一个列表形式的购物车
# money=0 #购物车中初始值为0
# while 1:
#     ret=input("请输入您要买的东西序号(q退出.n结算):").strip()
#     if ret.isdigit():
#         for el in dic:
#             if ret == el[0]:  #利用切片得到商品序号,判断用户输入的序号是否是商品序号
#               lst.append(el[1:]) #将商品添加到列表中
#               money +=dic[el]  #计算购物车中商品的总价
#               print("购物车中有:%s,消费总额为%s"%([i for i in lst],money))
#
#     elif ret.upper()=="Q": #执行退出操作
#        print("退出成功!\n余额还有%s"%account)
#        break
#     elif ret.upper()=="N": #执行结算操作
#        blance=account-money #余额 = 资产 - 消费总额
#        if blance <0:
#            print("您的余额不足!!!")
#        else:
#            print("购买成功,花费了%d,余额还剩%s"%(money,blance))
#        break
#     else:
#        print("输入有误,请再次输入!!!")
# a= int(input('输入你的人民币：'))
# print('账户余额{}'.format(a))
# a=[1,2,6,8,3,9,4,8,9]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in a:
#    if i==b[-1] or i==b[-2]:
#     print(i)
# a=[2,1,5,7,4]
# for i in range(len(a)-1):
#    a[i],a[i-1]=a[i-1],a[i]
# print(a)
# for i in range(1,10):
#    for j in range(1,i+1):
#       print('{}*{}={}'.format(i,j,i*j),end='\t')
#    print()
#10进制转16进制
# a=[str(x) for x in range(10)]+[chr(x) for x in range(97,103)]
# b=int(input('>>>>'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#      break
# f.reverse()
# f=''.join(f)
# print('0x{}'.format(f))
# class 小爱():
#    def 打电话(self):
#       print('打电话')
#       # self.播放音乐()
#       self.__发信息()
#    def __发信息(self):
#       print('发信息')
#    def 播放音乐(self):
#       print('播放音乐')
# xai=小爱()
# xai.打电话()
#
# xai.打电话()
# class 小强():
#    def  打他(self):
#       print('打他')
#
# 小强().打他()
# class 小度(小爱,小强):
#    pass
# xai=小度()
# 小度().发信息()
# 小强=小度()
# 小度().打他()
# class 小强(小爱):
#    def 打电话(self):
#       print('打电话')
#       print('视频电话')
# 小爱=小强
# 小爱().发信息()
# 小爱().打电话()
# a=[str(x) for x in range(10)]+[chr(x) for x in range(97,103)]
# b=int(input('>>>>'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#      break
# f.reverse()
# f=''.join(f)
# print('0x{}'.format(f))
# a=[str(x) for x in range(10)]+[chr(x) for x in range(97,103)]
# b=int(input('>>>:'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#      break
# f.reverse()
# f=''.format(f)
# print('0x{}'.format(f))
# a=[1,3,6,2,8,4,9]
# b=a.copy()
# # b=list(set(b))
# b.sort()
# print(b)
from xlutils.copy import copy
import  xlrd
f=xlrd.open_workbook('a.xls')
new_f-copy(f)
sheet=new_f.get_sheet(0)