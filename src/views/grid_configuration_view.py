import tkinter as tk
from tkinter import ttk

from widgets.widget_config import WidgetConfig
from widgets.label_entry import LabelEntry
from widgets.checkbox_entry import CheckboxEntry

class GridConfigurationView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Grid Configuration", relief=tk.SUNKEN, borderwidth=2)

        self.widgets = {}

        self.create_widhets()
        self.build_widgets()

    def create_widhets(self):
        self.widget_configs = {
            "width": WidgetConfig(LabelEntry, label="Width:", default=32, type=int),
            "height": WidgetConfig(LabelEntry, label="Height:", default=32, type=int),
            "seed": WidgetConfig(CheckboxEntry, label="Set Seed?", default=("", False), type=str)
        }

    def build_widgets(self):
        for key, config in self.widget_configs.items():
            widget = config.build_widget(self)
            widget.pack(fill=tk.X, padx=9, pady=4)
            self.widgets[key] = widget
    
    def get_settings(self):
        settings = {}
        for key, widget in self.widgets.items():
            widget_type = self.widget_configs[key].kwargs["type"]
            settings[key] = widget_type(widget.get())
        return settings
    
    def set_settings(self, settings):
        for key, value in settings.items():
            widget = self.widgets[key]
            widget_type = self.widget_configs[key].kwargs["type"]
            widget.set(widget_type(value))

