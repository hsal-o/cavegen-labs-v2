import tkinter as tk
from tkinter import ttk

from util.constants import WIDGET_WIDTH
from widgets.custom_base_widget import CustomBaseWidget

class CheckboxEntry(tk.Frame, CustomBaseWidget):
    def __init__(self, parent, label="", default=("", False)):
        super().__init__(parent)

        entry_default, checkbox_default = default

        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")

        # Create control variable
        self.is_checked = tk.BooleanVar()
        self.is_checked.set(checkbox_default)

        # Create checkbox
        self.checkbox = tk.Checkbutton(self, text=label, variable=self.is_checked, command=self.toggle_entry_state)
        self.checkbox.grid(row=0, column=0, sticky="w")

        # Create entry
        self.entry = ttk.Entry(self, width=WIDGET_WIDTH)
        self.entry.grid(row=0, column=1, sticky="ew")
        self.entry.config(state="readonly")

        self.entry.insert(0, entry_default)

    # Helper method
    def toggle_entry_state(self):
        if self.is_checked.get() == True:
            new_state = "normal"
        else:
            new_state = "readonly"
        self.entry.config(state=new_state)

    # Get entry value
    def get(self):
        return self.entry.get()

    # Get checkbox value
    def is_active(self):
        return self.is_checked.get()
    
    # Set entry value
    def set(self, value):
        # If entry is disabled, temporily enable it
        if(not self.is_active()):
             self.entry.config(state="normal")

        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

        # If entry was originally disabled, disable it again
        if(not self.is_active()):
             self.entry.config(state="readonly")

    # Set checkbox value
    def set_active(self, value):
        self.is_active.set(value)

    # Implementing parent methods
    def is_empty(self):
        value = self.get().strip()
        return (self.is_active() and (not value))
            

