#!/usr/bin/python
# -*- coding:utf-8 -*-
# for i in range(1,10):
#     if i ==7:
#         continue
# #     else:
# #         print(i)
# a=[12,23,34]
# for i in a:
#      print(i)
#可以被2和3整除的
# a= int(input('>>>>'))
# if a%2==0:
#     if a%3==0:
#         print ('nihao')
#     else:
#         print(haha)
# elif a%3==0:
#     print('22')
# else:
#     print('11')
# a=0
# for i in range(2,100):
#      for j in range(2,i+1):
#          if i%j==0:
#             break
#      if i==j:
#          a+=i
# print(a)
# import random
# a=random.randint(1,10)
# for i in range(1,4):
#     b=int(input('>>>>'))
#     if a==b:
#         print ('True')
#         break
#     elif b>a:
#         print ('大了,还有{}次机会'.format(3-i))
#     else:
#         print('小了,还有{}次机会'.format(3-i))
# else:
#     print('废物')
# import copy
# c=[[12,32],2,4,5]
# d=c.copy()
# b=copy.deepcopy(c)
# c[0].append(123)
# print(b)
# print(d)
# a='qwe'
# b=a.replace('qw','119')
# print(b)
# a=[12,34,56]
# a.remove(12)
# print(a)
# a=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         a+=i
# print(a)
# for i in range(1,10):
#     for j in range(1,1+i):
#         a='%d*%d=%d'
#         a=a%(i,j,i*j)
#         print(a,end='\t ')
#     print()
# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#           if i%j==0:
#               a+=j
#     if a==i:
#      print(a)
# def ss():
#    a = input('>>>:')
#    b=a.split(',')
#    for i in range(1,len(b)):
#      for j in range(0,len(b)-1):
#          if int(b[j]) > int(b[j+1]):
#              b[j],b[j+1]=b[j+1],b[j]
#    print(b)
# ss()
# a=4
# def xx():
#     global a
#     a=3
#     print(a)
# xx()
# print(a)
# def xx(a,b):
#     print(a,b)
# xx(123,456)
# def   xx(b=0):
#      a=0
#      for i in range(b+1):
#        a+=i
#      print(a)
# xx(10)
#
# def xx(**a):
#     print(a)
# xx(name='xiao',age='20',sex='man')
# def xx(b):
#     a=0
#     for i in range(1,b+1):
#         a+=i
#     print(a)
#     return 10,19
# c=xx(1000)
# print(c)
#选择排序
# a=[]
# b=input('请输入数据:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(0,len(a)-1):
#     for y in range(x+1,len(a)-1):
#         if a[x] > a[y] :
#             a[x],a[y]=a[y],a[x]
# print(a)
#选择排序
# a=[]
# b=input('请输入数据:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(0,len(a)):
#     for y in range(x+1,len(a)):
#         if a[x] > a[y] :
#             a[x],a[y]=a[y],a[x]
# print(a)
# def xx(b=10):
#     a=0
#     for i in range(b):
#         a=i+1
#         print(a)
# xx()
a=input('>>>>:')
b=a[::-1]
c=0
for i in range(len(b)):
    for j in range(10):
        if str[j]==b[i]:
            c+=j*10**i        
            print(c)

