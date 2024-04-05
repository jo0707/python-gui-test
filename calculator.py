import tkinter

window = tkinter.Tk() # membuat window baru dan menyimpannya ke variabel window

labelTitle = tkinter.Label(window, text="Kalkulator Kompleks Hebad", font=("Arial", 18))
entry1 = tkinter.Entry(window)
labelPlus = tkinter.Label(window, text="+")
entry2 = tkinter.Entry(window)
buttonHitung = tkinter.Button(window, text="Hitung!")
labelHasil = tkinter.Label(window, text="Hasil: ")


# fungsi akan dijalankan saat buttonHitung diklik
def fungsiJumlah():
    angka1 = entry1.get() # mengambil nilai (string) dari entry1
    angka2 = entry2.get() # mengambil nilai (string) dari entry2
    hasilHitung = int(angka1) + int(angka2) # menjumlahkan angka1 dan angka2
    labelHasil.config(text=f"Hasil: {hasilHitung}") # mengubah teks labelHasil

buttonHitung.config(command=fungsiJumlah) # menambahkan fungsiJumlah ke buttonHitung saat diklik


labelTitle.pack()
entry1.pack()
labelPlus.pack()
entry2.pack()
buttonHitung.pack()
labelHasil.pack()

window.mainloop()
