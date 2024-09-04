import random
from math import ceil, floor
from algorithms.base_classes.base_model import BaseModel
from util.constants import StartPosition

class RandomWalkModel(BaseModel):
    def generate(self, grid_config_settings, algo_config_settings):
        self.width = grid_config_settings["width"]
        self.height = grid_config_settings["height"]
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

        for _ in range(algo_config_settings["walker_count"]):
            start_x, start_y = StartPosition.determine(self.width, self.height, algo_config_settings["start_position"])
            self.generate_steps(algo_config_settings["step_count"], algo_config_settings["thickness"], start_x, start_y)

        return self.grid

    def paint_step(self, thickness, x, y):
        x_tt = ceil(thickness / 2)
        x_bt = floor(thickness / 2)

        y_tt = ceil(thickness / 2)
        y_bt = floor(thickness / 2)

        for _x in range(x - x_tt, x + x_bt):
            for _y in range(y - y_tt, y + y_bt):
                if(_x >= 0 and _x < self.width and _y >= 0 and _y < self.height):
                    self.grid[_y][_x] = 0

    def generate_steps(self, steps, thickness, start_x, start_y):
        curr_x = start_x
        curr_y = start_y
        self.paint_step(thickness, curr_x, curr_y)
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

            self.paint_step(thickness, curr_x, curr_y)


        