# !/usr/bin/python
# -*- coding:utf-8 -*-
#!/usr/bin/python
# -*- coding:utf-8 -*-
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('aaa.xls')
# f.save('aaa.xls')
# import requests
# # # import json
# import unittest
# class main(unittest.TestCase):
#     def denglu(self,user,password):
#         url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#         payload = "{\r\n    \"phone\":%d,\r\n    \"password\":%d,\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(user,password)
#         headers = {
#             'Content-Type': "application/json",
#             'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#             'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#             'Language': "zh_CN",
#             'APIVersion': "3.0",
#             'touck': "e2173eab53474af688d759cade27f8cd",
#             'cache-control': "no-cache",
#             'Postman-Token': "0c38c9b0-9c4b-4761-9927-e2998cd4f003"
#             }
#
#         response = requests.request("POST", url, data=payload, headers=headers)


# print(response.text)

# res=response.text
#         res=response.json()
#         return res
# with open('c.txt','r',encoding='utf-8') as f:
#     for i in range(len('c.txt')):
#         hang=f.readline()
#         shuju=hang.strip()
#         shuju1=shuju.split(',')
#         print(shuju1)


# msg=json.loads(res)
# if res['code']==0:
#     print("qwe")


# class qwe(unittest.TestCase):
    #执行每个测试用例前执行一次
    # def setUp(self):
    #     print('开始')
#     def test_1(self):
#         aa=self.denglu(15993835273,111111)
#         self.assertEqual(aa['code'],0)
# def test_1(self):
#     aa=self.denglu(int(a[0][0],a[0][0]))
#     self.assertEqual(aa['code'],0)
# def tast_2(self):
#     for i in range(10):
#         bb=self.denglu(int(a[i][0],a[i][0]))
#         self.assertNotEqual(bb['code'],0)
#
#
#     def test_2(self):
#         bb=self.denglu(15993835273,11234)
#         self.assertNotEqual(bb['code'],0)
#     def test_3(self):
#         cc=self.denglu(15993835277,111111)
#         self.assertNotEqual(cc['code'],0)
#
#         # 执行每个测试用例后执行一次
#     # def tearDown(self):
#     #     print('结束')
# if __name__== '__main__':
#     #同一执行测试
#     unittest.main()


# # class fff(object):
# #     def __init__(self,name):
# #         self.name=name
# #         print(name)
# #     def kk(self,age,name):
# #         print(age)
# #         print(name)
# # qwe=fff('长得帅')
# # qwe.kk(21,'长得帅那')
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('py_ttt')
# f.save('sss.xls')

import xlrd
import unittest
import requests
def shuju():
    shuj=[]
    f=xlrd.open_workbook('sss.xls')
    sheet=f.sheets()[0]
    hang=sheet.nrows
    for i in range(hang):
        b=sheet.row_values(i)
        shuj.append(b)
    return shuj

class qwe(unittest.TestCase):
    data=shuju()
    def dizhi(self,city):
            url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
            querystring = {"filterInput":"{}".format(city)}
            payload = ""
            headers = {
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'Accept-Encoding': "gzip, deflate",
                'Accept-Language': "zh-CN,zh;q=0.9",
                'Cache-Control': "max-age=0",
                'Connection': "keep-alive",
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "313c4384-af1f-414d-8857-47ca1a152653"
                }

            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            print(response.text)
            res=response.json()
            return res
    def test_1(self):
        a=self.dizhi(self.data[0])
        self.assertEqual(a['code'],0)
if __name__== '__main__':
    unittest.main()
