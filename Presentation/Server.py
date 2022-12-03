# This is a sample Python script.
import socket
import threading

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

PORT = 5050
SERVER_IP = "127.0.0.1"
FORMAT = "utf-8"
BASE = 5
MODULUS = 23
PRIMER = (BASE, MODULUS)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER_IP, PORT))

users = {"root": ("password", None)}
usersPublicKeys = {}
emailToUsername = {}
commands = {"verify", "validateEmail", "getPublicKey", "getListOfEmails", "regUser", "deleteUser", "setPublicKey", "getPrimer"}

#bob wants to send a tag to alice
# recipent email - > tag

# dictionary mapping email to pubic keys
# format prime integer
#public key primer
def handle_client(conn, addr):
    print(f"Client {addr} is connected")

    while True:
        msg = conn.recv(2048).decode(FORMAT)

        if not msg:
            break

        print(msg)

        command = msg.split(" ")

        if command[0] in commands:
            if command[0] == "verify":
                response = verify(command)
                conn.sendall(response.encode(FORMAT))
            if command[0] == "validateEmail":
                response = validateEmail(command)
                conn.sendall(response.encode(FORMAT))
            if command[0] == "getPublicKey":
                response = getPublicKey(command)
                conn.sendall(response.encode(FORMAT))
            if command[0] == "getListOfEmails":
                response = getListOfEmails(command)
                print(response)
                conn.sendall(response.encode(FORMAT))
            if command[0] == "regUser":
                response = regUser(command)
                conn.sendall(response.encode(FORMAT))
            if command[0] == "deleteUser":
                deleteUser(command)
            if command[0] == "setPublicKey":
                setPublicKey(command)
            if command[0] == "getPrimer":
                response = getPrimer(command)
                conn.sendall(response.encode(FORMAT))
        else:
            response = "Invalid command"
            conn.sendall(response.encode(FORMAT))

def start():
    sock.listen()
    while True:
        newConnection, clientAddr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(newConnection, clientAddr))
        thread.start()
        print(f"Active clients: {threading.active_count() - 1}")


def verify(command):
    username = command[1]
    password = command[2]
    email = command[3]

    rootPassword = users["root"][0]

    print(f"verifying...\nUsername: {username}\nPassword: {password}\nEmail: {email}")

    if username == "root" and password == rootPassword and email == "":
        return "root"

    if username in users.keys():
        storedPassword = users[username][0]
        storedEmail = users[username][1]

        if storedPassword == password and storedEmail == email:
            return "user"

    return "False"

def validateEmail(command):
    email = command[1]

    return str(email in usersPublicKeys.keys())

def getPublicKey(command):
    email = command[1]
    return usersPublicKeys[email]

def getListOfEmails(command):
    if usersPublicKeys:
        return str(usersPublicKeys.keys())[11:-2]

    return "no emails"

def regUser(command):
    username = command[1]
    password = command[2]
    email = command[3]

    if username not in users.keys() and email not in usersPublicKeys.keys():
        users[username] = (password, email)
        emailToUsername[email] = username
        print(f"{username} is now registered")
        return "True"

    print(f"{username} is already registered")
    return "False"

def deleteUser(command):
    email = command[1]

    del users[emailToUsername[email]]
    del usersPublicKeys[email]
    del emailToUsername[email]

def setPublicKey(command):
    email = command[1]
    publicKey = command[2]

    usersPublicKeys[email] = publicKey

def getPrimer(command):
    return f"{BASE} {MODULUS}"


print("Server is Starting")
start()
