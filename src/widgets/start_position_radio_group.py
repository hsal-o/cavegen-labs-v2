import tkinter as tk
from tkinter import ttk

from util.constants import StartPosition

class StartPositionRadioGroup(tk.LabelFrame):
    # def __init__(self, parent, label="Start Position", default=StartPosition.CENTER):
    #     super().__init__(parent, text=label, borderwidth=0)
    #     self.var = tk.IntVar(value=default)

    #     self.R1 = ttk.Radiobutton(self, text="Center", variable=self.var, value=StartPosition.CENTER)
    #     self.R1.pack(anchor=tk.W)

    #     self.R2 = ttk.Radiobutton(self, text="Top Left", variable=self.var, value=StartPosition.TOP_LEFT)
    #     self.R2.pack(anchor=tk.W)

    #     self.R3 = ttk.Radiobutton(self, text="Random", variable=self.var, value=StartPosition.RANDOM)
    #     self.R3.pack(anchor=tk.W)

    def __init__(self, parent, label="Start Position", default=StartPosition.CENTER):
        super().__init__(parent, text=label, borderwidth=0)
        self.var = tk.IntVar(value=default)

        self.default_bg = "lightgrey"
        self.selected_bg = "gray"
        self.selected_fg = "white"

        self.buttons = {}

        positions = {
            StartPosition.TOP_LEFT: (0, 0),
            StartPosition.TOP_CENTER: (0, 1),
            StartPosition.TOP_RIGHT: (0, 2),
            StartPosition.CENTER_LEFT: (1, 0),
            StartPosition.CENTER: (1, 1),
            StartPosition.CENTER_RIGHT: (1, 2),
            StartPosition.BOTTOM_LEFT: (2, 0),
            StartPosition.BOTTOM_CENTER: (2, 1),
            StartPosition.BOTTOM_RIGHT: (2, 2)
        }

        for position, grid_position in positions.items():
            button = tk.Button(
                self, 
                bg=self.default_bg,
                command=lambda pos=position: self.select_button(pos)
            )
            self.buttons[position] = button
            button.grid(row=grid_position[0], column=grid_position[1], sticky="nsew")

        random_button = tk.Button(
            self, 
            text="Random",
            bg=self.default_bg,
            command=lambda: self.select_button(StartPosition.RANDOM)
        )
        self.buttons[StartPosition.RANDOM] = random_button
        random_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

        for i in range(3):
            self.grid_rowconfigure(i, weight=1, uniform="1")
            self.grid_columnconfigure(i, weight=1, uniform="1")

        self.grid_rowconfigure(3, weight=1)

        self.select_button(default)

    def select_button(self, position):
        self.var.set(position)

        # Reset all buttons to unselected style
        for btn in self.buttons.values():
            btn.config(bg=self.default_bg, fg="black")

        # Highlight the selected button
        self.buttons[position].config(bg=self.selected_bg, fg=self.selected_fg)

    def set(self, value):
        self.var.set(value)

    def get(self):
        return self.var.get()