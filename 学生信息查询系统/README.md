## 计算机网络练手小项目
### 基于socket的学生信息查询系统

#### 一、项目目标
此项目主要实现的是基于socket设计的客户端client和服务端server程序，实现客户端的查询功能，比如序号，序号或者姓名。根据查询的方式我们实现了模糊查询，也就是当我们想要查询“吴越明”的成绩，我们仅输入“越明”也可以查询到吴越明的成绩。而且并发数量不少于10个。

#### 二、思路及方案
Socket又称为“套接字”，应用程序通常通过“套接字”向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。本次程序设计主要使用的是python 使用了python自带的socket库和_thread库。Scoket库主要实现的套接字的功能，_thread库主要实现的是多线程的功能。
<B>主要使用到的函数及其功能：</B>
<I>s.bind()</I> 
绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。 
<I>s.listen() </I>
开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。 
<I>s.accept() </I>
被动接受TCP客户端连接,(阻塞式)等待连接的到来. 
<B>客户端套接字: </B>
<I>s.connect() </I>
主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。 
<I>s.recv()</I> 
接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。 
<I>s.send()</I> 
发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。 
<I>s.close()</I> 
关闭套接字。

#### 三、实现

<B>首先是服务端的实现:</B>
我们要先设置端口号和IP地址。
```python
host = ""
port = 9999
```
host即为IP地址，这里使用空字符串则表示为使用本机的IP地址。
然后我们需要创建一个socket对象：
```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
其中，AF_INET是套接字家族，SOCK_STREAM是面向连接的套接字类型。
然后我们将地址绑定到socket套接字上。
```python
try:
    #bind the (host,port)
    server.bind((host, port))
    print ("server bind success")
except(socket.error,msg):
    print ('binding failed,error code:', str(msg[0]), 'message', msg)
    sys.exit()
```
然后我们需要设置TCP监听数。
```python
server.listen(11)
print ("server is serving on port", port)
```
这个监听数是在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，本项目意在实现能够至少实现10个线程的连接，所以将监听数设置为了11。

<B>接下来是客户端的设置:</B>
首先是创造socket对象：
```python

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
然后是使用下述命令与服务端连接：
```python
host = "192.165.72.1" #服务端IP地址（要保证能ping通，否则连接失败）
port = 9999
#连接服务端
client.connect((host, port))
```
连接查询过程：
```python
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
```
