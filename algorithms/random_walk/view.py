from algorithms.base_classes.base_view import BaseView
import tkinter as tk
from tkinter import ttk

class RandomWalkView(BaseView):
    def create_widgets(self):
        self.label_frame = tk.LabelFrame(self.frame, text="Random walk")
        self.label_frame.pack(expand='yes', fill='both', pady=0, padx=5)

        self.sample_entry = ttk.Entry(self.label_frame)
        self.sample_entry.pack(pady=10, padx=10)
        