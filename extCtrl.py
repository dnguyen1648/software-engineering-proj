# Extension Controller
# listens until an event occurs
#   the reader (the Outlook Add-in or equivalent) sends images to be en/decrypted
#   the database controller requests a public key from the user

import 
import Base64       # method to convert img to str

# ***************************************************
# GLOBAL
# ***************************************************
User = {"user id and company"}       # assigned when created by server


void main: 
    # listens for requests
    
    # ---- if db asks for key ----
    res = getEmployeePublicKey()
    # if no key, make one
    if (res == error):
        getPrimer()
        calculatePublicKey()
    sendPublicKey()
    
    # ---- if reader sends images ----
    # received something from the reader (img, code)
    # read the image as binary
    open(img, "rb") as image2string:
        imgStr = base64.b64encode(image2string.read())
    priv = calculatePrivateKey()
    # figure out if it's to be encrypted  or decrypted
    if (code == encryptCode):
        encrypt(imgStr, priv)
    elif (code == decryptCode):
        decrypt(imgStr, priv)
    else:
        print("bruh")
    # now send that result to the reader to put back into the email
    
int getPrimer:
    # go to server to ask database for primer
    return primer
    
# part of the diffie hellman process
int calculatePublicKey:
    # uses primer and user private key to make public key
    pri = requestPrivateKey # requesting the User 
    pub = a lot of complicated math(primer, pri)
    return pub
    
int getEmployeePublicKey: 
    # go to server to beg database for the OTHER employee's key
    # we know who the other employee is from the addin reading the recipient
    
int calculatePrivateKey:
    bob = getEmployeePublicKey
    alice = requestPrivateKey
    realPri = diffieHellmanMagic(alice, bob)
    return realPri
    
# whatever it takes to constantly run the extension
if __name__ == "__main__":
    main()
    