#!/usr/bin/python
# -*- coding:utf-8 -*-
#从TXT中读取写入到excel中
# import xlwt
# with open(r'c:\Users\lz\Desktop\c.txt','r',encoding='utf-8') as f:
#  a=f.read()
# ff=xlwt.Workbook()
# sheet =ff.add_sheet('txt.shuju')
# for i in range(len(a)):
#     k=a[i].split(',')
#     print(k)
#     for j in range(len(k)):
#      sheet.write(i,j,k[j])
# ff.save('b.xls')
#从TXT中读取写入到excel中
# import  xlwt
# with open(r'c:\Users\lz\Desktop\d.txt','r',encoding='utf-8-sig') as f:
#  a=f.read()
#  b=a.split()
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('txt.sj')
# for i in range(len(b)):
#     k=b[i].split(',')
#     for j in range(len(k)):
#         sheet.write(i,j,k[j])
# ff.save('c.xls')
#
# import xlwt
# with open('d.txt','r',encoding='utf-8-sig') as f:
#     a=f.read()
#     b=a.split()
# ff=xlwt.Workbook(encoding='utf-8')
# sheet=ff.add_sheet('txt.shuju')
# for i in range(len(b)):
#     k=b[i].split(',')
#     for j in range(len(k)):
#         sheet.write(i,j,k[j])
# ff.save('c.xls')


# with open('d.txt','r',encoding='utf-8-sig') as f:
#     a=f.read()
#     print(len(a))

import pymysql
with open('a.txt','r',encoding='utf-8') as f:
    for i in range(len(f)):
        a=f.readline()
        b=len(a)
        conn = pymysql.connect(host="192.168.2.161", port=3306, user='root', password='123456')
        qwe = conn.cursor()
        qwe.execute('use qwe;')
        qwe.execute('create table zyq(我 char(10),你 char(10),他 char(10));')

        qwe.execute('insert into zyq values("{}","{}","{}");'.format(a[0],a[1],a[2]))
        conn.commit()
        qwe.execute('select * from zyq')
        c = qwe.fetchall()
        print(c)
        conn.close()

import pymysql
with open('a.txt','r',encoding='utf-8') as f:
    a=f.read()
    a = a.split('\n')
conn = pymysql.connect(host="192.168.2.161", port=3306, user='root', password='123456')
qwe = conn.cursor()
qwe.execute('use qwe;')
qwe.execute('create table zyq(招呼 char(10),表白 char(10),哼哼 char(10));')
for i in a:
    i = i.split('，')
    qwe.execute('insert into zyq values("{}","{}","{}");'.format(i[0],i[1],i[2]))






