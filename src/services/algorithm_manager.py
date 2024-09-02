import tkinter as tk
from tkinter import ttk

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import algorithms

class AlgorithmManager:
    def __init__(self, parent):
        self.parent = parent
        self.cached_models = {}
        self.cached_views = {}
        self.cached_controllers = {}

        for algo_name in algorithms:
            self.preload_algorithm(algo_name)


    # Method to return a cached algorithm view and controller
    def load_algorithm(self, algo_name):
        if algo_name not in self.cached_models:
            self.preload_algorithm(algo_name)

        view_class = self.cached_views[algo_name]
        model_class = self.cached_models[algo_name]
        controller_class = self.cached_controllers[algo_name]

        algo_model = model_class()
        algo_view = view_class(self.parent)
        algo_controller = controller_class(algo_model, algo_view, algo_name)
        algo_view.set_controller(algo_controller)

        return algo_view, algo_controller
    

    # Method to dynamically fetch and store all algorithm MVC's
    def preload_algorithm(self, algo_name):
        class_prefix = ''.join(word.title() for word in algo_name.split('_'))
        modules = algorithms.get(algo_name)

        if modules:
            try:
                model_module = modules.get('model')
                view_module = modules.get('view')
                controller_module = modules.get('controller')
                
                self.cached_models[algo_name] = getattr(model_module, f'{class_prefix}Model')
                self.cached_views[algo_name] = getattr(view_module, f'{class_prefix}View')
                self.cached_controllers[algo_name] = getattr(controller_module, f'{class_prefix}Controller')
            except AttributeError as e:
                print(f"AttributeError: {e}")
                print(f"Module attributes: {dir(model_module)}, {dir(view_module)}, {dir(controller_module)}")
