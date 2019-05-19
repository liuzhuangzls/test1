#!/usr/bin/python
# -*- coding:utf-8 -*-
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
#函数传参求质数任意之和
# def xx(a,b):
#     c=0
#     for i in range(a,b):
#         for j in range(2,i+1):
#             if i%j==0:
#               break
#         if i == j:
#             c+=i
#     print(c)
# xx(2,100)
#函数传参求任意因数之和
# def xx(a,b):
#     c=0
#     for i in range(a,b):
#         d=0
#         for j in range(1,i):
#             if i%j==0:
#                 d+=j
#         if i==d:
#             c+=i
#     return c
# a=xx(1,100)
# print(a)
# def xx(a,b):
#     c=0
#     for i in range(a,b):
#         d=0
#         for j in range(1,i):
#             if i%j==0:
#                 d+=j
#         if i==d:
#             c+=i
#     return c
# a=xx(1,100)
# print(a)
#正则表达式
# import re
# a='qwe123qwfsahfshie'
#complie 编译，将[0-9]*编译成曾泽表达式语言
# p=re.compile('[0-9]{2,4}')
# p=re.compile('f(.*.)f')
#只匹配指定的内容给正则条件加括号
#
# print(p)
#findall 从某个地方查找所有符合正则的字符串
#如果有两个参数：1，正则条件 2，查找范围
# c=re.findall(p,a)
#c=re.findall('[0-9]{2,4}',a) 自带编译
# print(c)

#如果有一个参数的时候;1,查找的范围
# c=p.findall(a)
# print(c)
#贪婪模式 尽可能的匹配更多的内容
# a='qwe12q234q'
# p=re.compile('q(.*)q')
# c=p.findall(a)
# print(c)
# 非贪婪模式
# a='qwe12q234q'
# p=re.compile('q(.*?)q')
# c=p.findall(a)
# print(c)
#.是可以匹配字符 除换行符之外的
#re.S 给.加功能 可以匹配换行符在内的任意字符
# a='qwe\nqww12q23q'
# p=re.compile('q(.*?)q',re.S)
# c=p.findall(a)
# print(c)
# re.I 给条件加功能，不区分大小写
# a='qweQ12qweQ'
# p=re.compile('Q(.*?)Q',re.I)
# c=p.findall(a)
# print(c)
# import requests
# import re
# # class 糗事(object):
# for k in range(1,6):
#     a='https://www.zhipin.com/c101280600-p100301/?page={}&ka=page-{}'.format(k,k)
#     oo={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     b=requests.get(a,headers=oo)
#     c=b.content.decode('utf-8')
#     d=re.compile(' </h3>(.*?)</p>',re.S)
#     f=d.findall(c)
#     # print(f)
# # dd=re.compile('<h2>(.*)</h2>',re.S)
# # fff=dd.findall(c)
# ff=[]
# # ffff=[]
# for i in f:
#     i=i.replace('<em class="vline"></em>','')
#     # i=i.strip()
#     i=i.replace('<p>','')
#     i=i.replace('\n','')
#     ff.append(i)
#     print(ff)
# # for j in fff:
# #     j=j.replace('\n','')
# #     ffff.append(j)
# # for x in range(len(ff)):
# #     ff.insert(x*2,ffff[x])
# with open('a.xls','w',encoding='utf-8')as g:
#     for i in ff:
#         g.write(i+'\n')




# #豆瓣爬取电影名字和对应的图片
# import requests
# import re
# class diany(object):
#  def qingqiu(self,a):
#      url='https://movie.douban.com/top250?start={}&filter='.format(25*i)
#      head={'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.86Safari/537.36'}
#      res=requests.get(url,headers=head)
#      html=res.content.decode('utf-8')
#      return html
#  def guolv(self,abc):
#      mingzi=[]
#      tupian=[]
#      a=re.compile('<img width="100" alt="(.*?)"',re.S)
#      b=a.findall(abc)
#      c=re.compile('src="(.*?)" class="">')
#      d=c.findall(abc)
#      mingzi.extend(b)
#      tupian.extend(d)
#      # print(mingzi)
#      # print(tupian)
#      return mingzi,tupian
#  def save(self,mingzi,tupian):
#      for x,i in enumerate(tupian):
#          res=requests.get(i)
#          qq=res.content
#          z=mingzi[x]
#          with open('{}.jpg'.format(z),'ab') as f:
#              f.write(qq)
# tu=diany()
# for i in range(5):
#     ab=tu.qingqiu(i)
#     aaa,bbb = tu.guolv(ab)
#     tu.save(aaa,bbb)
#
# import requests
# import re
# import pymysql
# class douban(object):
#     def song(self,page):
#         url = "https://movie.douban.com/top250?start={}&filter=".format(page)
#         head = {'User-Agent':'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.86Safari/537.36'}
#         res = requests.get(url,headers=head)
#         html = res.content.decode("utf-8")
#         return html
#     def guo(self,aa):
#         patt = re.compile(r'<img width="100" alt="(.*?)"',re.S)
#         items = patt.findall(aa)
#         pat = re.compile(r'导演:(.*?)&nbsp;&nbsp;',re.S)
#         item = pat.findall(aa)
#         pa = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
#         ite = pa.findall(aa)
#         pp = re.compile(r'<span>(.*?)评价</span>')
#         it = pp.findall(aa)
#         return items,item,ite,it
#     def save(self,q,w,e,r):
#         conn = pymysql.connect(host= '192.168.2.225',port=3306,user='root',password='123456')
#         qwe =conn.cursor()
#         qwe.execute('use test;')
#         for i,j in enumerate(q):
#             qwe.execute('insert into douban values("{}","{}","{}","{}");'.format(j,w[i],e[i],r[i]))
# for i in range(0,25,25):
#     asd = douban()
#     a = asd.song(1)
#     m,n,b,v = asd.guo(a)
#     asd.save(m,n,b,v)
a=[1,[2],3,4,5,6]
# print(a[1][0])
b=[]
for i in range(len(a)):
    if i==1:
        continue
    b.append(a[i])
b.append(a[1][0])
b.sort()
print(b)







