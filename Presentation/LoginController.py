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

PORT = 5050
SERVER_IP = "127.0.0.1"
FORMAT = "utf-8"
PRIVATE_KEY = random.randint(155, 2000)
#feature
FILE_COUNT = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))


def send(msg):
    sock.sendall(msg.encode(FORMAT))


def read():
    return sock.recv(2048).decode("utf-8")

def regUser(screen, username, password, email):
    send(f"regUser {username} {password} {email}")
    response = read()

    if response == "True":
        setPublicKey(email)
        gui.msgToScreen(screen, "Successful: please close out of the window")
    else:
        gui.msgToScreen(screen, f"Failure: email or username is already registered")


def verifyLogin(topScreen, rootScreen, username, password, email):
    send(f"verify {username} {password} {email}")
    response = read()

    if response == "root":
        gui.admin_screen(rootScreen)
    elif response == "user":
        gui.selection_screen(rootScreen, email)
    else:
        gui.msgToScreen(topScreen, f"Failure: incorrect username, password, and email\nPlease try again")
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

    print(response)

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
    send("getPublicKey " + otherEmail)
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

            image.save(f"decrypt/decryptedImage0-{FILE_COUNT}.png")
            FILE_COUNT = FILE_COUNT + 1

        print("Success!")
        Label(screen, text="").pack()
        Label(screen, text="Success! Please close out of this window").pack()

def decrypting():
    pass

def setPublicKey(email):
    send("getPrimer")
    response = read()
    primer = response.split(" ")

    base = int(primer[0])
    modulus = int(primer[1])

    publicKey = (base**PRIVATE_KEY)%modulus

    send(f"setPublicKey {email} {publicKey}")

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

