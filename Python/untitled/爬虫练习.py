#!/usr/bin/python
# -*- coding:utf-8 -*-
# import pymysql
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import requests
# import re
# class diany(object):
#     def qingqiu(self,a):
#         url='https://movie.douban.com/top250?start={}&filter='.format(a)
#         head={'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.86Safari/537.36'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         ww=re.compile('<img width="100" alt="(.*?)"',re.S)
#         mingzi=ww.findall(abc)
#         c=re.compile('导演:(.*?)&nbsp;&nbsp;&nbsp;',re.S)
#         daoyan=c.findall(abc)
#         d=re.compile('<span class="inq">(.*?)</span>',re.S)
#         pingyu=d.findall(abc)
#         z=re.compile('property="v:average">(.*?)</span>',re.S)
#         pingfeng=z.findall(abc)
#         y = re.compile('<div class="star">(.*?)</div>', re.S)
#         pingjia = y.findall(abc)
#         www=[]
#         for t in pingjia:
#             tt=re.compile('<span>(.*?)</span>',re.S)
#             ttt=tt.findall(t)
#             www.append(ttt[0])
#         return list(zip(mingzi,daoyan,pingyu,pingfeng,www))
#     def shuju(self,a,b,c,d,e):
#         conn=pymysql.connect(host='192.168.2.225',port=3306,user='root',passwd='123456')
#         abc=conn.cursor()
#         abc.execute('use test1')
#         abc.execute('cerate table dianying(电影名 char(255),导演char(255),评语 char(255),评分 char(255),人数 char(255));))')
#         for i in range(len(a)):
#             abc.execute('insert into dianying values("{}","{}","{}","{}","{}");'.format(a[i][0],b[i][0],c[i][0],d[i][0],e[i][0]))
# tu=diany()


import smtplib
import email.mime.multipart
import email.mime.text
import pymysql
conn=pymysql.connect(host='192.168.2.225',port=3306,user='root',passwd='123456')
abc=conn.cursor()
abc.execute('create database text3;')
abc.execute('use text3 ')
abc.execute('create table shuju(`姓名` char(255),`性别` char(255),`年龄` char(255))')
# abc.execute('select count(*)from shuju;')
# a=abc.fetchall()
# print(a)

import xlwt
import xlrd
import pymysql
import os

with open ('c.txt','w+',encoding='utf-8') as f:
    for i in range (100):
        f.write('hello,word\n')
with open ('c.txt','r',encoding= 'utf-8') as po:
    a=po.readlines()
ff = xlwt .Workbook (encoding= 'utf-8')
sheet = ff.add_sheet('qqq')
for i in range (len(a )):
 sheet.write(i,0,a[i])
ff.save('c.xls')

fff = xlrd.open_workbook('c.xls')
sheet = fff.sheets()[0]
conn = pymysql.connect(host = '192.168.2.206',port= 3306,user='root',passwd='123456')
abc =conn .cursor()
abc.execute('create database qwe;')
abc.execute ('use qwe;')
abc.execute ('create table wenjian(wen char(255));')
q = sheet.nrows
for i in range(q):
        b =sheet.row_value(i)
        abc.execute ('insert into wenjian values("{}")'.format(b[0]) )


# abc.execute ('drop table wenjian ')
# os.remove('c.txt')
# os.remove('c.xls')



#字符串 数字 数字

# def shanchu(a,b,c):
#     q = len(a)
#     if b+c-1 >= q:
#         a=a[:b]
#     else:
#         w=a[:b]
#         e=a[b+c:]
#         a=w+e
#     return  a

#数据库导到Excel中
import xlwt
import pymysql
f =xlwt.Workbook (encoding= 'utf-8')
sheet =f.add_sheet('qwe')
conn = pymysql .connect(host='192.168.2.225',port = 3306,user = 'root',passwd= '123456')
abc = conn.cursor()
abc.execute('use text3;')
abc.execute('select  * from shuju;')
a = abc.fetchall()
# print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        sheet.write(i,j,a[i][j])
f.save('abc.xls')
f=xlwt.workbook(encoding='utf-8')
sheet=f.add_sheet('qwe')
conn=pymysql.connect(host='192.168.0.1',port='3306',user='root',passwd='112345')
abc=conn.cursor()
abc.execute('use text')
abc.execute('select * from shuju')
a=abc.fetchall()
for i in range(len(a)):
    for j in range(len(i)):
        sheet.write(i,j,a[i][j])
f.save(a.xls)

#Excel导到数据库
import pymysql
import xlrd
ff = xlrd.open_workbook('b.xls')
sheet = ff.sheets()[0]
a = sheet.nrows
conn = pymysql.connect(host='192.168.2.161',port=3306,user='root',password='123456')
qwe = conn.cursor()
qwe.execute('use qwe;')
qwe.execute('create table asd(电影名 char(20),导演 char(50),评分 char(10),评价 char(10));')
for i in range(1,a):
    i = sheet.row_values(i)
    qwe.execute('insert into asd values("{}","{}","{}","{}");'.format(i[0],i[1],i[2],i[3]))
conn.commit()
conn.close()




