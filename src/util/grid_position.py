import random
from enum import Enum

from services.grid_configuration_service import GridConfigurationService

class GridPosition(Enum):
    CUSTOM =        0
    RANDOM =        1
    TOP_LEFT =      2
    TOP_CENTER =    3
    TOP_RIGHT =     4
    CENTER_LEFT =   5
    CENTER =        6
    CENTER_RIGHT =  7
    BOTTOM_LEFT =   8
    BOTTOM_CENTER = 9
    BOTTOM_RIGHT =  10

    @staticmethod
    def determine(position, x=1, y=1):
        grid_configuration_service = GridConfigurationService()
        width = grid_configuration_service.get_width_entry()
        height = grid_configuration_service.get_height_entry()

        # min_width = 1
        # max_width = width
        # min_height = 1
        # max_height = height
        min_width = 0
        min_height = 0
        max_width = width-1
        max_height = height-1
        
        match position:
            # Top 
            case GridPosition.TOP_LEFT:
                x = min_width
                y = min_height
            case GridPosition.TOP_CENTER:
                x = round(width / 2)
                y = min_height
            case GridPosition.TOP_RIGHT:
                x = max_width
                y = min_height

            # Center
            case GridPosition.CENTER_LEFT:
                x = min_width
                y = round(height / 2)
            case GridPosition.CENTER:
                x = round(width / 2)
                y = round(height / 2)
            case GridPosition.CENTER_RIGHT:
                x = max_width
                y = round(height / 2)

            # Bottom
            case GridPosition.BOTTOM_LEFT:
                x = min_width
                y = max_height
            case GridPosition.BOTTOM_CENTER:
                x = round(width / 2)
                y = max_height
            case GridPosition.BOTTOM_RIGHT:
                x = max_width
                y = max_height

            # Random
            case GridPosition.RANDOM:
                x = random.randint(min_width, max_width)
                y = random.randint(min_height, max_height)

            # Custom
            case GridPosition.CUSTOM:
                # Clamp provided positions to fit in grid
                x = max(min_width, min(x, max_width))
                y = max(min_height, min(y, max_height))
        
        return x, y