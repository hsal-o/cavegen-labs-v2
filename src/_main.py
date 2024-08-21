import tkinter as tk
from tkinter import ttk
import sys
import os

from views.grid_configuration_view import GridConfigurationView

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import algorithms
from src.views.generic_input_view import GenericInputView
from src.views.output_console_view import OutputConsoleView
from views.algorithm_view_manager import AlgorithmViewManager

class MainApp:
    def __init__(self, root):
        self.root = root
        self.title = "CaveGen Labs 2.0"
        self.root.title(self.title)
        self.algo_view_manager = AlgorithmViewManager()
        self.add_menu()
        self.create_main_frames()
    
    def add_menu(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New Window', command=self.new_window)
        file_menu.add_command(label='Open...', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)

        # File/Save menu
        save_menu = tk.Menu(file_menu, tearoff=0)
        save_menu.add_command(label='Save Graph as PNG', command=self.save_graph)
        save_menu.add_command(label='Save Screen as PNG', command=self.save_screen)
        file_menu.add_cascade(label='Save Image As...', menu=save_menu) 

        # File/exit command
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.destroy)

        # Algorithms menu
        algorithm_menu = tk.Menu(file_menu, tearoff=0)
        menubar.add_cascade(label="Algorithms", menu=algorithm_menu)
        for algo_name in algorithms.keys():
            algorithm_menu.add_command(
                label=algo_name.replace('_', ' ').title(),
                command=lambda name=algo_name: self.load_algorithm_view(name)
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

        self.root.config(menu=menubar)
    
    def create_main_frames(self):
        # Create main input and output frames
        self.input_frame = ttk.Frame(self.root)
        self.output_frame = ttk.Frame(self.root)
        
        self.input_frame.pack(side='left', fill='both', expand=True)
        self.output_frame.pack(side='right', fill='both', expand=True)

        self.create_subframes()

    def create_subframes(self):
        # Create subframes for input frame
        self.generic_input_frame = tk.Frame(self.input_frame)
        # self.algo_input_frame = tk.Frame(self.input_frame)

        self.generic_input_frame.pack(fill='both', expand=True, padx=12, pady=(12, 6))
        # self.algo_input_frame.pack(fill='both', expand=True, padx=12, pady=(6, 12))

        self.add_generic_input(self.generic_input_frame)

        # self.algo_view_manager.set_parent(self.algo_input_frame)
        # self.algo_view_manager.show_placeholder()

        # self.add_console_frame(self.console_frame)

    def add_placeholder_view(self, parent):
        self.placeholder_frame = ttk.Frame(parent)
        label = ttk.Label(self.placeholder_frame, text="Select an algorithm")
        label.pack(pady=20, padx=20)
        self.placeholder_frame.pack(fill='both', expand=True)
    
    # def load_algorithm_view(self, algo_name):
    #     self.algo_view_manager.show_view(algo_name)

    def add_generic_input(self, parent_frame):
        self.generic_input_view = GridConfigurationView(parent_frame)

    def new_window(self):
        new_root = tk.Toplevel()
        MainApp(new_root)
        new_root.title(f"{self.title}*")
    
    def open_file(self):
        pass 
    
    def save_file(self):
        pass 

    def save_graph(self):
        pass 

    def save_screen(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

