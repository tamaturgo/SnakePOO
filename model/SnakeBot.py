import random
from math import sqrt

import pygame

from control.constants import *
from model.Snake import Snake

size = SIZE_SNAKE

'''Snake Class'''


class SnakeBot(Snake):
    def __init__(self, parent_screen):
        super().__init__(parent_screen)
        self.image = pygame.image.load("../assets/bodyEnemy.png")
        self.direction = 'down'
        self.length = 1
        self.x = [random.randint(1, 15) * SIZE_SNAKE]
        self.y = [random.randint(1, 12) * SIZE_SNAKE]
        self.orientation_h = 1
        self.orientation_v = 1

    def follow_apple(self, apple_x):
        if (self.x[0] > 700) and (self.y[0] > 532) and self.orientation_h == 1 and self.orientation_v == 1:
            self.direction = 'up'

        elif (apple_x - 10 <= self.x[0] <= apple_x + 10) and self.orientation_v == -1:
            self.direction = 'down'

        elif (self.x[0] < 50) and (self.y[0] < 50) and self.orientation_h == -1:
            self.direction = 'down'

        elif self.y[0] > 532:
            self.direction = 'right'

        elif self.y[0] < 50:
            self.direction = 'left'

        self.walk_bot()

    def collide_with(self, apple_x, apple_y):
        distance = sqrt(pow((self.x[0] - apple_x), 2) + pow(self.y[0] - apple_y, 2))
        return distance <= 25
