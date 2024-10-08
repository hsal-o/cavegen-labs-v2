from algorithms.base_classes.base_view import BaseView
from util.grid_position import GridPosition
from widgets.checkbox_entry import CheckboxEntry
from widgets.label_entry import LabelEntry
from widgets.position_selector import PositionSelector

class RandomWalkView(BaseView):
    def __init__(self, parent):
        super().__init__(parent, "Random Walk")

    def create_widgets(self):
        self.widgets = {
            "walker_count": LabelEntry(parent=self, 
                                       type=int,
                                       label="Walker Count:", 
                                       default=1, 
                                       tooltip="The number of walkers to use"),

            "step_count": LabelEntry(parent=self, 
                                     type=int, 
                                     label="Step Count:", 
                                     default=100, 
                                     tooltip="The number of steps each walker will take"),

            "thickness": LabelEntry(parent=self, 
                                    type=int, 
                                    label="Thickness:", 
                                    default=1, tooltip="The thickness of the path drawn by the walkers"),

            "bias": CheckboxEntry(parent=self, 
                                  type=float, 
                                  label="Set Bias?", 
                                  default=(0.05, False), 
                                  tooltip="Enable or disable bias in the walker movement. If enabled, adjust the bias % value"),

            "start_position": PositionSelector(parent=self, 
                                               type=int, 
                                               label="Start Position:", 
                                               default=GridPosition.CENTER, 
                                               tooltip="The starting position for the walkers in the grid"),
            
            "end_position": PositionSelector(parent=self, 
                                             type=int, 
                                             label="End Position:", 
                                             default=GridPosition.CENTER, 
                                             tooltip="The bias ending position for the walkers in the grid"),
        }

    # def create_widgets(self):
    #     self.widget_configs = {
    #         "walker_count": WidgetConfig(LabelEntry, label="Walker Count:", default=1, type=int, tooltip="The number of walkers to use"),

    #         "step_count": WidgetConfig(LabelEntry, label="Step Count:", default=100, type=int, tooltip="The number of steps each walker will take"),

    #         "thickness": WidgetConfig(LabelEntry, label="Thickness:", default=1, type=int, tooltip="The thickness of the path drawn by the walkers"),

    #         "bias": WidgetConfig(CheckboxEntry, label="Set Bias?", default=(0.05, False), type=float, tooltip="Enable or disable bias in the walker movement. If enabled, adjust the bias % value"),

    #         "start_position": WidgetConfig(PositionSelector, label="Start Position:", default=GridPosition.CENTER, type=int, tooltip="The starting position for the walkers in the grid"),
            
    #         "end_position": WidgetConfig(PositionSelector, label="End Position:", default=GridPosition.CENTER, type=int, tooltip="The bias ending position for the walkers in the grid"),
    #     }

    