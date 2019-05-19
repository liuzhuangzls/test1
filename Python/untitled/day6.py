#!/usr/bin/python
# -*- coding:utf-8 -*-
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# for i in range(30):
#  for j in range(30):
#   sheet.write(i,j,'{}'.format(i))
# f.save('a.xls')
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# # for i in range(30):
# #  for j in range(30):
# #   sheet.write(i,j,'{}'.format(i))
# for i in range(1,10):
#  for  j in range(1,i+1):
#   sheet.write(i-1,j-1,'{}*{}={}\t'.format(i,j,i*j))
# f.save('a.xls')
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# with open('c.txt','r') as f:
#     print(f.read())
# sheet.write()
# f.save('a.xls')
# import xlrd
# f= xlrd.open_workbook('a.xls')
# b=f.nsheets
# print(b)
# sheet=f.sheet_by_name('python_test')
# sheet=f.sheets()[0]
# b=sheet.row_values(1)
# print(b)
# c=sheet.nrows
# for i in range(c):
#     d=sheet.row_values(i)
#     print(d)
# c=sheet.nrows
# for i in range(c):
#     d=sheet.col_values(i)
#     print(d)
# c=sheet.ncols
# print(c)
# for i in range(3,8):
#     for j in range(2,4):
#       b=sheet.cell(i,j).value
# b=open(r'c:\Users\lz\Desktop\c.txt‪','r',encoding='utf-8')
# print(b.read())
# with open(r'c:\Users\lz\Desktop\c.txt','r') as f:
#  print(f.read())
# import xlrd
# f=xlrd.open_workbook('c.txt')
# with open(r'c:\Users\lz\Desktop\c.txt','r') as x:
#     import xlwt
#     f = xlwt.Workbook(encoding='utf-8')
#     sheet = f.add_sheet('插入数据')
#     c = x.read()
#     o = c.split('\n')
#     for i in range(len(o)):
#         a = o[i]
#         b = a.split('，')
#         for j in range(len(b)):
#             sheet.write(i,j,b[j])
#     f.save('a.xls')
#从TXT中读取写入到excel中
# import xlwt
# with open(r'c:\Users\lz\Desktop\c.txt','r') as f:
#    a=f.readlines()
# ff=xlwt.Workbook()
# print(a)
#    # a=f.readlines()
#    # print(a.split('\n'))
#    # b=a.split('\n')
#    # for i in a
# sheet =ff.add_sheet('txt.shuju')
# for i in range(len(a)):
#     k=a[i].split(',')
#     print(k)
#     for j in range(len(k)):
#      sheet.write(i,j,k[j])
# ff.save('a.xls')
#从excel中读取到a.txt中
# import xlrd
# # with open('a.txt','w',encoding='utf-8') as f:
# ff=xlrd.open_workbook('a.xls')
# sheet=ff.sheets()[0]
# b=sheet.nrows
# with open('c.txt','w',encoding='utf-8') as f:
#  for i in range(b):
#   i=sheet.row_values(i)
#   for j,k in enumerate(i):
#    if j==len(i)-1:
#        f.write(k)
#    else:
#        f.write(k+',')
#读取a.txt中以abc开头的
# with open('a.txt','r',encoding='utf-8-sig') as f:
#     a=f.readlines()
#     print(a)
#     # a=f.read()
#     # b=a.split()
#     for i in range(len(a)):
#         if a[i].startswith('abc'):
#             print(a[i])
#在c.txt中写入九九乘法表
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# # for i in range(30):
# #  for j in range(30):
# #   sheet.write(i,j,'{}'.format(i))
# for i in range(1,10):
#  for  j in range(1,i+1):
#   sheet.write(i-1,j-1,'{}*{}={}\t'.format(i,j,i*j))
# f.save('c.xls')


# def a(b,d):
#     c=0
#     for i in range(b,d+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#          c+=i
#     return c
# print(a(2,100))
#读取a.txt中带有abc的行
# with open('a.txt','r',encoding='utf-8-sig') as f:
#     a=f.readlines()
#     for i in range(len(a)):
#         if 'abc' in a[i]:
#          print(a[i])

