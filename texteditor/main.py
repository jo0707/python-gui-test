import tkinter
import consts
from textFrame import TextFrame
from controlFrame import ControlFrame

window = tkinter.Tk()
window.title("Text Editor")
window.geometry("1280x800")
window.config(bg=consts.BG_COLOR)

mainFrame = tkinter.Frame(window, bg=consts.BG_COLOR)
mainFrame.pack(expand=True, fill='both')

controlFrame = ControlFrame(
    mainFrame,
    getTextContent=lambda: textFrame.get_text(),
    setTextContent=lambda data: textFrame.set_text(data),
    width=200,
    bg=consts.BG_COLOR
)
controlFrame.pack_propagate(False)
controlFrame.pack(fill='y', side='left')

textFrame = TextFrame(mainFrame, bg=consts.BG_COLOR)
textFrame.pack(expand=True, fill='both', side='right')


window.mainloop()