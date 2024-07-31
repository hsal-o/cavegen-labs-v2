import tkinter as tk
from tkinter import ttk

class GenericInputView:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        self.configuration_labelframe = tk.LabelFrame(self.frame, text=f"Grid Configuration")
        self.configuration_labelframe.pack(fill=tk.X, padx=5, pady=5)

        # Container frame for Entry + Label
        container = tk.Frame(self.configuration_labelframe)
        container.pack(fill=tk.BOTH, padx=5, pady=5)

        # Add label to container
        label = tk.Label(container, text=f"Width:")
        label.pack(side=tk.LEFT)

        # Add entry to container
        self.width_entry = ttk.Entry(container)
        self.width_entry.pack(side=tk.RIGHT)
        self.width_entry.insert(0, 32) 


    def get_frame(self):
        return self.frame

