import tkinter as tk

from util.constants import WIDGET_WIDTH
from widgets.util.custom_base_widget import CustomBaseWidget

class Seperator(tk.Frame, CustomBaseWidget):
    def __init__(self, parent=None, type=None, tooltip=None):
        super().__init__(parent)
        CustomBaseWidget.__init__(self, type, tooltip)

        self.label = tk.Label(self, text="", anchor="w", justify="left")

        line = tk.Frame(self, bg="#A0A0A0", height=2)
        line.pack(fill=tk.X, padx=WIDGET_WIDTH, pady=7, expand=True)

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
