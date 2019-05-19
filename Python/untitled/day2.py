#!/usr/bin/python
# -*- coding:utf-8 -*-
# a='hello,我叫{name},今年{age}岁'
# b=input('liu')
# c=input(20)
# d=a.format(name=b,age=20)
# print(d)
# a=('qwe',123,'rty')
# print(a)
# a=(12,34,54,12)
# b=a.count(12)
# print(b)
# a=[21,23,45,56,[1,2,3]]
# b=a.copy()
# a[-1].append(777)
# print(a)
# # print(b)
# for i in range(1,9):
#     if i==7:
#         continue
#     else:
#         print(i)
# else:
#     print('hello')
# a='      werr      '
# b=a.lstrip( )
# print(b)
# a='qwe  123'
# print(len(a))
# a=('qwe','123','rty')
# b=a.count('123')
# print(b)
# a=['123','qwe','555']
# a[1]=100
# print(a)
# a=[123,456,789]
# a.pop[0]
# print(a)
# 因数之和
# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if a==i:
#         print(a)
# #水仙花数
# for i in renge(100,1000):
#     b=i // 100
#     c=i // 10%10
#     d=i % 10
#     if b**3+c**3+d**3==i:
#         print(i)
# a= ['1','2','3']
# for i,j in enumerate(a):
#     print(i+1,j)
# b=int(input('>>>>>'))
# while b > 20 :
#      print ('hello')
#      b-=1
#一百以内的之和
# a=0;b=1
# while b<101:
#     a=a+b
#     b=b+1
# print(a)

#a= int(input('>>>>'))
# while True:
#     c=[]
#     a= input('请输入一组数据，以逗号隔开：')
#     if '-' in a:
#       break
#     else:
#        b=a.split(',')
#        for i in b:
#           c.append(int(i))
#     d=sum(c)/len(c)
#     print('平均数为{}'.format(d))
#     for j in c:
#         if d > j:
#           print('低于平均数的有{}'.format(j))
#去重
# a=[1,1,1,2,3]
# B=[]
# for i in a:
#     if  i  not  in B:
#         B.append(i)
# print(B)
#冒泡排序
# a=input('>>>:')
# b=a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
#             print(b)
# print(b)
#冒泡排序
# a=[8,6,4,2,1]
# for i in range(1,len(a)):
#     for j in range(0,len(a)-1):
#         if int(a[j]) > int(a[j+1]):
#             a[j],a[j+1]=a[j+1],a[j]
#             print(a)
# print(a)
# a=[1,2,3,1,4,2]
# b=[]
# for i in a:
#   if i not in b:
#        b.append(i)
# print(b)
# a=input('>>>>:')
# b=a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
#             print(b)
# print(b)
# a=4
# def xx():
#     global a
#     a=3
#     print(a)
# xx()
# print(a)
# a=[1,3,2,5]
# a.append(100)
# print(a)
# a.insert(0,10)
#print(a)
# a=int(input('>>>'))
# b=[]
# for i in a:
#   if i not in b:
#        b.append(i)
# print(b)
# a='12345'
# b=0
# while True:
#     if str(b)==a:
#         print(b)
#         break
#     b+=1
# a='1234'
# 1*(10**3)+2*(10**2)
# a=a[::-1]
# print(a)
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b=b+j*10**i
#             #  j*10**(len(a)-1-i)
# print(b)
# a= [i for i in range(10) if i >7]
# print(a)


# a=['{}*{}.format(i,j,i*j)' for i in range(1,10) for j in range(1,i+1)]
# print(a)]
# f=open('a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,1+i):
#       f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')
# f.close()

# f=open('a.txt','a',encoding='utf-8')
# f.write('qwe')
# f.close()
# f=open('a.txt','wb')
# print(f.read())
# f.close()
# f=open('b.txt','a')
#         if a[x] > a[y] :
#             a[x],a[y]=a[y],a[x]
# print(a)
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(1,len(a)):
#    for y in range(0,len(a)-1):
#        if a[y] > a[y+1]:
#            a[y],a[y+1]=a[y+1],a[y]
# print(a)
# a=input('>>>：')
# b=a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1):
#         if int(b[j])>int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
#
# print(b)
# a=input('>>>')
# for i in range(len(a)-1):
#     if a[i] != a   [-i-1]:
#         print('不是回文字符串')
#         break
# else:
#  print('是回文字符串')
# for i in range(3):
#   print('hello')
# 0到任意数的和
# def qwe(b):
#     a=0
#     for i in range(1,b+1):
#      a+=i
#     return a
# a=qwe(100)
# print(a)
# a=lambda x:x+2
# if __name__ =='__main__':
#     print('hello')
#空行的个数
# with open('a.txt','r',encoding='utf-8')as f:
#     a=f.readlines( )
#
# b=len(a)
# for i in a:
#     if i.startswith('#') or i =='\n':
#         b-=1
# print(b)
#找出第一大和第二大的数
# a=[1,3,1,5,3,7,5,8]
# b=a.copy()
# b=list(set(b))
# print(b)
# b.sort()
# for i in a:
#     if i==b[-1] or i==b[-2]:
#         print(i)
a= int(input('输入你的人民币：'))
b =['直升飞机:1399','魔幻手机:9999','智能电脑:888','巴姆雷特:99999','航空母舰:88888','真爱戒指:1314520']
d =[]
z = 1
while z > 0:
    while z > 0:
        print('商品区')
        print('账户余额{}'.format(a))
        print()
        for x,y in enumerate(b):
            print(x+1,y)
        print()
        c =int(input( '(输入序号加入购物车),(110退出),(0进入购物车)：'))
        if c == 110:
            break
        elif c > len(b):
            print('输入错误，请重新输入')
        elif c > 0:
            print('已加入购物车:{}'.format(b[c - 1]))
            d.append(b[c - 1])
        elif c == 0:
            while z == 1:
                print()
                print('账户余额:{}'.format(a),       '(充值110)')
                print ('    购物车')
                for i,j in enumerate (d):
                    print(i+1,j)
                e = int(input('(移除商品输入序号),(结算0),(回到商品区1001)'))
                if e == 1001:
                    break
                elif e == 110:
                    o = int(input('请输入要充值金额'))
                    a +=o
                elif e == 0:
                    n=[]
                    for A in d:
                        m = A.split(':')[1]
                        n.append(int(m))
                    f = sum(n)
                    if f <= a:
                        a -=f
                        print('购买成功{},剩余{}'.format(d, a))
                        d.clear()
                        continue
                    elif f > a:
                        print('余额不足,剩余{}，请充值'.format(a) )
                        p = int(input('充值请输入1，不充值输入0：'))
                        if p == 1:
                            g = int(input('请输入充值金额'))
                            a +=g
                            print('充值{}成功'.format(g))
                        else:
                            continue
                elif e > len(d):
                    print('输入错误！！！！请重新输入！！！')
                else:
                    print(d)
                    print('把{}移除购物车'.format(d[e-1]) )
                    d.pop(e-1)
    if c == 110:
        print('余额剩余{}，欢迎下次再来'.format(a))
        break