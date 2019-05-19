#!/usr/bin/python
# -*- coding:utf-8
# a=[1,2,3,4]
# for i in a:
#     for j in a:
#         for k in a:
#            if i !=j and i!=k and j!=k:
#             print(i,j,k)
#追加
# from xlutils.copy import copy
# import  xlrd
# f=xlrd.open_workbook('a.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(7,0,'人生苦短，我用Python')
# new_f.save('a.xls')

#
# from xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('a.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write()
import  time
# a=time.time()
# print(a)
# a=time.localtime(1000000000)
# print(a)
# b=time.strftime('%y-%m-%d')
# print(b)
# a=(2019,10,10,1,2,3,4,5,6)
# b=time.mktime(a)
# print(b)
# for i in range(10):
#     print(i)
#     time.sleep(2)
# a=input('>>>:')
#  if a[:4]
# b=time.strftime('%Y-%m-%d')
# print(b)
# a=input('请输入年，月，日:')
# b=a.split(' ')
# c=[]
# for i in b:
#     c.append(int(i))
# if  c[0]%100==0:
#     if c[0]%400==0:
#         print('闰年')
# elif c[0]%4==0:
#     print('闰年')
# else:
#     print('no')
# k=time.strptime('{} {} {}'.format(c[0],c[1],c[2]),'%Y %m %d' )
# print(k)
# print('星期{}'.format(k[-3]+1))
# print('一年中的第{}'.format(k[-2]))

# 输入一个年月日判断是否为闰年 星期几 一年中第几天
# a=input('请输入年 月 日:')
# b=a.split(' ')
# c=[]
# for i in b:
#     c.append(int(i))
# if c[0]%4==0:
#     if c[0]%100==0:
#         if c[0]%400==0:
#             print('yes')
#         else:
#             print('no')
#     else:
#         print('yes')
# else:
#     print('no')
#
# k=time.strptime('{} {} {}'.format(c[0],c[1],c[2]),'%Y %m %d' )
# print('星期{}'.format(k[-3]+1))
# print('一年中的第{}'.format(k[-2]))





#把打印的内容写到文件中
# import calendar
# a=calendar.month(2018,6)
# print(a)
# with open('c.txt','w',encoding='utf-8-sig') as f:
#     f.write('{}'.format(a))


# a=input('请输入年，月，日:')
# # b=a.split(' ')
# c=time.strptime('{}'.format(a),'%Y-%m-%d' )
# print(c)
# d=time.mktime((c)-86400)
# print(c)

#
# import time
# m=[]
# a=input('请输入年份：')
# b=time.strptime(a,'%Y-%m-%d')
# print(b)
# for i in b:
#     m.append(i)
# m=tuple(m)
# chu=time.mktime(m)
# p=chu-86400
# q=time.localtime(p)
# n=time.strftime('%Y-%m-%d',q)
# print(n)

# def xx(b):
#     a=b[::-1]
#     b=0
#     for i in range(len(a)):
#         for j in range(10):
#             if str(j)==a[i]:
#                 b=b+j*10**i
#     print(b)
# xx('123')
#函数写不用in net 把字符串变成整数
# def xx(b):
#     a=b[::-1]
#     b=0
#     for i in range(len(a)):
#         for  j in range(10):
#            if str(j)==a[i]:
#                b=b+j*10**i
#     print(b)
# xx('123')
# a=input('>>>')
#    a=[::-1]
#    c=0
#    for i in range(len(a)):
#        for j in range(10):
#            if str(j)==a[i]:
#                b=a+j*10**i
#     print(a)


# a=int(input('>>>'))
# b=1
# if a<0:
#     print('负数没有阶层')
# elif a==0:
#     print('0的阶层为1')
# else:
#     for i in range(1,a+1):
#         b=b*1
#         print("%d 的阶乘为 %d" % (a, b))


# #阶层之和
# a= int(input("请输入一个数字: "))
# b= 1
# c=0
# if a< 0:
#   print("抱歉，负数没有阶乘")
# elif a == 0:
#    print("0 的阶乘为 1")
# else:
#    for i in range(1,a+1):
#     b = b*i
#     # print('{}的阶层{}'.format(a,b))
#     c+=b
#    print(c)
import time
m=[]
a=input('请输入年份：')
b=time.strptime(a,'%Y-%m-%d')
for i in b:
    m.append(i)
m=tuple(m)
chu=time.mktime(m)
p=chu-86400
q=time.localtime(p)
n=time.strftime('%Y-%m-%d',q)
print(n)

