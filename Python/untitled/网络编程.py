#!/usr/bin/python
# -*- coding:utf-8 -*-
#socket 简单

import socket
# #创建一个套接字，一个有发送接收能力的一个对象
# #默认使用tcp
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.2.126',7777))
# s.listen(3)
# while True:
#     a=input('>')
#     client,addr=s.accept()
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))
#     reg='{}'.format(a)
#     client.send(reg.encode('utf-8'))


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.2.126',9999))
while True:
    client,addr=s.recvfrom(1024)
    #客户端的请求数据
    #客户端的ip和端口号
    print(client.decode('utf-8'))
    msg='hello'
    s.sendto(msg.encode('utf-8'),addr)




