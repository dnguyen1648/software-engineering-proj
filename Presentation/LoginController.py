import socket
from tkinter import *
import pdfExtractor
import base64
from PIL import Image
import io
import os
import random
import hashlib
import imcrypt
import gui

SERVER_IP = "127.0.0.1"
PORT = 5050
FORMAT = "utf-8"

PRIVATE_KEY = random.randint(155, 2000)
FILE_COUNT = 0

#Socket connection to request information from server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, PORT))
except:
    print("FAILURE: Can not connect to the server, insert the following to turn on the server\npython Server.py")
    exit()

def registerUser(screen, username, password, email):
    inputParamters = f"Username: {username}\nPassword: {password}\nEmail: {email}"

    print(f"attempting to register User...")
    print(inputParamters)

    send(f"registerUser {username} {password} {email}")
    response = read()

    if response == "True":
        setPartialKey(email)
        gui.msgToScreen(screen, "Successful: please close out of the window")
        print(f"Registration successful")
    else:
        gui.msgToScreen(screen, f"Failure: email is already registered")
        print(f"Registration failed\nEither {email} is not unique")

def verifyLogin(topScreen, rootScreen, username, password, email):
    inputParameters = f"Username: {username}\nPassword: {password}\nEmail: {email}"

    print(f"attempting to verify User...")
    print(inputParameters)

    send(f"verify {username} {password} {email}")
    response = read()

    print(f"Response from {SERVER_IP}: {response}")

    if response == "ROOT":
        gui.admin_screen(rootScreen)
        print(f"Admin has logged in")
    elif response == "USER":
        gui.selection_screen(rootScreen, email)
        print(f"User {email} has logged in")
    elif response == "INVALID EMAIL":
        gui.msgToScreen(topScreen, f"Failure: Email {email} is not registered\nPlease try again")
        print(f"Email {email} is not registered")
    elif response == "INVALID CREDENTIALS":
        gui.msgToScreen(topScreen, f"Failure: incorrect username and/or password\nPlease try again")
    else:
        gui.msgToScreen(topScreen, f"INTERNAL ERROR: RESTART APPLICATION")
#TODO: CHANGE PUBLIC KEY TERMINOLGY RELEATED TO USERS TO REFER TO PARTIAL KEYS

def encrypt(screen, senderEmail, recieverEmail):
    global FILE_COUNT
    FILE_COUNT = 0

    if not validateEmail(recieverEmail):
        gui.msgToScreen(screen, "Please enter a registered recipient email")
        return


    print(f"{senderEmail} is sending encrypting an image for {recieverEmail}")
    pdfExtractor.extract()

    for x in os.listdir("images"):
        image64 = imgToByteAddress(f"images/{x}")
        AESKey = calcAESKey(recieverEmail)

        encryptMaster(senderEmail, image64, AESKey)




    """
    Insert encryption code here
    """
    #image64 = imgToByteAddress("images/pdf_file_p0-4.png")


    print("Success!")
    Label(screen, text="").pack()
    Label(screen, text="Success! Please close out of this window").pack()

    send("")

def validateEmail(email):
    send(f"validateEmail {email}")
    response = read()

    return response == "True"

def deleteUser(screen, otherEmail):
    if not validateEmail(otherEmail):
        gui.msgToScreen(screen, "Enter a registered email address")
        return

    send(f"deleteUser {otherEmail}")
    gui.msgToScreen(screen, f"{otherEmail} information has been deleted")

def getListOfEmails():
    send("getListOfEmails")
    response = read()

    if response == "no emails":
        return []

    return response.split(", ")

def printListOfEmails(rootScreen):
    listOfEmails = getListOfEmails()
    currScreen = Toplevel(rootScreen)

    gui.msgToScreen(currScreen, "List of all current employees emails\n")

    for email in listOfEmails:
        gui.msgToScreen(currScreen, f"{email}")

def calcAESKey(otherEmail):
    send("getPartialKey " + otherEmail)
    publicKey = int(read())

    send("getPrimer")
    response = read()
    primer = response.split(" ")

    base = int(primer[0])
    modulus = int(primer[1])

    dhKey = publicKey**PRIVATE_KEY%modulus

    return dhToAes(dhKey)

def encryptMaster(senderEmail, image64, aesKey):
    try:
        os.mkdir('encrypted')
    except:
        print('', end='')

    ciphertext = imcrypt.encrypt(senderEmail, image64, aesKey)

    global FILE_COUNT

    with open('encrypted\encryptedImg' + str(FILE_COUNT) + '.txt', 'wb') as a:  # wb: Write Binary
        a.write(ciphertext)
        FILE_COUNT = FILE_COUNT + 1



def decrypt(screen, email):
    global FILE_COUNT
    FILE_COUNT = 0

    try:
        os.mkdir('decrypted')
    except:
        print('', end='')

    for file in os.listdir("encrypted"):
        with open("encrypted\\" + file, 'rb') as a:
            ciphertext = a.read()
            foundEmail, foundTag, foundNonce, realDec = imcrypt.extractHead(ciphertext)
            senderEmail = foundEmail.decode('utf-16')
            AESkey = calcAESKey(senderEmail)
            b64string = imcrypt.decrypt(realDec, AESkey, foundNonce, foundTag)

            f = io.BytesIO(base64.b64decode(b64string))
            image = Image.open(f)

            image.save(f"decrypted/decryptedImage0-{FILE_COUNT}.png")
            FILE_COUNT = FILE_COUNT + 1

        print("Success!")
        Label(screen, text="").pack()
        Label(screen, text="Success! Please close out of this window").pack()

def decrypting():
    pass

def setPartialKey(email):
    send("getPrimer")
    response = read()
    primer = response.split(" ")

    base = int(primer[0])
    modulus = int(primer[1])

    partialKey = (base**PRIVATE_KEY)%modulus

    send(f"setPartialKey {email} {partialKey}")

def imgToByteAddress(fileName):
    with open(f"{fileName}", "rb") as image:
        return base64.b64encode(image.read())

def dhToAes(dhKey):
    byteKey = bytes(str(dhKey), 'utf-16')
    aesKey = (hashlib.sha256(byteKey)).digest()    # runs hash on the byte array and digests into bytes
    #print(aesKey)
    lenKey = len(aesKey)

    # gets 16 bytes (= 128 bits) from positions all around
    aesKey = aesKey[:4] + aesKey[16:20] + aesKey[-28:-24] + aesKey[-4:]
    #print(f"now have {aesKey}")
    return aesKey

def send(msg):
    sock.sendall(msg.encode(FORMAT))


def read():
    return sock.recv(2048).decode("utf-8")


