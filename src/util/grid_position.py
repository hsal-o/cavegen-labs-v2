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
    def determine(position):
        grid_configuration_service = GridConfigurationService()
        width = grid_configuration_service.get_width_entry()
        height = grid_configuration_service.get_height_entry()

        x = None
        y = None

        match position:
            # Top 
            case GridPosition.TOP_LEFT:
                x = 1
                y = 1
            case GridPosition.TOP_CENTER:
                x = round(width / 2)
                y = 1
            case GridPosition.TOP_RIGHT:
                x = width
                y = 1

            # Center
            case GridPosition.CENTER_LEFT:
                x = 1
                y = round(height / 2)
            case GridPosition.CENTER:
                x = round(width / 2)
                y = round(height / 2)
            case GridPosition.CENTER_RIGHT:
                x = width
                y = round(height / 2)

            # Bottom
            case GridPosition.BOTTOM_LEFT:
                x = 1
                y = height
            case GridPosition.BOTTOM_CENTER:
                x = round(width / 2)
                y = height
            case GridPosition.BOTTOM_RIGHT:
                x = width
                y = height

            # Random
            case GridPosition.RANDOM:
                x = random.randint(1, width)
                y = random.randint(1, height)
        
        return x, y