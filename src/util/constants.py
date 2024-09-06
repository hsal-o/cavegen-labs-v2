import random

class StartPosition:
    RANDOM =        0
    TOP_LEFT =      1
    TOP_CENTER =    2
    TOP_RIGHT =     3
    CENTER_LEFT =   4
    CENTER =        5
    CENTER_RIGHT =  6
    BOTTOM_LEFT =   7
    BOTTOM_CENTER = 8
    BOTTOM_RIGHT =  9

    def determine(width, height, position):
        start_x = 0
        start_y = 0
        
        match position:
            case StartPosition.TOP_LEFT:
                start_x = 1
                start_y = 1
            case StartPosition.TOP_CENTER:
                start_x = round(width / 2)
                start_y = 1
            case StartPosition.TOP_RIGHT:
                start_x = width
                start_y = 1

            case StartPosition.CENTER_LEFT:
                start_x = 1
                start_y = round(height / 2)
            case StartPosition.CENTER:
                start_x = round(width / 2)
                start_y = round(height / 2)
            case StartPosition.CENTER_RIGHT:
                start_x = width
                start_y = round(height / 2)

            case StartPosition.BOTTOM_LEFT:
                start_x = 1
                start_y = height
            case StartPosition.BOTTOM_CENTER:
                start_x = round(width / 2)
                start_y = height
            case StartPosition.BOTTOM_RIGHT:
                start_x = width
                start_y = height

            case StartPosition.RANDOM:
                start_x = random.randint(1, width)
                start_y = random.randint(1, height)
        
        return start_x, start_y