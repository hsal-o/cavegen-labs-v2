import string
from widgets.label_text import LabelText
from algorithms.base_classes.base_view import BaseView
from widgets.label_entry import LabelEntry
from widgets.seperator import Seperator
from widgets.single_button import SingleButton

class CellularAutomataView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Cellular Automata")

    def create_widgets(self):
        self.widgets = {
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

            "seperator": Seperator(parent=self),

            "button_generate_step": SingleButton(parent=self,
                                               label="GENERATE SINGLE ITERATION",
                                               command=None,
                                               tooltip="Generate a single iteration on the displayed grid. Must generate a grid before generating iteration"),
        
        }