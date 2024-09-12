from abc import ABC, abstractmethod
import tkinter as tk

from util.create_tool_tip import CreateToolTip

class CustomBaseWidget(ABC):
    def __init__(self, tooltip=None):
        if tooltip:
            CreateToolTip(self, tooltip)

    def apply_pack(self, *args, **kwargs):
        self.pack(fill=tk.X, padx=8, pady=2)

    def show(self):
        self.apply_pack()

    def hide(self):
        self.pack_forget()

    @abstractmethod
    def is_empty(self):
        pass




