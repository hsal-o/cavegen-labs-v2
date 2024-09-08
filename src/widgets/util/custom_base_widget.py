from abc import ABC, abstractmethod
import tkinter as tk

class CustomBaseWidget(ABC):
    def apply_pack(self, *args, **kwargs):
        self.pack(fill=tk.X, padx=8, pady=4)

    def show(self):
        self.apply_pack()

    def hide(self):
        self.pack_forget()

    @abstractmethod
    def is_empty(self):
        pass




