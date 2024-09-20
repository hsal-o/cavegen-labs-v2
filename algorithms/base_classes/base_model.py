from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self):
        self.parameters = {}
        self.grid = None

    def get_grid(self):
        return self.grid

    def set_parameters(self, parameters):
        self.parameters = parameters

    @abstractmethod
    def generate(self, grid_config_settings, algo_config_settings):
        pass