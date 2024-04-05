import tkinter
import consts
from widgets.textarea import TextArea
from widgets.button import Button

class TextFrame(tkinter.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs, bg=consts.BG_COLOR)
        self.infoFrame = tkinter.Frame(self, bg=consts.BG_COLOR)
        self.infoFrame.pack(expand=False, fill="x")
        self.filenameLabel = tkinter.Label(self.infoFrame, text="File Name:", fg=consts.TEXT_COLOR, bg=consts.BG_COLOR)
        self.filenameLabel.pack(expand=True, fill='x', side='left')
        self.clearButton = Button(self.infoFrame, text="Clear", command=lambda: self.textarea.clear())
        self.clearButton.pack(side='right')
        self.textarea = TextArea(self)
        self.textarea.pack(expand=True, fill='both', side='right')
        
    def set_text(self, text):
        self.textarea.set_text(text)
        
    def get_text(self):
        return self.textarea.get_text()
    
    def clear(self):
        self.textarea.clear()
        
    def set_filename(self, filename):
        self.filenameLabel.config(text=f"File Name: {filename}")
        
    def get_filename(self):
        return self.filenameLabel.cget('text')
    
    