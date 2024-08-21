import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RenderView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=400, height=400, background="white")
        self.pack(side=tk.LEFT)
        self.pack_propagate(False)

        self.canvas = None

    def destroy_prev_canvas(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        for child in self.winfo_children():
            child.destroy()

    def display_image(self, figure):
        self.destroy_prev_canvas()

        self.canvas = FigureCanvasTkAgg(figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    