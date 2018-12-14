import  socket

client=socket.socket()
client.connect(('localhost',9999))
while True:
    content=input("请输入要发送的内容:")
    if content.__len__()==0:
        continue
    client.send(content.encode())
    data=client.recv(1024)
    print(data.decode())

client.close()


#recy： 官方建议接受最大值不超过8192bytes
#send:只是把要发送的数据塞进缓冲区，并不是就直接发送出去了，如果数据过大这时候再次send会发送之前没有发送完的数据，
