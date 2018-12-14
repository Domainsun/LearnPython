import socket,os
server=socket.socket()
server.bind( ('localhost',9999) )
server.listen()
while True:
    conn,addr=server.accept()
    while True:
        print('等待指令中...')
        data=conn.recv(1024)
        if not data:
            print('客户端已经断开')
            break
        print('执行命令:', data.decode())
        cmd_res=os.popen(data.decode()).read()     #执行cmd命令
        if len(cmd_res)==0:                        #没有结果 表示执行失败
            cmd_res="错误的cmd命令!"
        conn.send(str(len(cmd_res.encode())).encode()) #发送执行结果的长度，先encode再取长度,因为有中文存在encode前一个汉字都是1的大小，encode后变成了3的大小，最后encode发送
        comfirm_message=conn.recv(1024)                #粘包处理
        print('收到客户端的确认:',comfirm_message.decode())
        conn.send(cmd_res.encode())
        print('send done')
server.close()

'''
粘包处理: 
    粘包:两次同时send，会导致两次发送的数据合并，windows的3.x python 环境下出现次数较少，在linux环境下必然出现。
    解决方式:send完第一次后，客户端接受到第一次发送的数据，然后再给服务端发送一下接受到的确认信息，服务端接收到确认信息后再发送第二次
os.popen('cmd')  os.popen('python') 执行后卡死
    还没有找到解决方式和原因
'''


