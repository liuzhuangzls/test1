#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from interface_test.data.duqu import Shuju
class qwe():
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

        res=response.json()
        return res


