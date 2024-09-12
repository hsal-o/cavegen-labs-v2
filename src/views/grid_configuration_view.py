import string
from tkinter import messagebox
from views.label_frame_view import LabelFrameView
from widgets.util.widget_config import WidgetConfig
from widgets.label_entry import LabelEntry
from widgets.checkbox_entry import CheckboxEntry

class GridConfigurationView(LabelFrameView):
    def __init__(self, parent):
        super().__init__(parent, "Grid Configuration")

    def create_widgets(self):
        self.widget_configs = {
            "width": WidgetConfig(LabelEntry, 
                                  label="Width:", 
                                  default=32, 
                                  type=int, 
                                  tooltip="Width of the generated grid"),
            "height": WidgetConfig(LabelEntry, 
                                   label="Height:", 
                                   default=32, type=int, 
                                   tooltip="Height of the generated grid"),
            "seed": WidgetConfig(CheckboxEntry, 
                                 label="Set Seed?", 
                                 default=("", False), 
                                 type=int, 
                                 tooltip=("Enable or disable the use of a specific seed for random number generation. "
                                          "If enabled, enter the seed value; if disabled, random seeds will be used"))
        }

    def get_width_entry(self):
        return int(self.widgets["width"].get())
    
    def get_height_entry(self):
        return int(self.widgets["height"].get())

    def get_seed_entry(self):
        # Return none if user wants to generate random seed
        if(not self.widgets["seed"].is_active()):
            return None
        
        # Return seed entry if user wants to use set seed
        return int(self.widgets["seed"].get())
    
    def set_seed_entry(self, seed):
        self.widgets["seed"].set(seed)
