
from algorithms.base_classes.base_view import BaseView
from util.grid_position import GridPosition
from widgets.checkbox import Checkbox
from widgets.checkbox_entry import CheckboxEntry
from widgets.label_double_entry import LabelDoubleEntry
from widgets.label_entry import LabelEntry
from widgets.position_selector import PositionSelector
from widgets.util.widget_config import WidgetConfig

class MidpointDisplacementView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Midpoint Displacement")

    def create_widgets(self):
        self.widget_configs = {
            "start_position": WidgetConfig(PositionSelector, label="Start Position:", default=GridPosition.TOP_LEFT, type=int, tooltip="The starting position on the grid"),
            
            "end_position": WidgetConfig(PositionSelector, label="End Position:", default=GridPosition.BOTTOM_RIGHT, type=int, tooltip="The ending position on the grid"),
        
            "iteration_count": WidgetConfig(LabelEntry, label="Iteration Count:", default=5, type=int, tooltip="The number of times the midpoint is displaced"),

            "magnitude": WidgetConfig(LabelEntry, label="Magnitude", default=6, type=int, tooltip="Sets the maximum random displacement; higher values create rougher terrain"),

            "thickness": WidgetConfig(LabelEntry, label="Thickness:", default=3, type=int, tooltip="The thickness of the path drawn"),

            "vary_thickness": WidgetConfig(LabelDoubleEntry, label="ΔThickness (+/-):", default=(0,0), type=int, tooltip=""),
        }