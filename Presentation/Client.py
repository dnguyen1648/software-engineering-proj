import socket

PORT = 5050
SERVER_IP = "127.0.0.1"
FORMAT = "utf-8"
EMAIL = "bob@gmail.com"
PASSWORD = "password123"
PRVIATE_KEY = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))

def send(msg):
        sock.sendall(msg.encode(FORMAT))

def read():
    return sock.recv(2048).decode("utf-8")



send("getPublicKey bob@gmail.com")
print(read())



"""

Encryption code

"""

