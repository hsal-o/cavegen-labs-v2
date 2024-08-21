import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

class RenderService:
    def __init__(self, view):
        self.view = view

    def set_view(self, view):
        self.view = view

    def render(self, grid, algo_name):
        figure = self.generate_figure(grid, algo_name)
        self.view.display_image(figure)

    def generate_figure(self, grid, algo_name):
        grid = self.color_grid(grid)
        grid = np.array(grid, dtype=np.uint8)

        figure_size = 4
        figure, ax = plt.subplots(figsize=(figure_size, figure_size))
        ax.imshow(grid)

        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title(f"{algo_name}")

        plt.close(figure)

        return figure

    def color_grid(self, grid):
        height = len(grid)
        width = len(grid[0])

        color_grid = [[None for _ in range(width)] for _ in range(height)]

        for _y in range(height):
            for _x in range(width):
                # value must be in value range [0, 1]
                # 0 = air
                # 1 = solid
                value = 255 - (grid[_y][_x] * 255)
                color_grid[_y][_x] = [value, value, value]

        return color_grid