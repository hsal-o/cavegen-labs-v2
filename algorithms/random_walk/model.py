import random
from math import ceil, floor
from algorithms.base_classes.base_model import BaseModel

class RandomWalkModel(BaseModel):
    def generate(self, grid_config_settings, algo_config_settings):
        # return grid_config_settings, algo_config_settings
        # seed = grid_config_settings["seed"]
        # random.seed(grid_config_settings["seed"])
        # print(f"model.generate() -> seed: '{seed}'")

        self.width = grid_config_settings["width"]
        self.height = grid_config_settings["height"]
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

        for _ in range(algo_config_settings["walker_count"]):
            if(algo_config_settings["random_start"]):
                start_x = random.randint(0, grid_config_settings["width"]-1)
                start_y = random.randint(0, grid_config_settings["height"]-1)
            else:
                start_x, start_y = algo_config_settings["start_coords"]

            self.generate_steps(algo_config_settings["step_count"], algo_config_settings["stroke_thickness"], start_x, start_y)


        return self.grid

    def paint_step(self, stroke_thickness, x, y):
        x_tt = ceil(stroke_thickness / 2)
        x_bt = floor(stroke_thickness / 2)

        y_tt = ceil(stroke_thickness / 2)
        y_bt = floor(stroke_thickness / 2)

        for _x in range(x - x_tt, x + x_bt):
            for _y in range(y - y_tt, y + y_bt):
                if(_x >= 0 and _x < self.width and _y >= 0 and _y < self.height):
                    self.grid[_y][_x] = 0

    def generate_steps(self, steps, stroke_thickness, start_x, start_y):
        curr_x = start_x
        curr_y = start_y
        self.paint_step(stroke_thickness, curr_x, curr_y)
        for _ in range(0, steps-1):
            prev_x = curr_x
            prev_y = curr_y

            next_dir = random.randint(0, 3)
            if(next_dir == 0): # North
                curr_y -= 1
            elif(next_dir == 1): # East
                curr_x += 1
            elif(next_dir == 2): # South
                curr_y += 1
            elif(next_dir == 3): # West
                curr_x -= 1

            if(curr_x < 0 or curr_x >= self.width):
                curr_x = prev_x

            if(curr_y < 0 or curr_y >= self.height):
                curr_y = prev_y

            # # Avoid redundant painting
            if(curr_x == prev_x and curr_y == prev_y):
                continue

            self.paint_step(stroke_thickness, curr_x, curr_y)


        