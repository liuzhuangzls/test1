#!/usr/bin/python
# -*- coding:utf-8 -*-
# a=0
# for i in range(2,101):
#     for j in range(2,i+1):
#        if i%j==0:
#         break
#     if i==j:
#       a+=i
# print(a)
# for i in range(1,100):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a==i:
#         print(a)
# for i in range(1,10):
#     for j in range(1,1+i):
#         a='%d*%d=%d'
#         a=a%(i,j,i*j)
#         print(a,end='\t')
#     print()
# a=input('>>>:')
# b=a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j])>int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
#             print(b)
# print(b)
# a=0
# b=1
# while b<101:
#     a=a+b
#     b=b+1
# print(a)
# def xx(b):
#     a=0
#     for i in range(1,b+1):
#      a+=i
#     return a
# a=xx(100)
# print(a)
# a=0
# for i in range(0,100):
#     if i%2==0:
#         a
# x='a'
# y='b'
# print(x,end='')
# print(y,end='')
#回文
# a=input('>>>')
# for i in range(len(a)-1):
#     if a[i] != a   [-i-1]:
#         print('不是回文字符串')
#         break
# else:
#  print('是回文字符串')
# for i in range(1,1000):
#     b=i//100
#     c=i//10%10
#     d=i%10
#     if b**3+c**3+d**3==i:
#      print(i)
# a=[11,1,22,11,4]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# for i in range(1,100):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a==i:
#         print(a)
#九九乘法表
# for i in range(1,10):
#     for  j in range(1,i+1):
#         print(('{}*{}={}').format(i,j,i*j),end='\t')
#     print()
# a=0
# for i in range(1,101):
#     a+=i
# print(a)
# try:
#     a=0
#     print(a)
# except:
#    pass
# print('hello')
# print(a)
# try:
#     a=0
#     print(a+b)
# except Exception as e:
#     print('rty')
# else:
#  print('qwe')
# try:
#     a=0
#     print(a)
# except Exception as e:
#     print('e')
# else:
#     print(456)
# finally:
#     print(123)
# a=int(input('>>>'))
# if a>4:
#     raise TypeError('hello')
# else:
#     raise NameError(qwe)
# try:
#     a=0
#     print(a)
# except Exception as e:
#     print(e)
# else:
# a=int(input('>>>:'))
# print('转换为二进制：',bin(a))
# print("转换为八进制:",oct(a))
# print('转换为十六进制:',hex(a))
#1-2+3-4+5-6+7+....98+99=?
# a=0
# for i in range(0,100):
#     if i%2==0:
#         a=a-i
#     else:
#         a=a+i
# print(a)
# a=0;b=0
# for i in range(1,100,2):
#     a+=i
# for j in range(2,100,2):
#     b+=j
# print(a-b)
# a=input('>>>')
# b=a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j])>int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
#             print(b)
# print(b)
splb=[
    {"name":"电脑","price":2000},
    {"name":"鼠标","price":100},
    {"name":"游艇","price":5000},
    {"name":"美女","price":6000},
    {"name":"空无","price":0}
]
a=int(input('请输入银行卡金额:'))
b=[]
c=[]
while True:
    print('商品列表')
    for i,j in enumerate(splb):
        print(i,j)
    d=int(input('请选择商品:'))
    if d>4 or d<0:
        print('没有该商品')
        break
    else:
        s=splb[d]
        b.append(s)
        print('购物车:')
        print(b)
        c.append(splb[d]['price'])
        u=sum(c)
        print('价格{}'.format(u))
    e=int(input('请输入选择:1.结算2.删除商品3.充值4.退出5.继续添加:'))
    if e==1:
        if a>u or a==u:
            a=a-u
            c.clear()
            b.clear()
            print('余额为{}'.format(a))
        if a<u:
            print('余额不足，请充值,或退出')
            h=u-a
            print('需充值{}元'.format(h))
            i=int(input('请选择:1.充值2.退出3.删除商品'))
            if i==1:
                g = input('请输入充值金额:')
                a = int(a) + int(g)
                print('当前余额{}元'.format(a))
            if i==2:
               continue
            if i==3:
                for i, j in enumerate(splb):
                    print(i, j)
                print(b)
                h = int(input('请输要删除的商品号:'))
                c.remove(splb[h]['price'])
                b.remove(splb[h])
                print(c)
                print(b)
    if e==2:
         for i, j in enumerate(splb):
            print(i, j)
         print(b)
         h=int(input('请输要删除的商品号:'))
         c.remove(splb[h]['price'])
         b.remove(splb[h])
         print(c)
         print(b)
    if e==3:
        g = input('请输入充值金额:')
        a = int(a) + int(g)
        print('当前余额{}元'.format(a))
    if e==4:
        print('再见')
        break

