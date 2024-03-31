import tkinter
import random

window = tkinter.Tk() # membuat window baru dan menyimpannya ke variabel window

labelTitle = tkinter.Label(window, text="Pengambil Nomor Acak", font=("Arial", 18))
labelFirstNumber = tkinter.Label(window, text="Insert First Number:")
entryFirstNumber = tkinter.Entry(window)
labelSecondNumber = tkinter.Label(window, text="Insert Second Number:")
entrySecondNumber = tkinter.Entry(window)
buttonGenerate = tkinter.Button(window, text="Get my Random Number!")
labelResult = tkinter.Label(window, text="") # label ini tersembunyi (teks kosong) saat aplikasi dimulai


def showRandomNumber():
    firstNumber = entryFirstNumber.get() # mengambil nilai (string) dari entryFirstNumber
    secondNumber = entrySecondNumber.get() # mengambil nilai (string) dari entrySecondNumber
    randomNumber = random.randint(int(firstNumber), int(secondNumber)) # mengambil nomor acak antara firstNumber dan secondNumber
    labelResult.config(text=f"Your random number: {randomNumber}") # mengubah teks labelResult

buttonGenerate.config(command=showRandomNumber) # menambahkan showRandomNumber ke buttonGenerate saat diklik


labelTitle.pack()
labelFirstNumber.pack()
entryFirstNumber.pack()
labelSecondNumber.pack()
entrySecondNumber.pack()
buttonGenerate.pack()
labelResult.pack()

window.mainloop() # menampilkan window