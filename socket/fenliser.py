import socket
import select

sk1 = socket.socket()
sk1.bind(('0.0.0.0', 8080))
sk1.listen()

inputs = [sk1, ]
outputs = []
message_dict = {}

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)
    print('正在监听的socket对象%d' % len(inputs))
