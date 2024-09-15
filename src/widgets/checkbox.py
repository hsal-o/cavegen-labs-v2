import tkinter as tk
from tkinter import ttk

from widgets.util.custom_base_widget import CustomBaseWidget

class Checkbox(tk.Checkbutton, CustomBaseWidget):
    def __init__(self, parent=None, type=None, label="", default=False, tooltip=None, command=None):
        self.var = tk.BooleanVar()
        self.var.set(default)
        self.command = command

        super().__init__(parent, variable=self.var, text=label, anchor="w", command=self.on_toggle)
        CustomBaseWidget.__init__(self, type, tooltip)

        self.on_toggle()

    def set_command(self, command):
        self.command = command
        self.on_toggle()

    def on_toggle(self):
        if self.command:
            self.command(self.get())

    ########################################
    # Abstract Method Implementations
    ######################################## 
    def _get_value(self):
        return self.var.get()
    
    def set(self, value):
        self.var.set(value)
