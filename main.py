from tkinter import *
import random

window = Tk()
window.title("Password Generator")

string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

introText = Label(window, text = "Welcome to Lucas Pascholatti's Password Generator, below you will find your new password:")
numberLength = Entry(window, width=20, borderwidth=3)

# it works, though it needs to be hard coded and cannot get the int as input

def generatePassword(passlen):
  password =  "".join(random.sample(string,passlen))
  print("password:", password)
  return password

# attempting to generate a new password and render at the same time - not working

def makePassword():
  passlen = numberLength.get()
  passlenInt = int(passlen)
  newPassword = "Your new password is: " + generatePassword(passlenInt)
  renderNewPassword = Label(window, text=newPassword)
  renderNewPassword.grid(row = 7, column = 0)
  print("newpassword:", newPassword)

def getNumber():
  passlen = numberLength.get()
  renderNumber = Label(window, text=passlen)
  renderNumber.grid(row = 5, column = 0)
  print("passlen in getNumber:", passlen)
  return passlen

button = Button(window, text="Submit Password Length", padx=15, pady=15, fg="black", bg="white", command=getNumber)
button2 = Button(window, text="New Password", padx=15, pady=15, fg="black", bg="white", command=makePassword)

# generatedPassword = Label(window, text = "Your password is: " + generatePassword(8))
# generatedPassword.grid(row = 4, column=0)

introText.grid(row = 0, column=0)
numberLength.grid(row = 1, column=0)
button.grid(row = 3, column=0)
button2.grid(row = 6, column=0)

window.mainloop()