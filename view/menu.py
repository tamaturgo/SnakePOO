import sys

import credits
import game
from game import *

main_clock = pygame.time.Clock()

pygame.init()


''''''
screen = pygame.display.set_mode(SIZE)

''''''
pygame.display.set_caption('Snake Fire')
cover = pygame.image.load("../assets/1.png")
cover_rect = cover.get_rect()

background_color = (0, 0, 0)
screen.fill(background_color)


font = pygame.font.Font("../fonts/VT323-Regular.ttf", 38)
text_play = font.render('PLAY', True, pygame.Color("White"))
text_rect_play = text_play.get_rect()
text_rect_play.center = (300, 270)

text_credits = font.render('CREDITS', True, pygame.Color("White"))
text_rect_credits = text_credits.get_rect()
text_rect_credits.center = (300, 380)


text_exit = font.render('EXIT', True, pygame.Color("White"))
text_rect_exit = text_exit.get_rect()
text_rect_exit.center = (300, 480)


def main():
    CLICK = False
    while not GAME:
        pos_x, pos_y = pygame.mouse.get_pos()

        if text_rect_play.collidepoint((pos_x, pos_y)):
            if CLICK:
                game.run()

        if text_rect_credits.collidepoint((pos_x, pos_y)):
            if CLICK:
                credits.main()

        if text_rect_exit.collidepoint((pos_x, pos_y)):
            if CLICK:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    CLICK = True

        screen.blit(cover, cover_rect)
        screen.blit(text_play, text_rect_play)
        screen.blit(text_credits, text_rect_credits)
        screen.blit(text_exit, text_rect_exit)
        pygame.display.update()
        main_clock.tick(FPS)


if __name__ == '__main__':
    main()
