import socket

host = "localhost"
port = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server socket is created and waiting for client...")

conn, addr = server_socket.accept()
print("Client connected:", addr)

data = conn.recv(1024).decode()
print("Client Says:", data)

message = "Hii"
conn.send(message.encode())
print("Reply to Client:", message)

conn.close()
server_socket.close()
