import socket
import os

HOST = "localhost"
PORT = 5000

client = socket.socket()
client.connect((HOST, PORT))

file_path = input("Enter file path to send: ")

if not os.path.isfile(file_path):
    print("File does not exist")
    client.close()
    exit()

filename = os.path.basename(file_path)
client.send(filename.encode())

with open(file_path, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client.send(data)

print("File sent successfully")
client.close()