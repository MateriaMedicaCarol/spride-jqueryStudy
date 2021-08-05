import socket

HOST = '10.70.107.171'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = '你好!'
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print('获取服务器信息:\n', data.decode('utf-8'))
    data = input('请输入信息：\n')
s.close()
