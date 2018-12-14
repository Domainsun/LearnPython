import  socket,os
server=socket.socket()
server.bind(('localhost',8888))
server.listen(5)
while True:
    conn,adder=server.accept()
    while True:
        data=conn.recv(1024)
        data = data.decode()
        print('已收到来自客户端的消息:%s'%data)
        if data:
            os.system(data)
            conn.send(('我是服务端,已收到客户端内容:%s' % data).encode())
        else:
            print('服务端已经断开连接...')
            break
conn.close()
