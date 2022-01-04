from const import *
import random

class Hexagon:
    def __init__(self, x, y, resource, value):
        self.x = x
        self.y = y
        self.resource = resource
        self.value = value

    def to_string(self):
        if self.resource == OCEAN:
            return ""
        return f"{self.resource[:2]}|{self.value}"

class Board:
    def __init__(self, width=5, rand=True):
        self.width = width
        self.height = 3*width-10
        self.num_tiles = width**2 - 6  # 2 (n(n+1)/2) - (1+2+1+2) - n
        self.expansion = width > 5
        self.random = rand
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = [[None]*self.width for i in range(self.height)]
        tile_bank = []
        value_bank = []
        for key, value in COUNT.items():
            tile_bank.extend([key]*value)

        for key, value in VALUE_COUNT.items():
            value_bank.extend([key]*value)

        if self.expansion:
            for key in COUNT.keys():
                tile_bank.extend([key]*(EXPANSION_RESOURCE_INCREASE if key != DESERT else EXPANSION_DESERT_INCREASE))
            for key in VALUE_COUNT.keys():
                if key != 2:
                    value_bank.extend([key]*EXPANSION_VALUE_INCREASE)

        random.shuffle(tile_bank)
        random.shuffle(value_bank)
        assert len(tile_bank) == len(value_bank) + 1 + self.expansion

        for y in range(self.height):
            for x in range(self.width):
                if self.inbounds(x, y):
                    resource = tile_bank.pop()
                    if resource != DESERT:
                        value = value_bank.pop()
                    else:
                        value = 0
                    grid[y][x] = Hexagon(x, y, resource, value)
                else:
                    resource = OCEAN
                    value = -1
                    grid[y][x] = Hexagon(x, y, resource, value)

        return grid

    def inbounds(self, x, y):
        r = abs(y-self.height//2)

        lower_x = (r-1) // 2
        upper_x = self.width - r // 2

        ret = not (x <= lower_x or x >= upper_x)
        return ret

    def to_string(self):
        board_string = ""
        a = False
        for x, row in enumerate(self.grid):
            a = not a
            board_string = board_string + ("     " if a else "")
            for y, entry in enumerate(row):
                board_string += entry.to_string().center(10)
            board_string += "\n\n"
        return board_string
