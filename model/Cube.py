from control.constants import *


class Cube:

    def __init__(self, POS, color, size):
        self.pos = POS
        self.dir_x = 1
        self.dir_y = 0
        self.color = color
        self.size = size

    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)
