from tkinter import *
import random

window = Tk()
window.title("Password Generator")

string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

introText = Label(window, text = "Welcome to Lucas Pascholatti's Password Generator, below you will find your new password:")
numberLength = Entry(window, width=20, borderwidth=3)
# numberLength.insert(0, "Enter the password length")

def generatePassword (passlen):
  password =  "".join(random.sample(string,passlen))
  print(password)
  return password

def getNumber():
  passlen = numberLength.get()
  # generatedPassword = Label(window, text = "Your password is: " + generatePassword(number))
  # generatedPassword.grid(row = 3, column=0)
  print(passlen)
  renderNumber = Label(window, text=passlen)
  renderNumber.grid(row = 5, column = 0)
  return passlen

number = getNumber()
print(number)

def makePassword():
  newPassword = generatePassword(number)
  print(newPassword)
  # renderNewPassword = Label(window, text="Your new password is: " + newPassword)
  # renderNewPassword.grid(row = 7, column = 0)

button = Button(window, text="Submit Password Length", padx=15, pady=15, fg="black", bg="white", command=getNumber)
button2 = Button(window, text="Generate New Password", padx=15, pady=15, fg="black", bg="white", command=makePassword)

generatedPassword = Label(window, text = "Your password is: " + generatePassword(8))
generatedPassword.grid(row = 4, column=0)

introText.grid(row = 0, column=0)
numberLength.grid(row = 1, column=0)
button.grid(row = 3, column=0)
button2.grid(row = 6, column=0)

window.mainloop()