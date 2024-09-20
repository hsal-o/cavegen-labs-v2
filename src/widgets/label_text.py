import tkinter as tk

from util.constants import WIDGET_WIDTH
from widgets.util.custom_base_widget import CustomBaseWidget

class LabelText(tk.Frame, CustomBaseWidget):
    def __init__(self, parent=None, type=None, label="", tooltip=None):
        super().__init__(parent)
        CustomBaseWidget.__init__(self, type, tooltip)
        
        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        
        # Create and place the label
        self.label = tk.Label(self, text=label, anchor="w", justify="left")
        self.label.grid(row=0, column=0, sticky="ew")
        
    ########################################
    # Abstract Method Implementations
    ######################################## 
    def _get_value(self):
        pass
    
    def set(self, value):
        pass

    ########################################
    # Method Overrides
    ########################################    
    def _evaluate_empty(self):
        return False
