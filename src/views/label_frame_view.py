import tkinter as tk
from abc import ABC, abstractmethod

from widgets.label_entry import LabelEntry

class LabelFrameView(tk.LabelFrame, ABC):
    def __init__(self, parent, title):
        # super().__init__(parent, text=title, relief=tk.SUNKEN, borderwidth=2)
        super().__init__(parent, text=title, relief=tk.SUNKEN, borderwidth=2)

        self.widgets = {}
        self.widget_configs = {}
        self.create_widgets()
        self.build_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def build_widgets(self):
        for key, config in self.widget_configs.items():
            widget = config.build_widget(self)
            widget.pack(fill=tk.X, padx=8, pady=4)
            self.widgets[key] = widget

    # SETTERS
    def set_settings(self, settings):
        # Iterate through the provided widget map
        for key, value in settings.items():

            # Grab widget's typing with associated key
            widget_type = self.widget_configs[key].get_type()

            # Grab widget with associated key
            widget = self.widgets[key]

            # If widget value is a tuple, convert every value to the provided typing and assign it to widget
            if isinstance(value, tuple):
                converted_value = tuple(widget_type(v) for v in value)
                widget.set(converted_value)

            # If widget value is singular, convert value to the provided typing and assign it to widget
            else:
                widget.set(widget_type(value))

    # GETTERS
    def get_settings(self):
        # Initialize empty map
        settings = {}

        # Iterate through widgets
        for key, widget in self.widgets.items():

            # Grab widget's typing from its configuration (Int, String, etc.)
            widget_type = self.widget_configs[key].get_type()

            # Grab widget value
            widget_value = widget.get()

            # If widget value is a tuple, convert every value to the provided typing and add to map
            if isinstance(widget_value, tuple):
                settings[key] = tuple(widget_type(value) for value in widget_value)

            # If widget value is singular, convert value to the provided typing and add to map
            else:
                settings[key] = widget_type(widget_value)

        return settings

    def has_empty_fields(self):
        for key, widget in self.widgets.items():
            if isinstance(widget, LabelEntry): 
                value = widget.get()
                if not value.strip():
                    return True
        return False
    
    # Abstract methods
    @abstractmethod
    def create_widgets(self):
        pass