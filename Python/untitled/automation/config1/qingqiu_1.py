#!/usr/bin/python
# -*- coding:utf-8 -*-
from interface_test.jiekou_test.test_denglu import qwe
import requests
class asd():
    def abc(self,aa):

        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = {"accountGuid": "{}".format(aa['data']['userInfo']['accountGuid']),
                       "targetUserGuid": "{}".format(aa['data']['userInfo']['accountGuid'])}

        payload = ""
        headers = {
                      'Content-Type': "application/json",
                      'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
                  'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
        'Language': "zh_CN",
        'APIVersion': "3.0",
        'AccessToken': "{}".format(aa['data']['accessToken']),
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "32b731d9-4e27-4653-adb2-36f97e817e72,29d078d7-b355-4186-9f21-680892295bb6",
        'Host': "120.132.8.33:9000",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        res=response.json()
        return res
# print(asd().abc(qwe().test_1()))