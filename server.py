# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:06:55 2019

@author: qizhiliu
"""

import socket
import sys
from _thread import *


#绑定地址
#设置监听
host = ""
port = 9999

result=[]
with open('students.txt','r', encoding="utf-8") as f:
	for line in f:
		result.append(list(line.strip('\n').split('\t')))
value = result
def return_message(value,strData,search):
    i = 3
    B=''
    if strData == '序号':
        i = 0
        search=search
    elif strData == '学号':
        i = 1
        search=search
    elif strData == '姓名':
        i = 2
        search=search
    b=0
    c = []     
    for a in value:
        b+=1                
        if search in a[i]:
            c.append(a)            
    B = str(c)
    if b ==0:
        print('无查询结果')
        B='无查询结果'
    return B
#创建一个socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #bind the (host,port)
    server.bind((host, port))
    print ("server bind success")
except(socket.error,msg):
    print ('binding failed,error code:', str(msg[0]), 'message', msg)
    sys.exit()

server.listen(11)
print ("server is serving on port", port)





def Processing(accp):
    client_socket, address = accp
    #while循环是为了让对话持续
    while True:
	     #接收客户端的请求
        recvmsg = client_socket.recv(1024)        
        #把接收到的数据进行解码
        strData = recvmsg.decode("utf-8")
        print( "(service from port:%s)"%address[-1],strData," acceped")
        #设置退出条件
        print(strData)
        if strData == 'q':
            print( "(service from port:%s)"%address[-1],'break')
            break
        elif strData == '序号':
            msge = '查询的序号为：'
        elif strData == '学号':
            msge = '查询的学号为：'
        elif strData == '姓名':
            msge = '查询的姓名为：'
        print("接收: %s" %strData)
        #输入
        msge = msge
        #发送数据，需要进行编码
        client_socket.send(msge.encode("utf-8"))
        print('发送过程已进行')
        recvmsg_1 = client_socket.recv(1024)
        strData_1 = recvmsg_1.decode("utf-8")
        print("接收: %s" %strData_1)
        B = return_message(value,strData,strData_1)
        print('查询结果：%s'%B)
        client_socket.send(B.encode("utf-8"))
        print('发送过程已进行')
    client_socket.close()

        
        
while True:
    #server.accept()返回一个元组, 元素1为客户端的socket对象, 元素2为客户端的地址(ip地址，端口号)
    accp = server.accept()
    #start a new thread to accept the data
    start_new_thread(Processing, (accp,))
#关闭服务器端
server.close()
