import socket

s = socket.socket()
host = 'localhost'
port = 12345

s.bind((host, port))
s.listen(5)

print("Server listening on", host, port)

while True:
    conn, addr = s.accept()
    print("Got connection from", addr)

    data = conn.recv(1024).decode()
    print("Server received:", data)

    filename = 'file.txt'
    f = open(filename, 'rb')
    chunk = f.read(65536)

    while chunk:
        conn.sendall(chunk)
        print("Sent:", len(chunk), "bytes")
        chunk = f.read(65536)

    f.close()
    print("Done sending")

    conn.send("Thank you for connecting".encode())
    conn.close()
