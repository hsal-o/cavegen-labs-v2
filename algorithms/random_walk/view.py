from algorithms.base_classes.base_view import BaseView
from widgets.checkbox import Checkbox
from widgets.label_double_entry import LabelDoubleEntry
from widgets.label_entry import LabelEntry
from widgets.start_position_radio_group import StartPositionRadioGroup
from widgets.widget_config import WidgetConfig

class RandomWalkView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Random Walk")

    def create_widgets(self):
        self.widget_configs = {
            "walker_count": WidgetConfig(LabelEntry, label="Walker Count:", default=1, type=int),
            "step_count": WidgetConfig(LabelEntry, label="Step Count:", default=100, type=int),
            "thickness": WidgetConfig(LabelEntry, label="Thickness:", default=1, type=int),
            "start_position" : WidgetConfig(StartPositionRadioGroup, type=int)
        }
