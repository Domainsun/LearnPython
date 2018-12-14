import select
import socket
import datetime

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 9999))
sock.listen(5)
sock.setblocking(0)

inputs = [sock, ]
while True:
    print(datetime.datetime.now())
    rlist, wlist, errlist = select.select(inputs, [], [], 10)
    print(" >>> ", rlist, wlist, errlist)
    for s in rlist:
        if s is sock:
            con, addr = s.accept()
            print('新的客户端连接:',addr)
            # 将新的请求连接加入到监控列表中
            inputs.append(con)
        else:
            # 对于其他的文件描述符要接收信息并返回
            try:
                data = s.recv(1024)
                if data:
                    s.send(data)
            finally:
                s.close()
                inputs.remove(s)