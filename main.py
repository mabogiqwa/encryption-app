from tkinter import *
from tkinter import messagebox
import base64
from PIL import Image, ImageTk
import os

def decrypt():
    try:
        encoded_message = text.get(1.0, END).strip()
        base64_bytes = encoded_message.encode("ascii")
        decoded_bytes = base64.b64decode(base64_bytes)
        decrypted_message = decoded_bytes.decode("ascii")
        screen1 = Toplevel(screen)
        screen1.title("Decryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#33ed83")
        Label(screen1, text="DECRYPT", font="arial", fg="white", bg="#33ed83").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypted_message)
    except Exception as e:
        print("Error during decryption:", e)

def encrypt():
    try:
        message = text.get(1.0, END)  # Retrieve text from text1
        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypt = base64_bytes.decode("ascii")
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)
    except Exception as e:
        print("Error:", e)
        
#Resets the message and password fields
def reset():
    code.set("")
    text.delete(1.0,END)

#Displays the main window
def main_screen():
    global code
    global text
    global screen
    
    screen=Tk()
    screen.geometry("375x250")
    screen.title("Message Encryption")

    #icon
    keys=Image.open("keys icon.jpeg")
    resized_keys=keys.resize((30,20))
    keys_icon=ImageTk.PhotoImage(resized_keys)
    screen.iconphoto(False,keys_icon)
    
    Label(text="Enter text for encryption:",fg="black",font=("calibri",13)).place(x=8,y=5)
    text=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text.place(x=10,y=30,width=355,height=100)

    #Label(text="Enter secret key for encryption and decryption:",fg="black",font=("calibri",13)).place(x=10,y=130)

    #code=StringVar()
    #Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=160)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=140)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=140)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=190)
    
    screen.mainloop()

#Calling function
main_screen()
