
import random

from algorithms.base_classes.base_model import BaseModel

class CellularAutomataModel(BaseModel):
    def generate(self, grid_config_settings, algo_config_settings, grid=None):
        self.width = grid_config_settings["width"]
        self.height = grid_config_settings["height"]

        # If grid is provided, use it; otherwise, generate a new one
        if grid is None:
            self.grid = self.generate_initial_grid(algo_config_settings["nonsolid_odds"])
        else:
            self.grid = grid

        # Apply iterations to the grid
        self.apply_iterations(algo_config_settings)

        return self.grid
    
    def apply_iterations(self, algo_config_settings):
        for _ in range(algo_config_settings["iterations"]):
            self.generate_iteration(algo_config_settings["solidify_thresh_solid"], algo_config_settings["solidify_thresh_nonsolid"], algo_config_settings.get("border_margin"))
    
    def generate_initial_grid(self, nonsolid_odds):
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(0, self.height):
            for x in range(0, self.width):
                # Exclude border cells
                if(y == 0 or x == 0 or y == self.height-1 or x == self.width-1):
                    grid[y][x] = 1 # Turn solid automatically
                    continue
                
                # Calculate chance
                chance = random.random()
                # Determine if cell should be nonsolid
                grid[y][x] = 0 if chance <= nonsolid_odds else 1
        return grid

    def count_solid_neighbors(self, y, x):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                # Skip calling cell
                if(dy == 0 and dx == 0):
                    continue

                # Check if neighbor is in bounds
                ny = y + dy
                nx = x + dx
                if(ny < 0 or nx < 0 or ny >= self.height or nx >= self.width):
                    continue

                # Count solid neighbors
                if(self.grid[ny][nx] == 1):
                    count += 1

        return count
    
    def generate_iteration(self, num_to_turn_solid, num_to_turn_nonsolid, border_margin=None):
        new_grid = [[self.grid[y][x] for x in range(self.width)] for y in range(self.height)]

        for y in range(0, self.height):
            for x in range(0, self.width):
                # Exclude border cells
                if(y == 0 or x == 0 or y == self.height-1 or x == self.width-1):
                    new_grid[y][x] = 1 # Turn solid automatically
                    continue

                # If border ring margin is provided, skip the inside cells
                if border_margin is not None:
                     if(y >= border_margin and y <= self.height-border_margin and x >= border_margin and x <= self.width-border_margin):
                        continue
                
                num_solid_neighbors = self.count_solid_neighbors(y, x)

                # If current cell is Solid
                if(self.grid[y][x] == 1):
                    if(num_solid_neighbors < num_to_turn_nonsolid):
                        # Cell turns nonsolid due to under/overpopulation
                        new_grid[y][x] = 0
                    else :
                        # Cell remains solid
                        new_grid[y][x] = 1
                
                # If current cell is NonSolid
                elif(self.grid[y][x] == 0):
                    if(num_solid_neighbors > num_to_turn_solid):
                        # Cell turns solid due to reproduction
                        new_grid[y][x] = 1
                    else:
                        # Cell remains nonsolid
                        new_grid[y][x] = 0

        self.grid = new_grid