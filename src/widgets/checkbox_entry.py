import tkinter as tk
from tkinter import ttk

from util.constants import WIDGET_WIDTH
from widgets.util.custom_base_widget import CustomBaseWidget

class CheckboxEntry(tk.Frame, CustomBaseWidget):
    def __init__(self, parent=None, type=None, label="", default=("", False), tooltip=None, command=None):
        super().__init__(parent)
        CustomBaseWidget.__init__(self, type, tooltip)
        self.command = command

        entry_default, checkbox_default = default

        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=2, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")

        # Create control variable
        self.is_checked = tk.BooleanVar()
        self.is_checked.set(checkbox_default)

        # Create checkbox
        self.checkbox = tk.Checkbutton(self, text=label, variable=self.is_checked, command=self.on_toggle)
        self.checkbox.grid(row=0, column=0, sticky="w")

        # Create entry
        # self.entry = ttk.Entry(self, width=WIDGET_WIDTH)
        self.entry = ttk.Entry(self, width=0)
        self.entry.grid(row=0, column=1, sticky="ew")
        self.entry.config(state="readonly")

        # self.entry.insert(0, str(entry_default))
        self.set(entry_default)

    def on_toggle(self):
        new_state = "normal" if self.is_active() else "readonly"
        self.entry.config(state=new_state)

        if self.command:
            self.command(self.is_active())

    # Get checkbox value
    def is_active(self):
        return self.is_checked.get()
    
    # Set command
    def set_command(self, command):
        self.command = command
        self.on_toggle()

    # Set checkbox value
    def set_active(self, value):
        self.is_active.set(value)

    ########################################
    # Abstract Method Implementations
    ######################################## 
    # Get entry value
    # Returns entry value if checkbox is active, otherwise returns None
    def _get_value(self):
        return self.entry.get() if self.is_active() else None
        
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

    ########################################
    # Method Overrides
    ########################################        
    def is_empty(self):
        raw_value = self.get()
        value = str(raw_value).strip() if raw_value is not None else ''
        return (self.is_active() and (not value))
    
    

