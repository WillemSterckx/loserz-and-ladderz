import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

import random
import pygame.display
import pgzrun

WIDTH = 1920
HEIGHT = 1080

pygame.display.set_caption('backgroun image example')

background = pygame.image.load('images/snakes.jpg')

one = pygame.image.load('images/dice-six-faces-one.png')
two = pygame.image.load('images/dice-six-faces-two.png')
three = pygame.image.load('images/dice-six-faces-three.png')
four = pygame.image.load('images/dice-six-faces-four.png')
five = pygame.image.load('images/dice-six-faces-five.png')
six = pygame.image.load('images/dice-six-faces-six.png')
paper = pygame.image.load('images/paper.png')

blue = Actor("blue", (422, 830))
red = Actor("red", (422, 830))

sq = [422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422,
      422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422,
      422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422,
      422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422,
      422, 497, 572, 647, 722, 797, 872, 947, 1022, 1097,
      1097, 1022, 947, 872, 797, 722, 647, 572, 497, 422]
counterblue = 0
counterred = 0

bluepl = True

bluetile = "0"
redtile = "0"

my_font = pygame.font.SysFont('Comic Sans MS', 30)


def draw():
    screen.blit(background, (385, 120))
    blue.draw()
    red.draw()

    blue_tile = my_font.render(bluetile, False, (255, 255, 255))
    red_tile = my_font.render(redtile, False, (255, 255, 255))
    screen.blit(blue_tile, (1200, 230))
    screen.blit(red_tile, (1200, 380))
    screen.blit(paper, (1150, 0))

def move_blue():
    global counterblue
    if 10 <= counterblue <= 19:
        blue.y = 755
    elif 20 <= counterblue <= 29:
        blue.y = 680
    elif 30 <= counterblue <= 39:
        blue.y = 605
    elif 40 <= counterblue <= 49:
        blue.y = 530
    elif 50 <= counterblue <= 59:
        blue.y = 455
    elif 60 <= counterblue <= 69:
        blue.y = 380
    elif 70 <= counterblue <= 79:
        blue.y = 305
    elif 80 <= counterblue <= 89:
        blue.y = 230
    elif 90 <= counterblue <= 100:
        blue.y = 155

def move_red():
    if 10 <= counterred <= 19:
        red.y = 755
    elif 20 <= counterred <= 29:
        red.y = 680
    elif 30 <= counterred <= 39:
        red.y = 605
    elif 40 <= counterred <= 49:
        red.y = 530
    elif 50 <= counterred <= 59:
        red.y = 455
    elif 60 <= counterred <= 69:
        red.y = 380
    elif 70 <= counterred <= 79:
        red.y = 305
    elif 80 <= counterred <= 89:
        red.y = 230
    elif 90 <= counterred <= 100:
        red.y = 155


def on_key_down(key):
    global counterblue, counterred, bluepl, bluetile, redtile
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    elif key == keys.L:
        pgzrun.quit()
    elif key == keys.O:
        blue.x = sq[3]
    elif key == keys.R:
        blue.x = sq[0]
        blue.y = 830
        counterblue = 0
        bluetile = "0"

        red.x = sq[0]
        red.y = 830
        counterred = 0
        redtile = "0"

    if key == keys.SPACE:
        if bluepl:
            dice = random.randint(1, 6)
            counterblue += dice
            if counterblue > 99:
                counterblue = 99

            blue.x = sq[counterblue]

            move_blue()

            if counterblue == 3:
                counterblue = 13
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 8:
                counterblue = 30
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 20:
                counterblue = 41
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 27:
                counterblue = 83
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 50:
                counterblue = 66
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 72:
                counterblue = 90
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 79:
                counterblue = 98
                blue.x = sq[counterblue]
                move_blue()

            if counterblue == 16:
                counterblue = 6
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 53:
                counterblue = 33
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 61:
                counterblue = 18
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 63:
                counterblue = 59
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 86:
                counterblue = 35
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 91:
                counterblue = 72
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 94:
                counterblue = 74
                blue.x = sq[counterblue]
                move_blue()
            elif counterblue == 97:
                counterblue = 78
                blue.x = sq[counterblue]
                move_blue()

            screen.fill(pygame.Color("black"))
            bluetile = str((counterblue + 1))

            if dice == 1:
                screen.blit(one, (10, 200))
            elif dice == 2:
                screen.blit(two, (10, 200))
            elif dice == 3:
                screen.blit(three, (10, 200))
            elif dice == 4:
                screen.blit(four, (10, 200))
            elif dice == 5:
                screen.blit(five, (10, 200))
            elif dice == 6:
                screen.blit(six, (10, 200))

            bluepl = False

        else:
            dice = random.randint(1, 6)
            counterred += dice
            if counterred > 99:
                counterred = 99

            red.x = sq[counterred]

            move_red()

            if counterred == 3:
                counterred = 13
                red.x = sq[counterred]
                move_red()
            elif counterred == 8:
                counterred = 30
                red.x = sq[counterred]
                move_red()
            elif counterred == 20:
                counterred = 41
                red.x = sq[counterred]
                move_red()
            elif counterred == 27:
                counterred = 83
                red.x = sq[counterred]
                move_red()
            elif counterred == 50:
                counterred = 66
                red.x = sq[counterred]
                move_red()
            elif counterred == 72:
                counterred = 90
                red.x = sq[counterred]
                move_red()
            elif counterred == 79:
                counterred = 98
                red.x = sq[counterred]
                move_red()

            if counterred == 16:
                counterred = 6
                red.x = sq[counterred]
                move_red()
            elif counterred == 53:
                counterred = 33
                red.x = sq[counterred]
                move_red()
            elif counterred == 61:
                counterred = 18
                red.x = sq[counterred]
                move_red()
            elif counterred == 63:
                counterred = 59
                red.x = sq[counterred]
                move_red()
            elif counterred == 86:
                counterred = 35
                red.x = sq[counterred]
                move_red()
            elif counterred == 91:
                counterred = 72
                red.x = sq[counterred]
                move_red()
            elif counterred == 94:
                counterred = 74
                red.x = sq[counterred]
                move_red()
            elif counterred == 97:
                counterred = 78
                red.x = sq[counterred]
                move_red()

            screen.fill(pygame.Color("black"))
            redtile = str((counterred + 1))

            if dice == 1:
                screen.blit(one, (10, 200))
            elif dice == 2:
                screen.blit(two, (10, 200))
            elif dice == 3:
                screen.blit(three, (10, 200))
            elif dice == 4:
                screen.blit(four, (10, 200))
            elif dice == 5:
                screen.blit(five, (10, 200))
            elif dice == 6:
                screen.blit(six, (10, 200))
            bluepl = True



pgzrun.go()