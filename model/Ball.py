
import pygame
from control.constants import *
from random import *
from math import radians, cos, sin


'''Ball Class'''


class Ball:
    def __init__(self, parent_screen):
        self.dx = 1
        self.image = pygame.image.load("../assets/ball.png")
        self.parent_screen = parent_screen
        self.dy = 1
        self.speed = 5
        self.MIN_SPEED = 5
        self.MAX_SPEED = 9
        self.x = 300
        self.y = 300
        self.randomize_angle()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.movement()
        self.collision_with_wall()

    def movement(self):
        # Ball movement
        self.x += self.speed * self.dx
        self.y += self.speed * self.dy

    def collision_with_wall(self):
        # Ball collision with the wall
        if self.x > 550:
            if self.y < 550:
                self.x = 550
                self.dx *= -1

        if self.x < 0:
            if self.y < 520:
                self.x = 0
                self.dx *= -1

        if self.y < 0:
            self.y = 0
            self.dy *= -1

        if self.y > 550:
            self.y = 550
            self.dy *= -1

    def randomize_angle(self):
        random_angle = randint(30, 60)
        angle = radians(random_angle)
        self.dx = cos(angle)
        self.dy = sin(angle)

    def restart_ball(self):
        self.randomize_angle()
        self.dy = randint(-1, 1)
        self.speed = self.MIN_SPEED
