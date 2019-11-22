from tkinter import *
import random

window = Tk()
window.title("Password Generator")

string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

introText = Label(window, text = "Welcome to Lucas Pascholatti's Password Generator, below you will find your new password:")
instruction = Label(window, text = "Please, state the password length below. Max characters is 74.")
numberLength = Entry(window, width=20, borderwidth=3)

def generatePassword(passlen):
  password =  "".join(random.sample(string,passlen))
  print("password:", password)
  return password

def makePassword():
  passlen = numberLength.get()
  passlenInt = int(passlen)
  newPassword = "Your new password is: " + generatePassword(passlenInt)
  renderNewPassword = Label(window, text=newPassword)
  renderNewPassword.grid(row = 6, column = 0)
  print("newpassword:", newPassword)

def getNumber():
  passlen = numberLength.get()
  renderNumber = Label(window, text= "Your Password's Length is: " + passlen)
  renderNumber.grid(row = 4, column = 0)
  print("passlen in getNumber:", passlen)
  return passlen

button = Button(window, text="Submit Password Length", padx=15, pady=15, fg="black", bg="white", command=getNumber)
button2 = Button(window, text="New Password", padx=15, pady=15, fg="black", bg="white", command=makePassword)

introText.grid(row = 0, column=0)
instruction.grid(row = 1, column = 0)
numberLength.grid(row = 2, column=0)
button.grid(row = 3, column=0)
button2.grid(row = 5, column=0)

window.mainloop()