#
# a=[2,3,4,5]
# b=[7,6,9,7]
# c=tuple(zip(a,b))
# print(c)
# #爬取豆瓣电影中电影名导演评分等保存到表格中
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
#     def save(self,pm):
#         try:
#             fff=xlrd.open_Workbook('h.xls')
#             sheet1=fff.sheets()[0]
#             num=sheet1.nrows
#             new_f=copy(fff)
#             sheet=new_f.get_sheet(0)
#             # num=num+1
#             for q,w,e,r,t in pm:
#                 sheet.write(num,0,q)
#                 sheet.write(num,1,w)
#                 sheet.write(num,2,e)
#                 sheet.write(num,3,r)
#                 sheet.write(num,4,t)
#                 num+=1
#             new_f.save('h.xls')
#         except:
#             f=xlwt.Workbook()
#             sheet=f.add_sheet('douban')
#             sheet.write(0,0,'片名')
#             sheet.write(0,1,'导演')
#             sheet.write(0,2,'评语')
#             sheet.write(0,3,'评分')
#             sheet.write(0,4,'评价人数')
#             i=1
#             for q,w,e,r,t in pm:
#                 sheet.write(i, 0, q)
#                 sheet.write(i, 1, w)
#                 sheet.write(i, 2, e)
#                 sheet.write(i, 3, r)
#                 sheet.write(i, 4, t)
#                 i=i+1
#                 f.save('h.xls')
# tu=diany()
# for i in range(0,25,25):
#     ab=tu.qingqiu(i)
#     e=tu.guolv(ab)
#     tu.save(e)
#爬取豆瓣电影中电影名导演评分等保存到表格中
import pymysql
import xlwt
import xlrd
from xlutils.copy import copy
import requests
import re
class diany(object):
    def qingqiu(self,a):
        url='https://movie.douban.com/top250?start={}&filter='.format(a)
        head={'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.86Safari/537.36'}
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,abc):
        ww=re.compile('<img width="100" alt="(.*?)"',re.S)
        mingzi=ww.findall(abc)
        c=re.compile('导演:(.*?)&nbsp;&nbsp;&nbsp;',re.S)
        daoyan=c.findall(abc)
        d=re.compile('<span class="inq">(.*?)</span>',re.S)
        pingyu=d.findall(abc)
        z=re.compile('property="v:average">(.*?)</span>',re.S)
        pingfeng=z.findall(abc)
        y = re.compile('<div class="star">(.*?)</div>', re.S)
        pingjia = y.findall(abc)
        www=[]
        for t in pingjia:
            tt=re.compile('<span>(.*?)</span>',re.S)
            ttt=tt.findall(t)
            www.append(ttt[0])
        return list(zip(mingzi,daoyan,pingyu,pingfeng,www))
    def save(self,pm):
        try:
            fff=xlrd.open_Workbook('h.xls')
            sheet1=fff.sheets()[0]
            num=sheet1.nrows
            new_f=copy(fff)
            sheet=new_f.get_sheet(0)
            # num=num+1
            for q,w,e,r,t in pm:
                sheet.write(num,0,q)
                sheet.write(num,1,w)
                sheet.write(num,2,e)
                sheet.write(num,3,r)
                sheet.write(num,4,t)
                num+=1
            new_f.save('h.xls')
        except:
            f=xlwt.Workbook()
            sheet=f.add_sheet('douban')
            sheet.write(0,0,'片名')
            sheet.write(0,1,'导演')
            sheet.write(0,2,'评语')
            sheet.write(0,3,'评分')
            sheet.write(0,4,'评价人数')
            i=1
            for q,w,e,r,t in pm:
                sheet.write(i, 0, q)
                sheet.write(i, 1, w)
                sheet.write(i, 2, e)
                sheet.write(i, 3, r)
                sheet.write(i, 4, t)
                i=i+1
            f.save('h.xls')
    def shuju(self,a,b,c,d,e):
        conn=pymysql.connect(host='192.168.2.225',port=3306,user='root',passwd='123456')
        abc=conn.cursor()
        abc.execute('use test1')
        abc.execute('cerate table dianying(电影名 char(255),导演char(255),评语 char(255),评分 char(255),人数 char(255));))')
        for i in range(len(a)):
            abc.execute('insert into dianying values("{}","{}","{}","{}","{}");'.format(a[i][0],b[i][0],c[i][0],d[i][0],e[i][0]))
tu=diany()
for i in range(0,25,25):
    ab=tu.qingqiu(i)
    e=tu.guolv(ab)
    # tu.shuju()
    # tu.save(e)
    q,w,e,r,t=tu.guolv(e)
    tu.save(q,w,e,r,t)




