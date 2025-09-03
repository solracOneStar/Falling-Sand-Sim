import random
import colorsys

class SandParticle:
    def __init__(self):
        # ASSIGN A RANDOM SAND COLOR (SANDY TONES)
        # RANDOM_COLOR FUNC IS USED TO CREATE A COLOR WITHIN HSV RANGES
        self.color = random_color((0.1, 0.12), (0.5, 0.7), (0.7, 0.9))

    def update(self, grid, row, column):
        """
        DETERMINES HOW SAND PARTICLES MOVE IN GRID
        - IF CELL BELOW IS EMPTY, FALL
        - IF CELL BELOW IS FULL, TRY FALLING DIAGONALLY
        - IF NOWHERE TO FALL, STAY
        RETURNS THE NEW POSITION
        """
        if grid.is_cell_empty(row + 1, column): # FALL DOWNWARD
            return row + 1, column
        else:
            offsets = [-1, 1] # DIAGONAL DIRECTIONS (LEFT OR RIGHT)
            random.shuffle(offsets) # RANDOMIZE FALL PATTERN
            for offset in offsets:
                new_column = column + offset
                if grid.is_cell_empty(row + 1, new_column): # TRY DIAGONAL FALL
                    return row + 1, new_column

        return row, column # STAY IF NOWHERE TO FALL

class RockParticle:
    def __init__(self):
        # ASSIGN RANDOM ROCK-ISH COLOR TO ROCK
        self.color = random_color((0.0, 0.1), (0.1, 0.3), (0.3, 0.5))

def random_color(hue_range, saturation_range, value_range):
    # GENERATE RANDOM RGB COLOR USING HSV
    hue = random.uniform(*hue_range) # CONTROLS BASE COLOR
    saturation = random.uniform(*saturation_range) # CONTROLS INTENSITY
    value = random.uniform(*value_range) # CONTROLS BRIGHTNESS
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    return int(r * 255), int(g * 255), int(b * 255)
