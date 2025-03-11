import pgzrun
import random
import pygame.display
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "100000,0"

WIDTH = 1920
HEIGHT = 1080

pygame.display.set_caption('backgroun image example')

background = pygame.image.load('images/snakes.jpg')

player = Actor("player", (750, 375))

def draw():
    screen.blit(background, (0, 0))
    player.draw()

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    elif key == keys.L:
        pgzrun.quit()


#def update():
    #if keyboard.l:
        #pgzrun.quit()
pgzrun.go()