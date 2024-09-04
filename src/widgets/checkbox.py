import tkinter as tk
from tkinter import ttk

class Checkbox(ttk.Checkbutton):
    def __init__(self, parent, label="", default=False):
        self.var = tk.BooleanVar()
        self.var.set(default)
        super().__init__(parent, variable=self.var, text=label, anchor="w")

    def set(self, value):
        self.var.set(value)

    def get(self):
        return self.var.get()