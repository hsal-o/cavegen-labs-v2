import tkinter as tk
from tkinter import ttk

class OutputConsoleView(tk.Text):
    def __init__(self, parent):
        super().__init__(parent, bg="black", fg="white")
        self.insert("1.0", "Hello World!")
