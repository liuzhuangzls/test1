
#!/usr/bin/python
# -*- coding:utf-8 -*-
# 自带的库，是与操作系统互交的
# 通过os模块来控制操作系统
# import os
#删除文件
#os.remove('文件名')
#执行windows命令
# b = os.popen('ip地址')
# print(b.read())
# 获取当前所在的位置
# print(os.getcwd())
#切换目录
# os.chdir(r'D:')
# print(os.getcwd())
#获取当前文件夹下面的文件
# a=(os.listdir('.'))
# for i in a:
#     if '.py' in i:
#         print(i)
# #将文件与路径分隔开 path.sqlit()
# a=os.path.split('‪C:\Users\lz\Desktop\d.txt')
# print(a)
# 将带有文件的后缀名与路径分隔开
# a=os.path.splittext()

# 判断文件是否是个目录
# a=os.path .isdir('.idea')
# print(a)


# 判断文件件是否是个普通文件
# a=os.path.isfile('b.txt')
# print(a)
# # 创建文件夹
# os.mkdir('aaa')
#创建递归文件夹
# os.makedirs('aaa/bbb/ccc')
# 删除空文件夹
# os.rmdir('')
# 删除空递归文件夹
# os.removedirs('')

# 包和模块的别
# 模块是：一个点py的文件，封装的是代码。
# 包是：一个目录，封装的是模块，必须含有__init__.py文件
#面向对象和面向过程的区别
# 面向过程;一步一步实现解决问题的步骤。性能高，不易维护，不易扩展
# 面向对象;将函数分类封装，是开发更高效，易扩展，易维护，性能低
# 封装ssh协议 可实现远程控制
# import paramiko
# #创建一个远程客户端
# ssh123=paramiko.SSHClient()
# #跳过验证，不到know_hosts文件中去查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #连接主机
# ssh123.connect(hostname='192.168.2.225',port=22,username='root',password='123456')
# #执行命令
# # 执行的命令 stuin
# # 执行的结果 stuout
# # 执行的报错 stuerr
# stuin,stuout,stuerr=ssh123.exec_command('ls -al')
# print(stuout.read().decode())
# # 断开连接
# # ssh123.close()
# # while True:
# #     a=input('>>>')
# #     if a==exit:
# #         break
# #     elif 'stuout' in a:
# # #传输文件
# # #建立一个传输通道
# ssh123=paramiko.Transport(('192.168.2.225',22))
# # #连接主机
# ssh123.connect(username='root',password='123456')
# # #创建一个sftp的客户端
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# # #从Linux下载文件到Windows
# # #要下载的文件，存储的本地位置
# # sftp.get('anaconda-ks.cfg','anaconda-ks.cfg')
# #从Windows上上传文件到Linux
# sftp.put('day1.py','/home/')
# #如果需要文件路径 需要加r



#发送邮件
# import smtplib #封装了SMTP协议
# import email.mime.multipart #处理邮件中的组成部分
# import email.mime.text #处理邮件中的中正文
# #发件人
# fr='liuzhuangzls@163.com'
# #收件人
# res='1746147518@qq.com'
# #服务器
# server='smtp.163.com'
# #授权码 授予登录客户端的授权码
# passwd='lz123456'
# # while True:
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# #给邮箱添加一个发件人
# message['From']=fr
# #添加一个收件人
# message['T0']=res
# #添加主题
# message['subject']='像极了爱情'
# text="。 \n守候是最永恒的承诺。"
# txt=email.mime.text.MIMEText(text)
# message.attach(txt)

# #定义一个服务器
# smtp123=smtplib.SMTP_SSL(server,465)
#
# #登录服务器
# smtp123.login(fr,passwd)
# #发送邮件
# smtp123.sendmail(fr,res,message.as_string())


# # 添加附件
# att2 = email.mime.text.MIMEText(open(r'C:\Users\lz\Desktop\379d50f8cb3846fa87351de5ebd32249!400x400.jpeg', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
# ## 头部字段
# message.attach(att2)
# message.attach(att2)
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(fr,passwd)
# smtp123.sendmail(fr,res,message.as_string())
import socket
# s=socket.socket()
# s.connect(('192.168.2.126',7777))
# while True:
#     a=input('>')
#     smg='{}'.format(a)
#     s.send(smg.encode('utf-8'))
#     reg=s.recv(1024)
#     print(reg.decode('utf-8'))

#
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #不需要建立连接
# host=('192.168.2.126',9999)
# msg='你好'
# s.sendto(msg.encode('utf-8'),host)
# reg=s.recv(1024)
# print(reg.decode('utf-8'))
# s.close()

