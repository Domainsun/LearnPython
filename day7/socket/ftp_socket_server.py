import socket,os,hashlib
server=socket.socket()
server.bind(('localhost',9999))
server.listen()
while True:
    conn,addr=server.accept()
    while True:
        print('等待指令中...')
        data=conn.recv(1024)
        if not data:
            print('客户端已经断开')
            break
        cmd,file_name=data.decode().split()
        if os.path.exists(file_name) and os.path.isfile(file_name):
            f=open(file_name,'rb')
            m=hashlib.md5()
            file_size=os.path.getsize(file_name)
            conn.send(str(file_size).encode())
            ack=conn.recv(1024)
            print('收到客户端的确认',ack)
            for line in f:
                conn.send(line)
                m.update(line)
            f.close()
            md5=m.hexdigest()
            conn.send(md5.encode())    #给客户端发送文件的md5
            print('value of md5:',md5)
            print('send done')
server.close()


'''
1.接受指令
2.判断是否是文件，是否存在文件
3.读取文件，文件大小
4.发送大小
5.接受客户端确认信息
6.边读取边发送边计算md5
7.关闭文件
8.发送md5，做粘包处理
'''
