from algorithms.base_classes.base_view import BaseView
from widgets.checkbox import Checkbox
from widgets.label_double_entry import LabelDoubleEntry
from widgets.label_entry import LabelEntry
from widgets.widget_config import WidgetConfig

class RandomWalkView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Random Walk")

    def create_widgets(self):
        self.widget_configs = {
            "walker_count": WidgetConfig(LabelEntry, label="Walker Count:", default=1, type=int),
            "step_count": WidgetConfig(LabelEntry, label="Step Count:", default=100, type=int),
            "stroke_thickness": WidgetConfig(LabelEntry, label="Stroke Thickness:", default=1, type=int),
            "start_coords" : WidgetConfig(LabelDoubleEntry, label="Start (x, y):", default=(0, 0), type=int),
            "random_start" : WidgetConfig(Checkbox, label="Random Start Position", default=False, type=bool)
        }
        