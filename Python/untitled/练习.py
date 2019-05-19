#!/usr/bin/python
# -*- coding:utf-8 -*-
# import xlrd
# import pymysql
# with open(r'a.xls', 'r',encoding='utf-8') as f:
#     a=f.read()
#     print(a)
# ff=xlrd.open_workbook('cc.xls')
# sheet=ff.sheets()[0]
# conn=pymysql.connect(host='192.168.2.225',port='3306',user='root',passwd='123456')
# abc=conn.cursor()
# abc.execute('use test1')
# abc.execute('creat table quanbu(w char(20),c char(20),q char(20),t int(20))')
# q=sheet.nrows
# for i in range(q):
#     b=sheet.row_value(i)
#     abc.execute('insert into quanbu value("{}"{}""{}"{}")'.format(b[0],b[1],b[2]))
import xlwt
import xlrd
import re
import requests
from xlutils.copy import copy
class boss(object):
    def qingqiu(self,page):
        head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url='https://www.zhipin.com/c101280600-p100301/b_%E7%A6%8F%E7%94%B0%E5%8C%BA/?page=2&ka=page-2'
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,abc):
        a=re.compile('target="_blank">(.*?)</a></h3>')
        aa=a.findall(abc)
        # print(aa)
        b=re.compile('<div class="job-title">(.*?)</div>')
        bb=b.findall(abc)
        # print(bb)
        c=re.compile('<div class="info-detail"></div>(.*?)<div class="info-company">',re.S)
        cc=c.findall(abc)
        neirong = []
        for i in cc:
            dd=re.compile('<p>(.*?)<em class="vline">',re.S)
            ddd = dd.findall(i)
            neirong.append(ddd[0])
        # print(neirong)
        quanbu=list(zip(aa,bb,neirong))
        print(quanbu)
        return quanbu
    def save(self,quanbu):
        f=xlwt.Workbook(encoding='utf-8')
        sheet=f.add_sheet('qwe')
        sheet.write(0,0,"公司名")
        sheet.write(0,1,"职位")
        sheet.write(0,2,"地区")
        for i in range(0,len(quanbu)):
            for j in range(len(quanbu[i])):
             sheet.write(i+1,j,quanbu[i][j])
        f.save('boss.xls')
tu=boss()
ab=tu.qingqiu(2)
a=tu.guolv(ab)
tu.save(a)












import xlwt
import xlrd
import re
import requests
from xlutils.copy import copy
class boss(object):
    def qingqiu(self,page):
        head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url='https://www.zhipin.com/c101280600-p100301/b_%E7%A6%8F%E7%94%B0%E5%8C%BA/?page={}&ka=page-2'.format(page)
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,abc):
        a=re.compile('target="_blank">(.*?)</a></h3>')
        aa=a.findall(abc)
        # print(aa)
        b=re.compile('<div class="job-title">(.*?)</div>')
        bb=b.findall(abc)
        # print(bb)
        c=re.compile('<div class="info-detail"></div>(.*?)<div class="info-company">',re.S)
        cc=c.findall(abc)
        neirong = []
        for i in cc:
            dd=re.compile('<p>(.*?)<em class="vline">',re.S)
            ddd = dd.findall(i)
            neirong.append(ddd[0])
        # print(neirong)
        quanbu=list(zip(aa,bb,neirong))
        print(quanbu)
        return quanbu
    def save(self,quanbu):
        try:
            f=xlrd.open_workbook('boss.xls')
            new_f=copy(f)
            sheet=new_f.get_sheet(0)
            hang=sheet.nrows
            hang1=hang
            for i in range(len(quanbu)):
                new_f.write(hang1,0,quanbu[i][0])
                new_f.write(hang1,1,quanbu[i][1])
                new_f.write(hang1,2,quanbu[i][2])
                new_f.save('boss.xls')

        except:

            f=xlwt.Workbook(encoding='utf-8')
            sheet=f.add_sheet('qwe')
            sheet.write(0,0,"公司名")
            sheet.write(0,1,"职位")
            sheet.write(0,2,"地区")
            for i in range(0,len(quanbu)):
                for j in range(len(quanbu[i])):
                 sheet.write(i+1,j,quanbu[i][j])
            f.save('boss.xls')
tu=boss()
for i in range(3):
    ab=tu.qingqiu(i)
    quanbu=tu.guolv(ab)
    # tu.save(a)
    f=xlrd.open_workbook('boss.xls')

    new_f=copy(f)

    sheet=new_f.get_sheet(0)
    sheet1=f.sheets()[0]
    hang=sheet1.nrows
    hang1=hang
    print(hang1)
    for i in range(len(quanbu)):
        sheet.write(hang1,0,quanbu[i][0])
        sheet.write(hang1,1,quanbu[i][1])
        sheet.write(hang1,2,quanbu[i][2])
        hang1+=1
    new_f.save('boss.xls')





