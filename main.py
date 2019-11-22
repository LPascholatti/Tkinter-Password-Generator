import tkinter
import random

def generatePassword (passlen):
  string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
  password =  "".join(random.sample(string,passlen))
  print(password)
  return password

window = tkinter.Tk()

window.title("Password Generator")
introText = tkinter.Label(window, text = "Welcome to Lucas Pascholatti's Password Generator, below you will find your new password:").grid(row = 0)
generatedPassword = tkinter.Label(window, text = "Your password is" + generatePassword(8)).grid(row = 1)
window.mainloop()