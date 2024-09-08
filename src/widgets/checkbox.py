import tkinter as tk
from tkinter import ttk

from widgets.util.custom_base_widget import CustomBaseWidget

class Checkbox(tk.Checkbutton, CustomBaseWidget):
    def __init__(self, parent, label="", default=False, command=None):
        self.var = tk.BooleanVar()
        self.var.set(default)
        self.command = command
        super().__init__(parent, variable=self.var, text=label, anchor="w", command=self.on_toggle)
        self.on_toggle()

    def set_command(self, command):
        self.command = command
        self.on_toggle()

    def on_toggle(self):
        if self.command:
            self.command(self.get())

    def set(self, value):
        self.var.set(value)

    def get(self):
        return self.var.get()
    
    # Implementing parent methods
    def is_empty(self):
        return False