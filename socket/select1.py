import select
import socket
import struct, time

PORT = 8037

TIME1970 = 2208988800

service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("", PORT))
service.listen(1)

print("listening on port", PORT)

while True:
    is_readable = [service]
    is_writable = []
    is_error = []
    r, w, e = select.select(is_readable, is_writable, is_error, 1.0)
    if r:
        channel, info = service.accept()
        print("connection from", info)
        t = int(time.time()) + TIME1970
        t = struct.pack("!I", t)
        channel.send(t)  # send timestamp        channel.close() # disconnect
    else:
        print('will')
