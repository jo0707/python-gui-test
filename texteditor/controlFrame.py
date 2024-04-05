"""
This class is responsible for creating the buttons for opening and saving files inside a Frame.
"""

import tkinter
from fileutil import FileUtil
from widgets.button import Button

class ControlFrame(tkinter.Frame):
    def __init__(self, master=None, getTextContent = None, setTextContent = None, **kwargs):
        super().__init__(master, kwargs)
        self.getTextContent = getTextContent
        self.setTextContent = setTextContent
        self.openButton = Button(self, text="Open File", command=lambda: self.openFile())
        self.saveButton = Button(self, text="Save", command=lambda: self.saveFile())
        self.saveAsButton = Button(self, text="Save As", command=lambda: self.saveFileAs())
        self.openButton.pack(fill="x", side='top')
        self.saveButton.pack(fill="x", side='top')
        self.saveAsButton.pack(fill="x", side='top')
        
        
    def openFile(self):
        file_path = FileUtil.openFileDialog()
        if file_path:
            data = FileUtil.readFile(file_path)
            if data:
                self.setTextContent(data)

    def saveFile(self):
        data = self.getTextContent()
        if FileUtil.currentFilePath:
            FileUtil.saveFile(FileUtil.currentFilePath, data)
            
    def saveFileAs(self):
        file_path = FileUtil.saveFileDialog()
        if file_path:
            data = self.getTextContent()
            FileUtil.saveFile(file_path, data)