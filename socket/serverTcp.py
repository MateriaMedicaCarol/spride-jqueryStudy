import socket

HOST = '10.70.107.171'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()  # conn是返回的一个连接的套接字对象 addr是返回连接的地址
print('客户端地址', addr)
while True:
    data = conn.recv(1024)
    print('获取信息', data.decode('utf-8'))
    if not data:
        break
    conn.sendall(data)
conn.close()
