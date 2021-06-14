import pygame
from control.constants import *
from model.DrawInterface import *
from model.MoveInterface import *

size = SIZE_SNAKE

'''Snake Class'''


class Snake(DrawInterface, MoveInterface):
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("../assets/body.png").convert()
        self.direction = ''
        self.score = 0
        self.length = 1
        self.x = [250]
        self.y = [250]

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
