import tkinter as tk

class AlgoConfigurationView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.current_view = None

        self.show_placeholder()

    def show_placeholder(self):
        placeholder_frame = self.create_placeholder_view()
        self.current_view = placeholder_frame
        self.current_view.pack(fill=tk.BOTH, expand=True)

    def create_placeholder_view(self):
        placeholder_frame = tk.Frame(self)
        label = tk.Label(placeholder_frame, text="Select an Algorithm", padx=12, pady=12, relief=tk.GROOVE, borderwidth=2)
        label.pack(fill=tk.BOTH, expand=True)
        return placeholder_frame
    
    def set_view(self, algo_view):
        # Remove current view
        if self.current_view:
            self.current_view.destroy()

        # Update current view
        self.current_view = algo_view
        self.current_view.pack(fill=tk.BOTH, expand=True)
        
        
