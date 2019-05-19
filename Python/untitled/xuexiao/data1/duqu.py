#!/usr/bin/python
# -*- coding:utf-8 -*-
import xlrd
class zxc():
    def qq(self):
        f=xlrd.open_workbook(r'E:\PycharmProjects\untitled\xuexiao\data1\diqu.xls')
        sheet=f.sheets()[0]
        aa=[sheet.row_values(i) for i in range(sheet.nrows)]
        return aa

# print(zxc().qq())