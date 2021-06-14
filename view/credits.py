import pygame
from control.constants import *
import menu

pygame.init()


''''''
screen = pygame.display.set_mode(SIZE)

''''''
pygame.display.set_caption('Snake')

cover = pygame.image.load("../assets/3.png")
cover_rect = cover.get_rect()


def main():
    while not GAME:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu.main()
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(cover, cover_rect)
        pygame.display.update()


if __name__ == '__main__':
    main()
