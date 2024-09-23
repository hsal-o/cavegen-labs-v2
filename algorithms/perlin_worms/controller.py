from algorithms.base_classes.base_controller import BaseController
from algorithms.cellular_automata.model import CellularAutomataModel
from services.grid_configuration_service import GridConfigurationService

class PerlinWormsController(BaseController):
    def __init__(self, model, view, algo_name):
        super().__init__(model, view, algo_name)

        self.cellular_automata_model = CellularAutomataModel()

    def get_result(self, grid_config_settings):
        algo_config_settings = self.get_settings()

        # Force grab seed from grid configuration service
        grid_config_settings["seed"] = GridConfigurationService().get_seed_entry(force=True)

        # Generate raw perlin worms grid
        grid = self.model.generate(grid_config_settings, algo_config_settings)

        if not algo_config_settings["show_raw_noise"] and algo_config_settings["apply_cellular_automata"]:
            grid = self.cellular_automata_model.generate(grid_config_settings, algo_config_settings, grid) 

        return grid