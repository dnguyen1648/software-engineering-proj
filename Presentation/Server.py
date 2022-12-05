import socket
import threading

PORT = 5050
SERVER_IP = "127.0.0.1"
FORMAT = "utf-8"

BASE = 5
MODULUS = 23
PRIMER = (BASE, MODULUS)

ROOT_USERNAME = "r"
ROOT_PASSWORD = "p"

#Create a socket to listen to request from multiple clients
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER_IP, PORT))

#TODO change key to be the email rather than the username

"""
Example of User database

        PK
    __________
|      Email     | Username |   Password   | Partial Key |
--------------------------------------------------------
|Alice@gmail.com | Alice    | Password*123 |     125     |
----------------------------------------------------------
|Bob@gmail.com   | Bob      | Password*456 |     254     |

"""

"""

Dictionary implementation example

{Alice@gmail.com : (Alice, Password*123, 125), Bob@gmail.com: (Bob, Password*456, 254)}

"""

users = {}

"""
USAGE OF COMMANDS

verify <username> <password> <email> 

returns "ROOT" if the username and password equal the stored ROOT_USERNAME and ROOT_PASSWORD and the email is an empty string
returns "USER" if the email is stored key in the dictionary/database
returns "False" if

validateEmail <Email>

...



"""

commands = {"verify", "validateEmail", "getPrimer", "getPartialKey", "getListOfEmails", "setPartialKey", "registerUser", "deleteUser"}

def handle_client(conn, addr):
    print(f"Client {addr} is connected")

    while True:
        msg = conn.recv(2048).decode(FORMAT)

        if not msg:
            break

        print(f"Incoming request from {addr}: {msg}")

        command = msg.split(" ")
        
        commandStem = command[0]
        
        if commandStem in commands:
            if commandStem == "verify":
                sendResponse(verify(command), conn)
            if commandStem == "validateEmail":
                sendResponse(validateEmail(command), conn)
            if commandStem == "getPartialKey":
                sendResponse(getPartialKey(command), conn)
            if commandStem == "getListOfEmails":
                sendResponse(getListOfEmails(command), conn)
            if commandStem == "registerUser":
                sendResponse(registerUser(command), conn)
            if commandStem == "deleteUser":
                deleteUser(command)
            if commandStem == "setPartialKey":
                setPartialKey(command)
            if commandStem == "getPrimer":
                sendResponse(getPrimer(command), conn)
        else:
            sendResponse("Invalid command", conn)

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

    storedUsername = ""
    storedPassword = ""

    inputParameters = f"Username: {username}\nPassword: {password}\nEmail: {email}"

    print(f"verifying...")
    log(inputParameters)

    if username == ROOT_USERNAME and password == ROOT_PASSWORD and email == "":
        print("Verification successful")
        print(f"Verified as root user")
        return "ROOT"

    if email in users.keys():
        storedUsername = users[email][0]
        storedPassword = users[email][1]

        if username == storedUsername and password == storedPassword:
            print("Verification successful")
            print(f"Verified as user")
            return "USER"

    print(f"Verification failed")

    if email not in users.keys():
        print(f"Reason: Email {email} is not registered")
        return "INVALID EMAIL"
    elif username != storedUsername or password != storedPassword:
        print(f"Reason: Username {username} and/or password {password} is incorrect")
        return "INVALID CREDENTIALS"
    else:
        print("Reason: uhhh, this line of code shouldn't be executed")
        return "ERROR"

def validateEmail(command):
    email = command[1]

    return str(email in users.keys())

def getPartialKey(command):
    email = command[1]
    return users[email][2]

def getListOfEmails(command):
    if users:
        return str(users.keys())[11:-2]

    return "no emails"

def registerUser(command):
    username = command[1]
    password = command[2]
    email = command[3]

    inputParameters = f"Username: {username}\nPassword: {password}\nEmail: {email}"

    print("registering user...")
    print(f"attempting to register User...\n")
    print(inputParameters)

    if email not in users.keys() and username != ROOT_USERNAME:
        users[email] = [username, password, -1]
        print(f"SUCCESSFUL: {email} is now registered")
        return "True"

    print(f"FAILED: User is already registers")
    return "False"

def deleteUser(command):
    email = command[1]

    del users[email]

def setPartialKey(command):
    email = command[1]
    partialKey = command[2]

    users[email][2] = partialKey

def getPrimer(command):
    return f"{BASE} {MODULUS}"

#Displays msg and current state
def log(msg):
    print(msg)
    print(getState())

def getState():
    pass

def sendResponse(response, conn):
    conn.sendall(response.encode(FORMAT))
    

print("Server is Starting...")
start()