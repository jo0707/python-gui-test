"""TextArea Widget
    A text area widget that inherits from tkinter.Text.
    Used for displaying and editing text.
"""

import tkinter
import consts

class TextArea(tkinter.Text):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, bg=consts.EDITOR_BG_COLOR, fg=consts.TEXT_COLOR, insertbackground=consts.TEXT_COLOR, selectbackground=consts.TEXT_COLOR, selectforeground=consts.EDITOR_BG_COLOR, wrap=tkinter.WORD)
        
    def get_text(self):
        return self.get(1.0, tkinter.END)
    
    def set_text(self, text):
        self.delete(1.0, tkinter.END)
        self.insert(tkinter.END, text)
        
    def clear(self):
        self.delete(1.0, tkinter.END)