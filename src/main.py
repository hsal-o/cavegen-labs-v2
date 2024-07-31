import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import algorithms
from src.services.generic_input_service import GenericInputService
from src.views.generic_input_view import GenericInputView
from src.controllers.generic_input_controller import GenericInputController

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CaveGen Labs 2.0")
        # self.root.geometry("800x600")

        self.input_service = GenericInputService.get_instance()
        
        self.addMenu()
        self.createMainFrames()
    
    def addMenu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New Window', command=self.new_window)
        file_menu.add_command(label='Open...', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.destroy)

        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Import Algorithm")
        tools_menu.add_command(label="Import Parameters")
        tools_menu.add_command(label="Import Grade Metric")

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="User Guide")
        help_menu.add_command(label="About")

        self.root.config(menu=menubar)
    
    def createMainFrames(self):
        # Create main input and output frames
        self.input_frame = ttk.Frame(self.root)
        self.output_frame = ttk.Frame(self.root)
        
        self.input_frame.pack(side='left', fill='both', expand=True)
        self.output_frame.pack(side='right', fill='both', expand=True)

        # Create subframes for input frame
        self.algo_input_frame = ttk.Frame(self.input_frame)
        self.generic_input_frame = ttk.Frame(self.input_frame)

        self.algo_input_frame.pack(side='left', fill='both', expand=True)
        self.generic_input_frame.pack(side='right', fill='both', expand=True)

        self.addNotebook(self.algo_input_frame)
        self.addGenericInput(self.generic_input_frame)
    
    def addNotebook(self, parent_frame):
        style = ttk.Style()
        style.configure('TNotebook.Tab', width=24, padding=[3, 6])
        style.configure('lefttab.TNotebook', tabposition='wn', tabmargins=[2, 5, 2, 0])
        
        notebook = ttk.Notebook(parent_frame, style='lefttab.TNotebook')

        for algo_name, modules in algorithms.items():
            class_prefix = ''.join(word.title() for word in algo_name.split('_'))
            print("class_prefix: ", class_prefix)

            try:
                # Access individual modules from the dictionary
                model_module = modules.get('model')
                view_module = modules.get('view')
                controller_module = modules.get('controller')
                
                # Get classes from the modules
                model_class = getattr(model_module, f'{class_prefix}Model')
                view_class = getattr(view_module, f'{class_prefix}View')
                controller_class = getattr(controller_module, f'{class_prefix}Controller')
                
                # Initialize algorithm's model
                algo_model = model_class()
                
                # Initialize algorithm's view
                tab_frame = ttk.Frame(notebook)
                algo_view = view_class(tab_frame, None)

                # Initialize algorithm's controller
                algo_controller = controller_class(algo_model, algo_view)
                algo_view.controller = algo_controller
                
                algo_view.get_frame().pack(fill='both', expand=True)
                notebook.add(tab_frame, text=algo_name.replace('_', ' ').title())
                
            except AttributeError as e:
                print(f"AttributeError: {e}")
                print(f"Module attributes: {dir(model_module)}, {dir(view_module)}, {dir(controller_module)}")
            
        notebook.pack(expand=True, fill='both')

    def addGenericInput(self, parent_frame):
        # label = tk.Label(parent_frame, text="Generic Input Parameters")
        # label.pack(pady=10, padx=10)
        self.generic_input_view = GenericInputView(parent_frame)
        self.generic_input_controller = GenericInputController(self.generic_input_view, self.input_service)
        self.generic_input_view.get_frame().pack(fill='both', expand=True)
        
    def new_window(self):
        pass  # Placeholder for the new window logic
    
    def open_file(self):
        pass  # Placeholder for the open file logic
    
    def save_file(self):
        pass  # Placeholder for the save file logic


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
