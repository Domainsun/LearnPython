import socket
client=socket.socket()
client.connect(('localhost',9999))
while True:
    cmd=input('input cmd:')
    if len( cmd)==0:continue
    client.send(cmd.encode())
    res_size=client.recv(1024)     #获取传过来的数据size
    client.send(res_size)
    rev_size=0
    rev_data=b''
    while rev_size<int(res_size.decode()):  #接受的数据size小于传过来的数据size 则继续接收
        data=client.recv(1024)
        rev_data+=data
        rev_size += len(data)
    else:
        print('receive done!\n ',rev_data.decode())
client.close()