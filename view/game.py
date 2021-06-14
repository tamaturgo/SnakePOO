import sys
import pygame
from pygame.locals import *
import time
import random
from control.constants import *
from game_over import *
from model.Snake import Snake
from model.Apple import Apple
from model.SnakeBot import SnakeBot


'''Constants'''
size = SIZE_SNAKE

'''Init'''
main_clock = pygame.time.Clock()
pygame.init()

pygame.display.set_caption("Snake")
surface = pygame.display.set_mode(SIZE)
cover = pygame.image.load("../assets/5.png")
cover_rect = cover.get_rect()
snake = Snake(surface)
snake_Bot = SnakeBot(surface)
apple = Apple(surface)
count = 0
aux = 5

'''Reset'''


def reset():
    global snake, apple, snake_Bot
    snake = Snake(surface)
    apple = Apple(surface)
    snake_Bot = SnakeBot(surface)
    snake.score = 0


'''Colision'''


def is_collision(x1, y1, x2, y2):
    if ((x1 + size >= x2) or (x1 >= x2)) and x1 < x2 + size:
        if ((y1 >= y2) or (y1 + size >= y2)) and y1 < y2 + size:
            return True
    return False


'''Background'''


def background():
    surface.blit(cover, cover_rect)


'''Play'''


def play():
    global count, aux, snake
    background()
    snake.walk()
    apple.draw()
    font = pygame.font.Font("../fonts/VT323-Regular.otf", 30)
    score_text = font.render("Score:" + str(snake.score), True, pygame.color.Color("White"))

    # snake eating apple scenario
    for i in range(snake.length):
        if is_collision(snake.x[i], snake.y[i], apple.x, apple.y):
            snake.score += 1
            snake.increase_length()
            apple.move()
            count += 1
            if count == aux:
                count = 0
                aux = random.randint(5, 10)

    # snake colliding with itself
    for i in range(3, snake.length):
        if is_collision(snake.x[0], snake.y[0], snake.x[i], snake.y[i]):
            score = snake.score
            show_game_over(score)

    # snake collide with walls
    if not (0 <= snake.x[0] <= SIZE[0] and 0 <= snake.y[0] <= SIZE[1]):
        score = snake.score
        show_game_over(score)

    # snake colliding with bot
    for i in range(snake_Bot.length):
        for j in range(snake.length):
            if is_collision(snake.x[j], snake.y[j], snake_Bot.x[i], snake_Bot.y[i]):
                score = snake.score
                show_game_over(score)

    # Snake Bot, start follow apple
    snake_Bot.follow_apple(apple.x, apple.y)

    # Snake Bot, check if eat apple
    if snake_Bot.collide_with(apple.x, apple.y):
        snake_Bot.increase_length()
        apple.move()

    surface.blit(score_text, (500, 50))
    pygame.display.update()
    main_clock.tick(FPS)


'''Game Over'''


def show_game_over(score):
    set_click()
    reset()
    game_over(score)


'''Run'''


def run():
    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    snake.move_left()

                if event.key == K_RIGHT:
                    snake.move_right()

                if event.key == K_UP:
                    snake.move_up()

                if event.key == K_DOWN:
                    snake.move_down()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        play()


if __name__ == '__main__':
    run()
