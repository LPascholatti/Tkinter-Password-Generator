import tkinter
import random

def generatePassword (passlen):
  string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
  password =  "".join(random.sample(string,passlen))
  print(password)
  return password

window = tkinter.Tk()
# to rename the title of the window
window.title("Password Generator")
# pack is used to show the object in the window
introText = tkinter.Label(window, text = "Welcome to Lucas Pascholatti's Password Generator, below you will find your new password:").grid(row = 0)
# passwordLength = tkinter.Label(window, text = "Password Length.").grid(row = 1)
# lengthEntry = tkinter.Entry(window).grid(row = 1, column = 1)
generatedPassword = tkinter.Label(window, text = "Your password is" + generatePassword(8)).grid(row = 1)
window.mainloop()