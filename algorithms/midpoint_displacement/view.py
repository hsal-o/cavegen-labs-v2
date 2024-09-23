
from algorithms.base_classes.base_view import BaseView
from util.grid_position import GridPosition
from widgets.label_double_entry import LabelDoubleEntry
from widgets.label_entry import LabelEntry
from widgets.position_selector import PositionSelector

class MidpointDisplacementView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Midpoint Displacement")

    def create_widgets(self):
        self.widgets = {
            "start_position": PositionSelector(parent=self, 
                                               type=int, 
                                               label="Start Position:", 
                                               default=GridPosition.TOP_LEFT, 
                                               tooltip="The starting position on the grid"),
            
            "end_position": PositionSelector(parent=self, 
                                             type=int, 
                                             label="End Position:", 
                                             default=GridPosition.BOTTOM_RIGHT, 
                                             tooltip="The ending position on the grid"),
        
            "iteration_count": LabelEntry(parent=self, 
                                          type=int, 
                                          label="Iteration Count:", 
                                          default=5, 
                                          tooltip="The number of times the midpoint is displaced"),

            "magnitude": LabelEntry(parent=self, 
                                    type=int, 
                                    label="Magnitude", 
                                    default=6, 
                                    tooltip="Sets the maximum random displacement; higher values create rougher terrain"),

            "thickness": LabelEntry(parent=self, 
                                    type=int, 
                                    label="Thickness:", 
                                    default=3, 
                                    tooltip="The thickness of the path drawn"),

            "vary_thickness": LabelDoubleEntry(parent=self, 
                                               type=int, 
                                               label="ΔThickness (+/-):", 
                                               default=(0,0), 
                                               tooltip="Adjust the variation in thickness. Positive and negative values will increase or decrease the width range"),
        }