
from algorithms.base_classes.base_view import BaseView
from widgets.checkbox import Checkbox
from widgets.label_double_entry import LabelDoubleEntry
from widgets.label_entry import LabelEntry
from widgets.label_text import LabelText
from widgets.seperator import Seperator

class PerlinWormsView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Perlin Worms")

    def create_widgets(self):
        self.widgets = {
            "octaves": LabelEntry(parent=self,
                                 type=int,
                                 label="Octaves:",
                                 default=3,
                                 tooltip="Dictates the number of octats of Perlin noise to be generated. Higher values add more detail and complexity"),

            "threshold": LabelDoubleEntry(parent=self, 
                                       type=float, 
                                       label="Threshold Range:", 
                                       default=(-0.12,0.12), 
                                       tooltip="Enter a range of values. If a number falls within this range, it will be considered 'Nonsolid'"), 

            "show_raw_noise": Checkbox(parent=self,
                                       type=bool,
                                       label="Show Raw Perlin Noise",
                                       default=False,
                                       tooltip="Set True to view the raw perlin noise used for preprocessing"),

            "apply_cellular_automata": Checkbox(parent=self,
                                       type=bool,
                                       label="Apply Cellular Automata",
                                       default=True,
                                       tooltip="Set True to apply Cellular Automata for postprocessing"),

            "seperator": Seperator(parent=self),

            "border_margin": LabelEntry(parent=self,
                                     type=int,
                                     label="Border Margin:",
                                     default=5,
                                     tooltip="Width of the outer border ring where cellular automata rules are applied"),

            "iterations": LabelEntry(parent=self,
                                     type=int,
                                     label="Iterations:",
                                     default=5,
                                     tooltip="Number of iterations to run the automation"),
        
            "nonsolid_odds": LabelEntry(parent=self,
                                     type=float,
                                     label="Nonsolid Odds:",
                                     default=0.65,
                                     tooltip="Odds of cell randomly being assigned as nonsolid, in range (0,1)"),

            "label_solid_neighbors": LabelText(parent=self,
                                               label="Number of Solid neighbors to..."),

            "solidify_thresh_solid": LabelEntry(parent=self,
                                     type=int,
                                     label="Solidify:",
                                     default=4,
                                     tooltip="The minimum threshold number of solid neighbors needed for a cell to convert to solid"),

            "solidify_thresh_nonsolid": LabelEntry(parent=self,
                                     type=int,
                                     label="Nonsolidify:",
                                     default=3,
                                     tooltip="The maximum threshold number of solid neighbors needed for a cell to convert to nonsolid"),
        }