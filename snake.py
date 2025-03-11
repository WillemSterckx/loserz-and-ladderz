import pgzrun
import random
import pygame.display

WIDTH = 1500
HEIGHT = 750

DISPLAYSURF = pygame.display.set_mode((1500, 750), pygame.FULLSCREEN)

pygame.display.set_caption('backgroun image example')

background = pygame.image.load('images/snakes.jpg')

player = Actor("player", (750, 375))

def draw():
    screen.clear()
    screen.blit(background, (0, 0))
    player.draw()

def update():
    if keyboard.l:
        pgzrun.quit()
pgzrun.go()