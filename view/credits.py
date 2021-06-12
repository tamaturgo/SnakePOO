import sys

import pygame
from pygame.locals import *
from control.constants import *
import menu

pygame.init()


''''''
screen = pygame.display.set_mode(SIZE)

''''''
pygame.display.set_caption('Snake Fire')
background_color = (0, 0, 0)
screen.fill(background_color)

cover = pygame.image.load("../assets/3.png")
cover_rect = cover.get_rect()


font = pygame.font.SysFont('CLIQUE', 30)
text = font.render('CLIQUE', True, pygame.Color("Blue"))
text_rect = text.get_rect()


def main():
    while not GAME:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu.main()
        screen.blit(cover, cover_rect)
        pygame.display.update()


if __name__ == '__main__':
    main()
