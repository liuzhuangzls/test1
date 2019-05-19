#!/usr/bin/python
# -*- coding:utf-8 -*-
#爬取：任何资源为html文件。静态网页
#动态网页：资源不在HTML文件中，实时动态更新。
#加载网页资源 浏览器调试工具
# #JavaScript  ajax
# # {json}
# import requests
# import json #轻量级的数据传输格式 Python 不认识json数据，
# url= 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=3&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13&city=410200&geoobj=114.296488|34.769458|114.434539|34.81458&keywords=洗浴中心'
# res=requests.get(url)
# qwe=res.text
# asd=json.loads(qwe)
#  #将json格式转换成字典
# # qwe=json.dumps(asd)
#  #将字典转换为json
# print((asd['data']['poi_list'][0]['name']))


# 授权grant all privileges on *.* to root@"%" identified by "123456";
#flush privileges;
#iptables -F
#Python连接数据库
# #connect 连接数据库
# import pymysql
# conn=pymysql.connect(host='192.168.2.225',port=3306,user='root',passwd='123456')
# #创建游标 类似于vim里面的光标
# abc=conn.cursor()
#执行SQL语句
# abc.execute('create database python_tast;')
# #fetchall 获取上一个SQL语句的结果
# a=abc.fetchall()
# print(a)
# abc.execute('use python_tast;')
# # abc.execute('create table py_tast(姓名 char(255),年龄 int,性别 char(225));')
# # abc.execute('insert into py_tast values("小明",25,"男"),("小强",20,"男"),("小花",19,"女");')
# #循环添加
# # for i in range(100):
# #     abc.execute('insert into py_tast values("{}","{}","{}");'.format("张三",20,"男"))
# abc.execute('select * from py_tast;')
# #提交
# conn.commit()
# #获取上一个SQL语句的结果，默认只获取结果中第一个数据,可传入一个数字() 数字就是获取相应的多少条数据。
# a=abc.fetchmany(10)
# #每次只获取一条结果，本身有迭代的功能
# a=abc.fetchone()#读取第一行
# b=abc.fetchone()#读取第二行
# print(a)
#
# #断开连接
# conn.close()
# while True:
#     a=input('>>>')
#     if a=='exit':
#         break
#     elif 'show' in a:
#         abc.execute('{}'.format(a))
#         print(abc.fetchall())
#     else:
#         abc.execute('{}'.format(a))
#     try:
#         while 'use' in a:
#             b=input('>>>')
#             if b=='exit':
#                 break
#             elif 'show' in b or 'select' in a or 'desc' in a:
#                 abc.execute('{}'.format(b))
#                 print(abc.fetchall())
#             else:
#                 abc.execute('{}'.format(b))
#     except Exception as e:
#         print(e)
#         continue
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



#动态爬取
import xlwt
import xlrd
import requests
import json
from xlutils.copy import copy
class zhilian(object):
    def qingqiu(self,page):
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        url='https://fe-api.zhaopin.com/c/i/sou/page-title?start=90&pageSize=90&cityId=765&areaId=2037&businessarea=%7B%7D&industry=&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=-1&sortType=&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&bj=&sj=&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22765%22,%22re%22:%222037%22,%22sf%22:%220%22,%22st%22:%220%22,%22kw%22:%22%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88%22,%22kt%22:%223%22%7D&=0&companyNo=&companyName=&_v=0.27907016&x-zp-page-request-id=7fab32cb337247098d0f8f67bfb7abae-1554428729590-708994'.format(90*page)
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,abc):
        quanbu=[]
        for i in range(90):
            a=[]
            aa=json.loads(abc)
            name=aa['data']['results'][i]['company']['name'];a.append(name)
            city=aa['data']['results'][i]['city']['display'];a.append(city)
            jobname=aa['data']['results'][i]['jobName'];a.append(jobname)
            salary=aa['data']['results'][i]['salary'];a.append(salary)
            edulevel=aa['data']['results'][i]['eduLevel']['name'];a.append(edulevel)
            workingexp=aa['data']['results'][i]['workingExp']['name'];a.append(workingexp)
            quanbu.append(a)
        return quanbu
    def save(self,quanbu):
        try:
            f=xlrd.open_workbook('ccc.xls')
            new_f=copy(f)
            new_sheet = new_f.get_sheet(0)
            read = f.sheets()[0]
            hang = read.nrows
            hang1 = hang
            for i in range(len(quanbu)):
                new_sheet.write(hang1, 0, quanbu[i][0])
                new_sheet.write(hang1, 1, quanbu[i][1])
                new_sheet.write(hang1, 2, quanbu[i][2])
                new_sheet.write(hang1, 3, quanbu[i][3])
                new_sheet.write(hang1, 4, quanbu[i][4])
                new_sheet.write(hang1, 5, quanbu[i][5])
                hang1 += 1
            new_f.save('ccc.xls')
        except:
            f=xlwt.Workbook(encoding='utf-8')
            sheet= f.add_sheet("智联")
            sheet.write(0,0,"公司名")
            sheet.write(0,1,"所在地")
            sheet.write(0,2,"工作岗位")
            sheet.write(0,3,"薪资")
            sheet.write(0,4,"学历")
            sheet.write(0,5,"工作经验")
            for i in range(1,len(quanbu)):
                sheet.write(i, 0, quanbu[i][0])
                sheet.write(i, 1, quanbu[i][1])
                sheet.write(i, 2, quanbu[i][2])
                sheet.write(i, 3, quanbu[i][3])
                sheet.write(i, 4, quanbu[i][4])
                sheet.write(i, 5, quanbu[i][5])
            f.save('ccc.xls')
a=zhilian()
for i in range(3):
    c=a.qingqiu(i)
    # print(a.guolv(c))
    quanbu=a.guolv(c)
    a.save(quanbu)


    # f= xlrd.open_workbook('cc.xls')
    # new_f = copy(f)
    # new_sheet = new_f.get_sheet(0)
    # read = f.sheets()[0]
    # hang = read.nrows
    # hang1 = hang
    # for i in range(len(quanbu)):
    #     new_sheet.write(hang1,0,quanbu[i][0])
    #     new_sheet.write(hang1, 1, quanbu[i][1])
    #     new_sheet.write(hang1, 2, quanbu[i][2])
    #     new_sheet.write(hang1, 3, quanbu[i][3])
    #     new_sheet.write(hang1, 4, quanbu[i][4])
    #     new_sheet.write(hang1, 5, quanbu[i][5])
    #     hang1+=1
    # new_f.save('cc.xls')
