import pgzrun
import random

import pygame.display

WIDTH = 1500
HEIGHT = 750

pygame.display.set_caption('backgroun image example')

background = pygame.image.load('images/wmremove-transformed_Nero_AI_Image_Upscaler_Photo_Face.webp')


player = Actor("player", (750, 375))

def draw():
    screen.clear()
    screen.blit(background, (0, 0))
    player.draw()

def update():
    if keyboard.l:
        pgzrun.quit()
pgzrun.go()