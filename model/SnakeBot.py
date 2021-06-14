import random
import sys
from math import sqrt

import pygame
from pygame import QUIT

from control.constants import *

size = SIZE_SNAKE


'''Snake Class'''


class SnakeBot:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("../assets/ball.png")
        self.direction = 'down'
        self.length = 1
        self.x = [random.randint(1, 15) * SIZE_SNAKE]
        self.y = [random.randint(1, 12) * SIZE_SNAKE]
        self.orientation_h = 1
        self.orientation_v = 1

    def walk(self):
        for i in range(self.length-1, 0,  -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
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
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def follow_apple(self, apple_x, apple_y):
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

        self.walk()

    def collide_with(self, apple_x, apple_y):
        distance = sqrt(pow((self.x[0] - apple_x), 2) + pow(self.y[0] - apple_y, 2))
        return distance <= 25