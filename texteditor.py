import tkinter
import tkinter.filedialog

window = tkinter.Tk()
window.geometry("1000x800")

frame1 = tkinter.Frame(window, width=200)
frame1.pack(fill="y", side='left')
frame1.pack_propagate(False)

openButton = tkinter.Button(frame1, text="Open")
openButton.pack()

saveButton = tkinter.Button(frame1, text="Save")
saveButton.pack()

text = tkinter.Text(window)
text.pack(expand=True, fill='both', side='right')

def readFile():
    file_path = tkinter.filedialog.askopenfilename()
    if file_path:
        file = open(file_path, 'r')
        data = file.read()
        text.delete(1.0, tkinter.END)
        text.insert(tkinter.END, data)
            
def saveFile():
    file_path = tkinter.filedialog.asksaveasfilename()
    if file_path:
        data = text.get(1.0, tkinter.END)
        file = open(file_path, 'w')
        file.write(data)
        file.close()

openButton.config(command=readFile)
saveButton.config(command=saveFile)

window.mainloop()