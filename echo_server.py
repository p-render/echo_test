#echo_server.py

import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP)

server_socket.bind(('127.0.0.1', 50000))
server_socket.listen(1)
conn, addr = server_socket.accept()

while True:
    conn, addr = server_socket.accept()
    while True:
        msg = conn.recv(32)
        conn.sendall(msg)
        if len(msg) < 32:
            break       
        
    conn.close()



