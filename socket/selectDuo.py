import selectors
import socket

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8000))
sk1.listen()

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8001))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('127.0.0.1', 8002))
sk3.listen()

li = [sk1, sk2, sk3]
while True:
    r_list, w_list, e_list = selectors.select(li, [], [], 1)
    for line in r_list:
        conn, addr = line.accept()
        conn.sendall(bytes('hello world!', encoding='utf-8'))
