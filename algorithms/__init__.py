import os
import importlib

def load_algorithms():
    algorithm_modules = {}
    base_path = os.path.dirname(__file__)
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path) and folder not in {'base_classes', '__pycache__'}:
            algorithm_modules[folder] = {}
            for file in os.listdir(folder_path):
                if file.endswith('.py') and file != '__init__.py':
                    module_name = file[:-3]  # Strip off '.py'
                    module = importlib.import_module(f'algorithms.{folder}.{module_name}')
                    algorithm_modules[folder][module_name] = module
    return algorithm_modules

# Load algorithms and expose them
algorithms = load_algorithms()

# print("algorithms: ", algorithms)

# __all__ = list(algorithms.keys())
