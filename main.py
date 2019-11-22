import tkinter
import random

# string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 8
# password =  "".join(random.sample(string,passlen))

def generatePassword ():
  string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
  passlen = 8
  password =  "".join(random.sample(string,passlen))
  print(password)
  return password

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Welcome to Lucas Pascholatti's Password Generator, below you will find your new password:").pack()
label = tkinter.Label(window, text = generatePassword()).pack()
window.mainloop()