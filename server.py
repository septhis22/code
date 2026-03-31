import socket
import os

HOST = "localhost"
PORT = 5000
SAVE_DIR = "received_files"

os.makedirs(SAVE_DIR, exist_ok=True)

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Server waiting for client...")

conn, addr = server.accept()
print("Connected from", addr)

# receive file name
filename = conn.recv(1024).decode()
filepath = os.path.join(SAVE_DIR, filename)

# receive file data
with open(filepath, "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File stored successfully:", filename)

conn.close()
server.close()