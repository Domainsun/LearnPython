'''
1. 创建请求处理类（ 每一个客户端 都会实例化一个这个类），继承自BaseRequestHandler,重写handle  用于处理客户端发送过来的请求。
2. 实例化TCPServer（用什么请求就示例化什么：1.TCPServer 2.UDPServer 3.UnixStreamServer(Unix的TCP),4,UnixStreamServer）(Unix的UDP)，传递ip，和刚刚创建的请求类
3.调用 实例化TCPServer对象的serve_forever()
4.调用 实例化TCPServer对象的close()
'''

import  socketserver
class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:     #不断接收
            try:
                data=self.request.recv(1024)#通过self.request 接收
                print(data)
                self.request.send('from server: '.encode()+data)#通过self.request 发送
            except ConnectionResetError as e:
                print(e)
                break


# server=socketserver.TCPServer(('localhost',9999),RequestHandler)        #只能一个客户端操作
server=socketserver.ThreadingTCPServer(('localhost',9999),RequestHandler) #多线程执行，实现并发
server.serve_forever()
