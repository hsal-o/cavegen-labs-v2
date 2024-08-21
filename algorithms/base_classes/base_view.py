import tkinter as tk
from tkinter import ttk

from widgets.label_entry import LabelEntry

class BaseView(tk.LabelFrame):
    def __init__(self, parent, controller, title):
        super().__init__(parent, text=title, relief=tk.SUNKEN, borderwidth=2)
        self.controller = controller

        self.widgets = {}
        self.widget_configs = {}
        self.create_widgets()
        self.build_widgets()

    def create_widgets(self):
        raise NotImplementedError("Method not implemented")

    def build_widgets(self):
        for key, config in self.widget_configs.items():
            widget = config.build_widget(self)
            widget.pack(fill=tk.X, padx=8, pady=4)
            self.widgets[key] = widget

    def has_empty_fields(self):
        for key, widget in self.widgets.items():
            if isinstance(widget, LabelEntry): 
                value = widget.get()
                if not value.strip():
                    return True
        return False