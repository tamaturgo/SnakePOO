import pygame
from random import *

from control.constants import *

size = SIZE_SNAKE


'''Apple Class'''


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("../assets/arthur_santos_apple.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = randint(5, 20) * size
        self.y = randint(5, 20) * size
