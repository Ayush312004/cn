import socket

s = socket.socket()
host = 'localhost'
port = 12345

s.connect((host, port))
s.send("Hello server!".encode())

with open('received_file.txt', 'wb') as f:
    print("File opened")
    while True:
        print("Receiving data...")
        data = s.recv(65536)

        if not data:
            break

        f.write(data)

print("Successfully received the file")
s.close()
print("Connection closed")
