"""Before running this code, install the following packages:
    Windows:
        pip install qrcode
    Linux:
        python -m venv venv
        source venv/bin/activate
        pip install qrcode
"""

import tkinter
import qrcode
    
window = tkinter.Tk()
window.title("QR Code Generator")

label = tkinter.Label(window, text="Enter the data to be encoded:")
textInput = tkinter.Entry(window)
button = tkinter.Button(window, text="Generate QR Code", command=lambda: generate_qr(textInput.get()))

# penting, PhotoImage bukanlah widget, namun sebuah objek yang nantinya dapat dimasukkan ke widget Label sebagai gambar
qrPhotoImage = tkinter.PhotoImage()
qrPhotoLabel = tkinter.Label(window)

def generate_qr(data):
    qrImage = qrcode.make(data)
    qrImage.save("qrcode.png")
    qrPhotoImage.config(file="qrcode.png")
    qrPhotoLabel.config(image=qrPhotoImage)


label.pack()
textInput.pack()
button.pack()
qrPhotoLabel.pack()

window.mainloop()
