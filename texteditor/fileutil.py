"""
FileUtil class
A utility class for file operations.
"""


import tkinter as tk
from tkinter import filedialog

class FileUtil:
    currentFilePath = ""
    
    @staticmethod
    def openFileDialog():
        print("Opening file dialog...")
        file_path = filedialog.askopenfilename()
        FileUtil.currentFilePath = file_path
        return file_path
    
    def saveFileDialog():
        print("Saving file dialog...")
        file_path = filedialog.asksaveasfilename()
        FileUtil.currentFilePath = file_path
        return file_path

    @staticmethod
    def readFile(file_path = currentFilePath):
        try:
            with open(file_path, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file '{file_path}': {str(e)}")
            return None

    @staticmethod
    def saveFile(file_path = currentFilePath, data = ""):
        try:
            with open(file_path, 'w') as file:
                file.write(data)
            print(f"Data saved to '{file_path}' successfully.")
        except Exception as e:
            print(f"An error occurred while saving data to the file '{file_path}': {str(e)}")
