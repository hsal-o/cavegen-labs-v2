from controllers.label_frame_controller import LabelFrameController

class BaseController(LabelFrameController):
    def __init__(self, model, view, algo_name):
        self.model = model
        self.view = view
        self.algo_name = " ".join(word.capitalize() for word in algo_name.split("_"))

    def get_algo_name(self):
        return self.algo_name

    def get_result(self, grid_config_settings):
        # Grab algorithm parameters
        algo_config_settings = self.get_settings()

        # Generate grid
        grid = self.model.generate(grid_config_settings, algo_config_settings)
        
        return grid