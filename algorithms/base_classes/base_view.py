import tkinter as tk
from tkinter import ttk

class BaseView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def get_frame(self):
        return self.frame

    def create_widgets(self):
        raise NotImplementedError("Method not implemented")
