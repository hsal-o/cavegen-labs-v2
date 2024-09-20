from tkinter import messagebox
from algorithms.base_classes.base_controller import BaseController

class CellularAutomataController(BaseController):
    def __init__(self, model, view, algo_name):
        super().__init__(model, view, algo_name)

        self.view.get_widget("button_generate_step").set_command(self.handle_single_generate)

    def handle_single_generate(self):
        if(self.model.get_grid() is None):
            messagebox.showerror("Error", "Generate a grid first")
            return

        algo_config_settings = self.get_settings()
        self.model.generate_iteration(algo_config_settings["solidify_thresh_solid"], algo_config_settings["solidify_thresh_nonsolid"])
        self.parent_controller.render_result(self.model.get_grid(), self.get_algo_name())