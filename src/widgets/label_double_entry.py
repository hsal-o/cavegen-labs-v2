import tkinter as tk
from tkinter import ttk

from util.constants import WIDGET_WIDTH
from widgets.util.custom_base_widget import CustomBaseWidget

class LabelDoubleEntry(tk.Frame, CustomBaseWidget):
    def __init__(self, parent, label="", default=("", ""), tooltip=None):
        super().__init__(parent, background="red")
        CustomBaseWidget.__init__(self, tooltip)

        ### Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")
        
        ### Create and place the label
        self.label = tk.Label(self, text=label, anchor="w", justify="left")
        self.label.grid(row=0, column=0, sticky="w")

        ### Create double entry for custom input
        entry_container = tk.Frame(self, background="red", width=WIDGET_WIDTH)
        entry_container.grid(row=0, column=1, sticky="ew")
        entry_container.grid_columnconfigure(0, weight=1)
        entry_container.grid_columnconfigure(1, weight=1)

        # Create and place the left entry
        self.entry_left = ttk.Entry(entry_container, width=0)
        self.entry_left.grid(row=0, column=0, sticky="ew")

        # Create and place the right entry
        self.entry_right = ttk.Entry(entry_container, width=0)
        self.entry_right.grid(row=0, column=1, sticky="ew")

        
    def get(self):
        return (self.entry_left.get(), self.entry_right.get())
    
    def set(self, value):
        left_value, right_value = value

        self.entry_left.delete(0, tk.END)
        self.entry_left.insert(0, left_value)

        self.entry_right.delete(0, tk.END)
        self.entry_right.insert(0, right_value)
      
    # Implementing parent methods
    def is_empty(self):
        return not (self.entry_left.get().strip() and self.entry_right.get().strip())