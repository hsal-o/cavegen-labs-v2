import tkinter as tk
from tkinter import ttk

from util.constants import WIDGET_WIDTH
from util.create_tool_tip import CreateToolTip
from widgets.util.custom_base_widget import CustomBaseWidget

class LabelEntry(tk.Frame, CustomBaseWidget):
    def __init__(self, parent=None, type=None, label="", default="", tooltip=None):
        super().__init__(parent)
        CustomBaseWidget.__init__(self, type, tooltip)
        
        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")
        
        # Create and place the label
        self.label = tk.Label(self, text=label, wraplength=WIDGET_WIDTH*6, anchor="w", justify="left")
        self.label.grid(row=0, column=0, sticky="w")
        
        # Create and place the entry
        self.entry = ttk.Entry(self, width=WIDGET_WIDTH)
        self.entry.grid(row=0, column=1, sticky="ew")
        
        # Set initial value
        self.entry.insert(0, default)

    ########################################
    # Abstract Method Implementations
    ######################################## 
    def _get_value(self):
        return self.entry.get()
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
