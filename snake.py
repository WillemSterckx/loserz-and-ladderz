import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

import random
import pygame.display
import pgzrun

WIDTH = 1920
HEIGHT = 1080

pygame.display.set_caption('backgroun image example')

background = pygame.image.load('images/snakes.jpg')

blue = Actor("blue", (422, 830))

sq = [422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422,
      422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422,]
counter = 0

def draw():
    screen.blit(background, (385, 120))
    blue.draw()

def on_key_down(key):
    global counter
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    elif key == keys.L:
        pgzrun.quit()
    elif key == keys.O:
        blue.x = sq7
    if key == keys.SPACE:
        dice = random.randint(1, 6)
        counter += dice
        blue.x = sq[counter]
        if 11 <= counter <= 20:
            blue.y = 755
        elif 21 <= counter <= 30:
            blue.y = 680
        elif 31 <= counter <= 40:
            blue.y = 605

def update():
    # Move the player with arrow keys
    if keyboard.left:
        blue.x = blue.x - 1
    elif keyboard.right:
        blue.x = blue.x + 1



pgzrun.go()