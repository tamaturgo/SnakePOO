import pygame
import menu
from control.constants import *

pygame.init()
window = pygame.display.set_mode(SIZE)
cover = pygame.image.load("../assets/2.png")
cover_rect = cover.get_rect()

pygame.display.set_caption("Snake Fire")
score = 0
click = False


"""Game Over Function"""


def game_over(score):
    global click
    while not click:
        font_2 = pygame.font.Font("../fonts/VT323-Regular.ttf", 35)
        text_2 = "Press space to back menu"
        text_3 = 'Score:' + str(score)
        text_2 = font_2.render(text_2, True, (250, 250, 250))
        text_3 = font_2.render(text_3, True, (250, 250, 250))
        text_2_rect = text_2.get_rect()
        text_3_rect = text_3.get_rect()
        text_2_rect.center = (300, 500)
        text_3_rect.center = (300, 315)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu.main()
                    click = True
        window.blit(cover, cover_rect)
        window.blit(text_2, text_2_rect)
        window.blit(text_3, text_3_rect)
        pygame.display.update()


def set_click():
    global click
    click = False


if __name__ == '__main__':
    game_over(score)
