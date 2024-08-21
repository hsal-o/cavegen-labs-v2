class BaseModel:
    def __init__(self):
        self.parameters = {}

    def set_parameters(self, parameters):
        self.parameters = parameters

    def generate(self, grid_config_settings, algo_config_settings):
        raise NotImplementedError("Method not implemented")