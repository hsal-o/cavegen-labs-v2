import tkinter as tk
from tkinter import ttk

class LabelDoubleEntry(tk.Frame):
    def __init__(self, parent, label="", default=""):
        super().__init__(parent)

        self.widget_width = 7
        
        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")
        
        # Create and place the label
        self.label = tk.Label(self, text=label, anchor="w", justify="left")
        self.label.grid(row=0, column=0, sticky="w")

        entry_container = tk.Frame(self, background="red")
        entry_container.grid(row=0, column=1, sticky="ew")
        entry_container.grid_columnconfigure(0, weight=1, uniform="1")
        entry_container.grid_columnconfigure(1, weight=1, uniform="1")

        # Create and place the left entry
        self.entry_left = ttk.Entry(entry_container, width=self.widget_width)
        self.entry_left.grid(row=0, column=0, sticky="ew")

        # Create and place the right entry
        self.entry_right = ttk.Entry(entry_container, width=self.widget_width)
        self.entry_right.grid(row=0, column=1, sticky="ew")
        
        # Set initial value
        left_default, right_default = default
        self.entry_left.insert(0, left_default)
        self.entry_right.insert(0, right_default)
        
    def get(self):
        return (self.entry_left.get(), self.entry_right.get())
    
    def set(self, value):
        left_value, right_value = value

        self.entry_left.delete(0, tk.END)
        self.entry_left.insert(0, left_value)

        self.entry_right.delete(0, tk.END)
        self.entry_right.insert(0, right_value)
      