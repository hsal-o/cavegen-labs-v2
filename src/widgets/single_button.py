import tkinter as tk

from widgets.util.custom_base_widget import CustomBaseWidget

class SingleButton(tk.Frame, CustomBaseWidget):
    def __init__(self, parent=None, type=None, label="", tooltip=None, command=None):
        super().__init__(parent)
        CustomBaseWidget.__init__(self, type, tooltip)
        self.command = command
        
        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        
        # Create and place the label
        self.button = tk.Button(self, text=label, command=self.on_click, bg="#D6DBDF", height=1)
        self.button.grid(row=0, column=0, sticky="ew")
        
    def on_click(self):
        if self.command:
            self.command()
    
    def set_command(self, command):
        self.command = command

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
