#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from xuexiao.data1.duqu import zxc
class xuex():
    def chaxun(self,city):
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
            'Postman-Token': "f0b2524d-8237-4a50-9bdc-9f57133d2eff"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        # print(response.text)
        res=response.json()
        # print(res)
        return res
# a = zxc().qq()
# xuex().chaxun(a[0][0])