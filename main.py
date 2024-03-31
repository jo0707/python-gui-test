import tkinter

def button1Click():
    print("Button 1 diklik")


window = tkinter.Tk() # membuat window baru dan menyimpannya ke variabel window

# Membuat widgets
# Widget Label adalah widget yang digunakan untuk menampilkan teks atau gambar
# membuat objek Label
myNameLabel = tkinter.Label(
    window,
    text="Nama saya Fredi",
    background="red",
    cursor="target", # kita bisa tambahkan kustomisasi lainnya di sini
    font=("Arial", 24),
    width=20,
    height=5,
)
myNameLabel.pack() # mengirim label ke window

# Widget Entry adalah widget yang digunakan untuk menerima input teks dari pengguna
# membuat objek Entry
kolomTextSebaris = tkinter.Entry(window)
kolomTextSebaris.pack() # mengirim kolomTextSebaris ke window

# Widget Text adalah widget yang digunakan untuk menerima input dalam beberapa baris
# membuat objek Text
kolomTextMultiline = tkinter.Text(window) 
kolomTextMultiline.pack() # mengirim kolomTextMultiline ke window

# Widget Button adalah widget yang digunakan untuk membuat tombol
# membuat objek Button
button1 = tkinter.Button(
    window, 
    text="Tekan aku!", 
    command=button1Click
) 
button1.pack() # mengirim button ke window

window.mainloop() # menampilkan window