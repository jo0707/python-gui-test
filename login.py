#  Joshua Palti Sinaga
# 122140141

import tkinter
from tkinter import messagebox

USERNAME = "admin"
PASSWORD = "admin"

def showSuccessDialog():
  messagebox.showinfo("SUCCESS", "Berhasil Login")

def showErrorDialog():
  messagebox.showerror("GAGAL", "Gagal Login")

def checkLogin(username, password):
  if username == USERNAME and password == PASSWORD:
    showSuccessDialog()
  else:
    showErrorDialog()

window = tkinter.Tk()
window.title("Login to App")

usernameLabel = tkinter.Label(window, text="Username : ")
usernameLabel.pack()

usernameEntry = tkinter.Entry(window)
usernameEntry.pack()

passwordLabel = tkinter.Label(window, text="Password : ")
passwordLabel.pack()

passwordEntry = tkinter.Entry(window)
passwordEntry.pack()

loginButton = tkinter.Button(window, text="Login", command=lambda: checkLogin(usernameEntry.get(), passwordEntry.get()))
loginButton.pack()

window.mainloop()