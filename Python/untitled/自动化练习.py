# #!/usr/bin/python
# # -*- coding:utf-8 -*-
import requests
import unittest
import xlrd
from src.testcase import HTMLTestRunner


def shuju():
    shuj=[]
    f=xlrd.open_workbook('aaa.xls')
    sheet=f.sheets()[0]
    shu=sheet.nrows
    for i in range(shu):
        b=sheet.row_values(i)
        shuj.append(b)
    return shuj
class qwe(unittest.TestCase):
    data=shuju()
    def denglu(self,user,password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = "{\r\n    \"phone\":%d,\r\n    \"password\":%d,\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(user,password)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'touck': "e2173eab53474af688d759cade27f8cd",
            'cache-control': "no-cache",
            'Postman-Token': "0c38c9b0-9c4b-4761-9927-e2998cd4f003"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        res=response.json()
        return res
    def test_1(self):
        aa = self.denglu(int(self.data[0][0]), int(self.data[0][1]))
        self.assertEqual(aa['code'], 0)

    def test_2(self):
        for i in range(1,len(self.data)):
            bb = self.denglu(int(self.data[i][0]), int(self.data[i][1]))
            self.assertNotEqual(bb['code'], 0)

if __name__== '__main__':
    # unittest.main()
    # #创建一个测试套件
    suit=unittest.TestSuite()
    #将测试用例添加到测试套件中
    # suit.addTest(qwe('test_1'))
    # suit.addTest(qwe('test_2'))
    #将qwe类中所有test开头的函数都添加到测试套件中
    suit.addTest(unittest.makeSuite(qwe))
    #打开一个空文件
    f=open('abc.html','wb')
    #定义一个测试报告的信息
    runner= HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='刘壮', description='结果如下')
    runner.run(suit)
    f.close()


