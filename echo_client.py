#echo_client.py

import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)

client_socket.connect(('127.0.0.1', 50000))
client_socket.sendall("Hey, can you hear me? Here is a longer message, so there.")

client_socket.shutdown(socket.SHUT_WR)

total = ''

while True:
    msg = client_socket.recv(32)
    total += msg

    if len(msg) < 32:
        break  
# conn.sendall("Yes, I hear you.")
# conn.shutdown(socket.SHUT_WR)
client_socket.close()

print total