import socket

HOST = '127.0.0.1'
PORT = 65432
s = socket.socket()
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print("Connected by: ", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)