import socket,os

cmd_res = os.popen('ipconfig').read()
print(cmd_res)