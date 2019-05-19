#!/usr/bin/python
# -*- coding:utf-8 -*-
import xlrd
class Shuju():
    def shuju(self):
        shu=[]
        f=xlrd.open_workbook(r'E:\PycharmProjects\untitled\interface_test\data\aaa.xls')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(hang):
            b=sheet.row_values(i)
            shu.append(b)
        return shu
