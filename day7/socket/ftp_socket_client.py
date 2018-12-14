import socket,hashlib
client=socket.socket()
client.connect(('localhost',9999))
while True:
    cmd=input('input cmd:')
    if len( cmd)==0:continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        res_size=client.recv(1024)     #获取传过来的数据size
        client.send(res_size)          #给服务端发送传过来的数据size以确认
        res_size=int(res_size.decode())
        rev_size=0
        file_name=cmd.split()[1]
        f=open('new'+file_name,'wb')
        m=hashlib.md5()
        while rev_size<res_size:  #接受的数据size小于传过来的数据size 则继续接收
            if res_size-rev_size>1024:   # 用接收大小处理文件数据和md5的粘包，如果剩余接收文件大小大于1024，继续接收1024的大小
                size=1024
            else:
                size=res_size-rev_size   # 如果剩余接收文件大小小于或者等于1024，就接收文件总大小减去已经接收的文件大小
            data = client.recv(size)     # 开始接收
            rev_size += len(data)
            f.write(data)               # 边接收边写入文件
            m.update(data)        # 计算已接收文件的md5值，md5是连续叠加的
        else:
            f.close()
            server_md5=client.recv(1024)    #接收服务端发送的md5值
            client_md5=m.hexdigest()
            print('receive done!\n ','rev_size:',rev_size,'rev_size:',rev_size)
            print('server_md5:',server_md5,'client_md5:',client_md5)   #输出接收到文件的md5值和服务端发送的md5值
client.close()