import tkinter as tk
from tkinter import ttk

from algorithms import algorithms
from views.algo_configuration_view import AlgoConfigurationView
from views.grid_configuration_view import GridConfigurationView
from views.render_view import RenderView

class AppView(tk.Tk):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.title("CaveGen Labs 2.0")
        self.build_menu()
        self.build_main_frames()

    # Method to buid menubar
    def build_menu(self):
        menubar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Window", command=self.controller.handle_menu_new_window_command)
        file_menu.add_command(label="Open...", command=self.controller.handle_menu_open_command)
        file_menu.add_command(label="Save", command=self.controller.handle_menu_save_command)

        # File/Save menu
        save_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Save Image As...", menu=save_menu)
        save_menu.add_command(label="Save Graph as PNG", command=self.controller.handle_menu_save_graph_png_command)
        save_menu.add_command(label="Save Screen as PNG", command=self.controller.handle_menu_save_screen_png_command)

        # File/Exit command
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)


        # Algorithms menu
        algorithm_menu = tk.Menu(file_menu, tearoff=0)
        menubar.add_cascade(label="Algorithms", menu=algorithm_menu)
        for algo_name in algorithms.keys():
            algorithm_menu.add_command(
                label=algo_name.replace("_", " ").title(),
                command=lambda name=algo_name: self.controller.load_algorithm(name)
            )


        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Import Algorithm")
        tools_menu.add_command(label="Import Parameters")
        tools_menu.add_command(label="Import Grade Metric")


        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="User Guide")
        help_menu.add_command(label="About")

        
        # Assign menubar
        self.config(menu=menubar)

    
    def build_main_frames(self):
        # Input frame (on the left)
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=12, pady=12, expand=True)
        self.build_input_frame(input_frame)

        # Output frame (on the right)
        output_frame = tk.Frame(self)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=12, pady=12, expand=True)
        self.build_output_frame(output_frame)


    def build_input_frame(self, input_frame):
        configuration_container = tk.Frame(input_frame)
        configuration_container.pack(fill=tk.BOTH, expand=True)

        self.grid_configuration_view = GridConfigurationView(configuration_container)
        self.grid_configuration_view.pack(fill=tk.BOTH)

        self.algo_configuration_container = AlgoConfigurationView(configuration_container)
        self.algo_configuration_container.pack(fill=tk.BOTH, expand=True, pady=(12,0))

        self.generate_button = tk.Button(input_frame, text="GENERATE", command=self.controller.handle_generate_button, bg="#D6DBDF", height=2)
        self.generate_button.pack(fill=tk.BOTH, pady=(12,0))

    def _build_input_frame(self, input_frame):
        self.grid_configuration_view = GridConfigurationView(input_frame)
        self.grid_configuration_view.pack(fill=tk.BOTH, expand=True)

        self.algo_configuration_container = AlgoConfigurationView(input_frame)
        self.algo_configuration_container.pack(fill=tk.BOTH, expand=True, pady=(12,0))

        self.generate_button = tk.Button(input_frame, text="GENERATE", command=self.controller.handle_generate_button, bg="#D6DBDF", height=2)
        self.generate_button.pack(fill=tk.BOTH, expand=True, pady=(12,0))

    def build_output_frame(self, output_frame):
        self.render_view = RenderView(output_frame)
        self.render_view.pack(fill=tk.BOTH, expand=True)


    def get_algo_configuration_container(self):
        return self.algo_configuration_container
    
    def get_grid_configuration_view(self):
        return self.grid_configuration_view
    
    def get_render_view(self):
        return self.render_view

    def set_algorithm_view(self, algo_view):
        self.algo_configuration_container.set_view(algo_view)
    

   