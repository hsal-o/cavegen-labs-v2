import tkinter as tk
from tkinter import messagebox
from PIL import Image
import numpy as np
import random

from exceptions.empty_field_error import EmptyFieldError
from services.grid_configuration_service import GridConfigurationService
from services.render_service import RenderService
from services.algorithm_manager import AlgorithmManager
from views.app_view import AppView

class AppController:
    def __init__(self, view=None):
        self.view = view
        self.algo_controller = None
        self.algo_manager = None
        self.grid_config_service = None
        self.render_service = None

    def set_view(self, view):
        self.view = view
        self.algo_manager = AlgorithmManager(self.view.get_algo_configuration_container())
        self.grid_config_service = GridConfigurationService(self.view.get_grid_configuration_view())
        self.render_service = RenderService(self.view.get_render_view())

    def handle_menu_new_window_command(self):
        new_controller = AppController()
        new_view = AppView(new_controller)
        new_controller.set_view(new_view)
        new_view.title(self.view.title())
        new_view.mainloop()

    def handle_menu_open_command(self):
        pass

    def handle_menu_save_command(self):
        pass

    def handle_menu_save_graph_png_command(self):
        pass

    def handle_menu_save_screen_png_command(self):
        pass

    def handle_generate_button(self):
        if(self.algo_controller == None):
            messagebox.showerror("Error", "Select an Algorithm before generating")
            return
        
        try:
            # Grab configuration parameters
            grid_config_settings = self.grid_config_service.get_settings()

            self.handle_seed()

            # Grab generated result
            result = self.algo_controller.get_result(grid_config_settings)

            # Render the grid
            self.render_service.render(result, self.algo_controller.get_algo_name())        
        
        except EmptyFieldError as e:
            messagebox.showerror("Error", str(e))
            return

    def generate_seed(self):
        return random.randint(0, 2**32 - 1)
    
    def handle_seed(self):
        seed = self.grid_config_service.get_seed_entry() or self.generate_seed()
        random.seed(seed)
        self.grid_config_service.set_seed_entry(seed)

    def load_algorithm(self, algo_name):
        algo_view, self.algo_controller = self.algo_manager.load_algorithm(algo_name)
        self.view.set_algorithm_view(algo_view)
