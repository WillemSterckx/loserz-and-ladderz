import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
import random
import pygame.display
import pgzrun


WIDTH = 1920
HEIGHT = 1080

pygame.display.set_caption('backgroun image example')

background = pygame.image.load('images/snakes.jpg')

player = Actor("player", (675, 795))

def draw():
    screen.blit(background, (385, 120))
    player.draw()

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    elif key == keys.L:
        pgzrun.quit()

def update():
    # Move the player with arrow keys
    if keyboard.left:
        player.x = player.x - 1
    elif keyboard.right:
        player.x = player.x + 1

# def update():

pgzrun.go()