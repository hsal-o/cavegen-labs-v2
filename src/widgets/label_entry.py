import tkinter as tk
from tkinter import ttk

from util.constants import WIDGET_WIDTH
from widgets.util.custom_base_widget import CustomBaseWidget

class LabelEntry(tk.Frame, CustomBaseWidget):
    def __init__(self, parent, label="", default=""):
        super().__init__(parent)
        
        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")
        
        # Create and place the label
        self.label = tk.Label(self, text=label, wraplength=WIDGET_WIDTH*7, anchor="w", justify="left")
        self.label.grid(row=0, column=0, sticky="w")
        
        # Create and place the entry
        self.entry = ttk.Entry(self, width=WIDGET_WIDTH)
        self.entry.grid(row=0, column=1, sticky="ew")
        
        # Set initial value
        self.entry.insert(0, default)

    def get(self):
        return self.entry.get()
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    # Implementing parent methods
    def is_empty(self):
        return not (self.get().strip())