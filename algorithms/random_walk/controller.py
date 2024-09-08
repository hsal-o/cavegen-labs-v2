from algorithms.base_classes.base_controller import BaseController

class RandomWalkController(BaseController):
    def __init__(self, model, view, algo_name):
        super().__init__(model, view, algo_name)

        self.view.get_widget("bias").set_command(self.toggle_end_position_entry)

    def toggle_end_position_entry(self, use_bias):
        if(use_bias):
            self.view.get_widget("end_position").show()
        else:
            self.view.get_widget("end_position").hide()