import pygame
from random import *

from control.constants import *
from model.DrawInterface import DrawInterface

size = SIZE_SNAKE


'''Apple Class'''


class Apple(DrawInterface):
    def __init__(self, parent_screen):
        super().__init__()
        self.parent_screen = parent_screen
        self.image = pygame.image.load("../assets/apple.png")
        self.x = 120
        self.y = 120

    def spawn_apple(self):
        self.x = randint(5, 15) * size
        self.y = randint(5, 15) * size
