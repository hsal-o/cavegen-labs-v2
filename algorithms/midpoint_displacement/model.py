import random
from math import ceil, floor

from algorithms.base_classes.base_model import BaseModel

class MidpointDisplacementModel(BaseModel):
    def generate(self, grid_config_settings, algo_config_settings):
        self.width = grid_config_settings["width"]
        self.height = grid_config_settings["height"]
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

        start_x, start_y = algo_config_settings["start_position"]
        end_x, end_y = algo_config_settings["end_position"]
        magnitude = algo_config_settings["magnitude"]
        iteration_count = algo_config_settings["iteration_count"]
        thickness = algo_config_settings["thickness"]
        vary_thickness = algo_config_settings["vary_thickness"]

        points = self.generate_points(start_x, start_y, end_x, end_y, magnitude, iteration_count)
        self.connect_points(points, thickness, vary_thickness)

        return self.grid

    ################################################################################
    # Algorithm specific methods
    ################################################################################
    def generate_points(self, x1, y1, x2, y2, magnitude, step):
        if step == 0:
            return [(x1, y1), (x2, y2)]

        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2

        new_midpoint_x = midpoint_x + random.randint(-magnitude, magnitude)
        new_midpoint_y = midpoint_y + random.randint(-magnitude, magnitude) # Can cross itself
        # new_midpoint_y = midpoint_y # Cannot cross itself

        # Clamp new_midpoint_x and new_midpoint_y within grid bounds
        new_midpoint_x = max(0, min(new_midpoint_x, self.width - 1))
        new_midpoint_y = max(0, min(new_midpoint_y, self.height - 1))

        points_start = self.generate_points(x1, y1, new_midpoint_x, new_midpoint_y, magnitude, step-1)
        points_end = self.generate_points(new_midpoint_x, new_midpoint_y, x2, y2, magnitude, step-1)

        return points_start + [(new_midpoint_x, new_midpoint_y)] + points_end
    
    def connect_points(self, points, stroke_thickness, vary_thickness):
        for i in range(len(points)-1):
            self.draw_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], stroke_thickness, vary_thickness)
            
    def draw_line(self, x1, y1, x2, y2, stroke_thickness, vary_thickness):
        # Convert floating-point coordinates to integers
        x1, y1 = int(x1), int(y1)
        x2, y2 = int(x2), int(y2)

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        if vary_thickness != (0,0):
            vary_thickness_inc, vary_thickness_dec = vary_thickness
            new_thickness = stroke_thickness + random.choice([-vary_thickness_dec, vary_thickness_inc])
        else:
            new_thickness = stroke_thickness

        max_iterations = self.width * self.height  # Safety check for maximum iterations
        iterations = 0

        while True:
            # Ensure x1 and y1 are within bounds before modifying grid
            if 0 <= x1 < self.width and 0 <= y1 < self.height:
                x_thickness = new_thickness - 1
                x_tt = ceil(x_thickness / 2)
                x_bt = floor(x_thickness / 2)

                y_thickness = new_thickness - 1 #new_thickness
                y_tt = ceil(y_thickness / 2)
                y_bt = floor(y_thickness / 2)

                for _x in range(max(0, x1 - x_tt), min(self.width, x1 + x_bt + 1)):
                    for _y in range(max(0, y1 - y_tt), min(self.height, y1 + y_bt + 1)):
                        self.grid[_y][_x] = 0 # Air 

            if x1 == x2 and y1 == y2:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

            iterations += 1
            if iterations > max_iterations:
                print(f"Safety check triggered: iterations exceeded {max_iterations}")
                break
