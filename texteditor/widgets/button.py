import tkinter
import consts

class Button(tkinter.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, bg=consts.BUTTON_BG_COLOR, fg=consts.TEXT_COLOR)