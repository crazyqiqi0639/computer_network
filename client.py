# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:08:18 2019

@author: qizhiliu
"""
import socket
#创建一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.165.72.1"
port = 9999
#连接服务端
client.connect((host, port))
while True:
    send_msg = input("请输入你选择的查询方式:")
    #设置退出条件

    send_msg = send_msg
    #发送数据，编码
    client.send(send_msg.encode("utf-8"))
    if send_msg == "q":
        break
    print('发送过程已进行')
    #接收服务端返回的数据
    msg = client.recv(1024)
    #解码
    send_msg_1=input(msg.decode("utf-8"))
    client.send(send_msg_1.encode("utf-8"))
    print('发送过程已进行')
    msg_1 = client.recv(1024)
    msg_1=msg_1.decode("utf-8")
    print(msg_1[1:-1])
#关闭客户端
client.close()
