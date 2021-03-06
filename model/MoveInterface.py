from control.constants import *

size = SIZE_SNAKE


class MoveInterface:

    def __init__(self):
        self.y = None
        self.x = None
        self.length = None
        self.direction = ''

        self.orientation_h = None
        self.orientation_v = None

    def move_left(self):
        if not self.direction == 'right':
            self.direction = 'left'

    def move_right(self):
        if not self.direction == 'left':
            self.direction = 'right'

    def move_up(self):
        if not self.direction == 'down':
            self.direction = 'up'

    def move_down(self):
        if not self.direction == 'up':
            self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size

        self.draw()

    def walk_bot(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= size
            self.orientation_h = -1
        if self.direction == 'right':
            self.x[0] += size
            self.orientation_h = 1

        if self.direction == 'up':
            self.y[0] -= size
            self.orientation_v = -1
        if self.direction == 'down':
            self.y[0] += size
            self.orientation_v = 1

        self.draw()

    def draw(self):
        pass
