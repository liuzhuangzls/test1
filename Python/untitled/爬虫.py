#!/usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# # class 糗事(object):
# a='https://www.qiushibaike.com/text/page/{}/'.format(2)
# #发送请求
# oo={}
# b=requests.get(a)
# #读取接收相应1.text 字符串  2.content 以字节的方式去接收
# # c=b.content.decode('utf-8')
# #网页源代码
# c=b.content.decode('utf-8')
# d=re.compile('<div class="content">(.*?)</span>',re.S)
# f=d.findall(c)
# ff=[]
# for i in f:
#     i=i.replace('<span>','')
#     i=i.strip()
#     i=i.replace('<br/>','')
#     print(i)
#     ff.append(i)
# with open('c.txt','w',encoding='utf-8')as g:
#     for i in ff:
#         g.write(i+'\n')



# #对服务器造成压力
# 爬取文字内容和作者
# import requests
# import re
# # class 糗事(object):
# for k in range(1,6):
#  a='https://www.qiushibaike.com/text/page/{}/'.format(k)
# oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# b=requests.get(a,headers=oo)
#     #读取接收相应1.text 字符串  2.content 以字节的方式去接收
#     # c=b.content.decode('utf-8')
#     #网页源代码
# c=b.content.decode('utf-8')
# d=re.compile('<div class="content">(.*?)</span>',re.S)
# f=d.findall(c)
# print(f)
# dd=re.compile('<h2>(.*?)</h2>',re.S)
# fff=dd.findall(c)
# ff=[]
# ffff=[]
# for i in f:
#     i=i.replace('<span>','')
#     i=i.strip()
#     i=i.replace('<br/>','')
#     ff.append(i)
# for j in fff:
#     j=j.replace('\n','')
#     ffff.append(j)
# for x in range(len(ff)):
#     ff.insert(x*2,ffff[x])
# with open('a.txt','a',encoding='utf-8')as g:
#     for i in ff:
#      g.write(i+'\n')








#爬去图片和对应的文字
# import requests
# import re
# class Tupian(object):
#     def 发送请求(self,page):
#         url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari /537.36'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def 过滤(self,abc):
#         lianjie=[]
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items=patt.findall(abc)
#         print(items)
#         for i in items:
#             new_a=re.compile(r'<img src="(.*?)"')
#             aaa=new_a.findall(i)
#             lianjie.extend(aaa)
#         return lianjie
#     #保存的函数
#     def save(self,shu):
#         #图片是一个链接，需要请求图片的链接，将相应保存
#         for a,i in enumerate(shu):
#             # print('https:'+i)
#             res=requests.get('https:'+i)
#             #接收响应的结果只能用content
#             qq=res.content
#             with open('{}.jpg'.format(a),'wb') as f:
#                 f.write(qq)
#
# tu=Tupian()
# ab=tu.发送请求(1)
# sh=tu.过滤(ab)
# tu.save(sh)
# import requests
# import re
# class diany(object):
#     def qingqiu(self,a):
#         url='https://movie.douban.com/top250?start={}&filter='.format(25*i)
#         head={'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.86Safari/537.36'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         a=re.compile('<img width="100" alt="(.*?)"',re.S)
#         bb=a.findall(abc)
#         b=re.compile('src="(.*?)" class="">')
#         d=b.findall(abc)
#         e=dict(zip(bb,d))
#         return e
#     def save(self,shu):
#         for i,j in shu.items():
#             res=requests.get(j)
#             qq=res.content
#             with open('{}.jpg'.format(i),'wb') as f:
#                 f.write(qq)
# tu=diany()
# for i in range(1):
#     ab=tu.qingqiu(i)
#     e=tu.guolv(ab)
#     tu.save(e)
import smtplib
import email.mime.multipart
import email.mime.text
import pymysql
conn=pymysql.connect(host='192.168.2.225',port=3306,user='root',passwd='123456')
abc=conn.cursor()
abc.execute('create database text3;')
abc.execute('use text3 ')
abc.execute('create table shuju(`姓名` char(255),`性别` char(255),`年龄` char(255))')
for i in range(1,101):
    abc.execute('insert into shuju values("小强","男",20);')
    a=abc.fetchall()
    b=int(a[0][0])
    if b%100==0:
        break
    fr='liuzhuang@163.com'
    res='12345678@qq.com'
    server='smtp.163.com'
    passwd='123456'
    message=email.mime.multipart.MIMEMultipart()
    message['From']=fr
    message['To']=res
    message['subject']='zhuti'
    text='qwe'
    smtp123=smtplib.SMTP_SSL(server,465)
    smtp123.login(fr.passwd)
    smtp123.sendmail(fr,res,message.as_string())





