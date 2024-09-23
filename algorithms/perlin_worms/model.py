import random
from perlin_noise import PerlinNoise
from algorithms.base_classes.base_model import BaseModel

class PerlinWormsModel(BaseModel):
    def generate(self, grid_config_settings, algo_config_settings):
        self.initialize_grid(grid_config_settings)

        self.seed = grid_config_settings["seed"]
        self.lower_bound, self.upper_bound = algo_config_settings["threshold"]
        
        self.generate_perlin_noise(
            width=grid_config_settings["width"], 
            height=grid_config_settings["height"], 
            octave=algo_config_settings["octaves"], 
            show_raw_noise=algo_config_settings["show_raw_noise"])
        
        return self.grid

    def initialize_grid(self, grid_config_settings):
        self.grid = [[1 for _ in range(grid_config_settings["width"])] for _ in range(grid_config_settings["height"])]

    def generate_perlin_noise(self, width, height, octave, show_raw_noise):
        noise = PerlinNoise(octaves=octave, seed=self.seed)

        for y in range(height):
            for x in range(width):
                perlin_noise_value = self.get_normalized_perlin_value(noise, x, y, width, height)

                if show_raw_noise:
                    self.grid[y][x] = (perlin_noise_value + 1) * 0.5 # Normalize value to fit in range [0, 1]
                else:
                    self.apply_perlin_worm_point(x, y, perlin_noise_value)

    def get_normalized_perlin_value(self, noise, x, y, width, height):
        normalized_x = x / width
        normalized_y = y / height
        return noise([normalized_x, normalized_y])

    def apply_perlin_worm_point(self, x, y, perlin_noise_value):
        if self.lower_bound < perlin_noise_value < self.upper_bound:
            self.grid[y][x] = 0
        else:
            self.grid[y][x] = 1
