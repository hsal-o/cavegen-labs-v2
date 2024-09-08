import random
from math import ceil, floor
from algorithms.base_classes.base_model import BaseModel

class RandomWalkModel(BaseModel):
    def generate(self, grid_config_settings, algo_config_settings):
        self.width = grid_config_settings["width"]
        self.height = grid_config_settings["height"]
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

        for _ in range(algo_config_settings["walker_count"]):
            start_x, start_y = algo_config_settings["start_position"]
            bias = algo_config_settings["bias"]
            end_x, end_y = algo_config_settings["end_position"]
            self.generate_steps(algo_config_settings["step_count"], bias, algo_config_settings["thickness"], start_x, start_y, end_x, end_y)

        return self.grid

    def paint_step(self, thickness, x, y):
        x_tt = ceil(thickness / 2)
        x_bt = floor(thickness / 2)

        y_tt = ceil(thickness / 2)
        y_bt = floor(thickness / 2)

        for _x in range(x - x_tt, x + x_bt):
            for _y in range(y - y_tt, y + y_bt):
                if 0 <= _x < self.width and 0 <= _y < self.height:
                    self.grid[_y][_x] = 0

    def generate_steps(self, steps, bias, thickness, start_x, start_y, end_x, end_y):
        curr_x = start_x
        curr_y = start_y
        self.paint_step(thickness, curr_x, curr_y)

        for _ in range(steps - 1):
            prev_x = curr_x
            prev_y = curr_y

            # Calculate the difference between current position and end position
            dx = end_x - curr_x
            dy = end_y - curr_y

            possible_directions = [0, 1, 2, 3]

            if bias:
                bias = max(0, min(bias, 1))

                biased_directions = []
                if dy < 0:  # North
                    biased_directions.append(0)
                if dx > 0:  # East
                    biased_directions.append(1)
                if dy > 0:  # South
                    biased_directions.append(2)
                if dx < 0:  # West
                    biased_directions.append(3)

                # Randomly decide whether to follow bias or choose a random direction
                # if random.random() < 0.05:  
                if random.random() < bias:  
                    if biased_directions:
                        next_dir = random.choice(biased_directions)
                    else:
                        next_dir = random.choice(possible_directions)  
                else:
                    next_dir = random.choice(possible_directions) 
            else:
                # No bias, purely random walk
                next_dir = random.choice(possible_directions)

            # Move the walker in the chosen direction
            if next_dir == 0:  # North
                curr_y -= 1
            elif next_dir == 1:  # East
                curr_x += 1
            elif next_dir == 2:  # South
                curr_y += 1
            elif next_dir == 3:  # West
                curr_x -= 1

            # Ensure the walker stays within grid bounds
            if curr_x < 0 or curr_x >= self.width:
                curr_x = prev_x

            if curr_y < 0 or curr_y >= self.height:
                curr_y = prev_y

            # Avoid redundant painting
            if curr_x == prev_x and curr_y == prev_y:
                continue

            self.paint_step(thickness, curr_x, curr_y)