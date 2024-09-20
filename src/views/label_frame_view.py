import tkinter as tk
from abc import ABC, abstractmethod

from widgets.util.custom_base_widget import CustomBaseWidget
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
        for key, widget in self.widgets.items():
            widget.apply_pack()
            self.widgets[key] = widget

    def set_settings(self, settings):
        # Iterate through the provided widget map
        for key, value in settings.items():

            # Grab widget's typing with associated key
            widget_type = self.widgets[key].get_type()

            # Grab widget with associated key
            widget = self.widgets[key]

            # If widget value is a tuple, convert every value to the provided typing and assign it to widget
            if isinstance(value, tuple):
                converted_value = tuple(widget_type(v) for v in value)
                widget.set(converted_value)

            # If widget value is singular, convert value to the provided typing and assign it to widget
            else:
                widget.set(widget_type(value))

    def get_settings(self):
        # Initialize empty map
        settings = {}

        # Iterate through widgets
        for key, widget in self.widgets.items():
            if widget.get_type() is not None:
                settings[key] = widget.get()

        return settings

    def get_widget(self, widget_name):
        return self.widgets.get(widget_name, None)

    def has_empty_fields(self):
        for key, widget in self.widgets.items():
            if isinstance(widget, CustomBaseWidget): 
                if(widget.is_empty()):
                    return True
        return False
    
    # Abstract methods
    @abstractmethod
    def create_widgets(self):
        pass