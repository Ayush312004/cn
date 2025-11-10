import socket

host = "localhost"
port = 8000

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect((host, port))
print("Client socket is created and waiting for server")

message = "Hii"
print("Sending message to the server...")
cs.send(message.encode())

reply = cs.recv(1024).decode()
print("Server Says:", reply)

cs.close()
print("Connection closed!")
