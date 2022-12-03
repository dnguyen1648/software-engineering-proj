from tkinter import *
import LoginController
import pdfExtractor


def register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    username = StringVar()
    password = StringVar()
    email = StringVar()

    Label(screen1, text="Please enter valid info below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    Entry(screen1, textvariable=username).pack()
    Label(screen1, text="Password * ").pack()
    Entry(screen1, textvariable=password).pack()
    Label(screen1, text="Email * ").pack()
    Entry(screen1, textvariable=email).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1,
           command=lambda: LoginController.regUser(screen1, username.get(), password.get(), email.get())).pack()
#Pass down parameters to update the server process

def msgToScreen(currScreen, msg):
    Label(currScreen, text=msg).pack()

def login():
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    username = StringVar()
    password = StringVar()
    email = StringVar()

    Label(screen2, text="Please enter login info below").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Username * ").pack()
    Entry(screen2, textvariable=username).pack()
    Label(screen2, text="Password * ").pack()
    Entry(screen2, textvariable=password).pack()
    Label(screen2, text="Email * ").pack()
    Entry(screen2, textvariable=email).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1,
           command=lambda: LoginController.verifyLogin(screen2, screen, username.get(), password.get(), email.get())).pack()

def admin_screen(screen):
    screen6 = Toplevel(screen)
    screen6.title("Admin")
    screen6.geometry("300x250")

    otherEmail = StringVar()

    Label(screen6, text="Enter email of the employee you like to delete:").pack()
    Label(screen6, text="").pack()
    Entry(screen6, textvariable=otherEmail).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Delete", width=10, height=1, command=lambda: LoginController.deleteUser(screen6, otherEmail.get())).pack()

    Label(screen6, text="").pack()
    Button(screen6, text="Display list of employees", width=30, height=1, command=lambda: LoginController.printListOfEmails(screen)).pack()
    Label(screen6, text="").pack()



def selection_screen(screen, email: str):
    screen3 = Toplevel(screen)
    screen3.title("Selection")
    screen3.geometry("300x250")
    Label(screen3, text="").pack()
    Label(screen3, text=email).pack()
    Label(screen3, text="Please select if you are encrypting or decrypting").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Encrypt", width=10, height=1, command=lambda: encryption(screen, email)).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Decrypt", width=10, height=1, command=lambda: decryption(screen, email)).pack()



def encryption(screen, email: str):
    screen4 = Toplevel(screen)
    screen4.title("Selection")
    screen4.geometry("300x250")
    Label(screen4, text="").pack()
    Label(screen4, text=email).pack()
    Label(screen4, text="Please put a pdf with images in the content folder").pack()
    Label(screen4, text="").pack()

    Label(screen4, text="Please enter recipient email").pack()
    Label(screen4, text="").pack()

    otherEmail = StringVar()
    Entry(screen4, textvariable=otherEmail).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Encrypt", width=10, height=1, command=lambda: LoginController.encrypt(screen4, email, otherEmail.get())).pack()


def decryption(screen, email: str):
    screen5 = Toplevel(screen)
    screen5.title("Selection")
    screen5.geometry("300x250")
    Label(screen5, text="").pack()
    Label(screen5, text=email).pack()
    Label(screen5, text="Please put images to decrypt in the images folder ").pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Decrypt", width=10, height=1, command=lambda: LoginController.decrypt(screen5, email)).pack()

def check_encryption():
    pass

def check_decryption():
    pass

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Imcryptr")
    Label(text="Imcryptr", bg="grey", width="300", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()
    Button(text="Login", width="30", height="2", command=lambda: login()).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2", command=lambda: register()).pack()

    screen.mainloop()

if __name__ == "__main__":
    main_screen()
