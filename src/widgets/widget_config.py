import tkinter as tk
from tkinter import ttk

class WidgetConfig:
    def __init__(self, widget_class, type, **kwargs):
        self.widget_class = widget_class
        self.type = type
        self.kwargs = kwargs

    def build_widget(self, parent):
        return self.widget_class(parent, **self.kwargs)
    
    def get_type(self):
        return self.type