import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

import random
import pygame.display
import pgzrun
import pygame.mixer
import socket 
import threading
import numpy as np
kill = False

pygame.mixer.init()
pygame.mixer.music.load('sounds/lazy-day.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) #loop indefinetiely
dice_sound = sounds.dice_sound

WIDTH = 1920
HEIGHT = 1080

delay_start_time = 0
delay_duration = 2
# blindblindblindblindblindblindblindblindblindblindblindblindblindblindblindblindblindblind
noen_mode = False # Set to True to enable colorblind mode

colorblind_mode = 0 

COLORBLIND_FILTERS = {
    1: np.array([[0.43, 0.72, -0.15], [0.34, 0.57, 0.09], [-0.02, 0.03, 1.00]]),  # Deuteranopia
    2: np.array([[0.20, 0.99, -0.19], [0.16, 0.79, 0.04], [0.01, -0.01, 1.00]]),  # Protanopia
    3: np.array([[0.95, 0.05, 0.00], [0.00, 0.43, 0.57], [0.00, 0.47, 0.53]])   # Tritanopia
}

# Server setup
SERVER_IP = "0.0.0.0"  # Listen on all interfaces
SERVER_PORT = 5001

game_over = False
winner = None

pygame.display.set_caption('backgroun image example')
main_background = pygame.image.load('images/background1.jpg')
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

you_win_image_blue = pygame.image.load('images/blue_wins.jpg')
you_win_image_red = pygame.image.load('images/red_wins.jpg')

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

err_channel = pygame.mixer.Channel(0)
sound_channel = pygame.mixer.Channel(1)

speaking = False


my_font = pygame.font.SysFont('Comic Sans MS', 30)

dice = 1
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)

    print("Waiting for connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    def handle_input(input_data):
        if input_data == "SELECT":
            print("Select button pressed")
            on_key_down(keys.SPACE)  # Call the game's on_key_down function
            draw()  # Call the draw function
            pygame.display.flip()
            
            

    try:
        while True:
            data = client_socket.recv(1024).decode()
            if data:
                handle_input(data)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        client_socket.close()
        server_socket.close()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True  # Daemonize thread to exit when the main program exits
server_thread.start()

def apply_neon_filter():
    # Get the current screen image
    screen_surface = pygame.display.get_surface()
    
    # Apply a grayscale filter (common for colorblind assistance)
    grayscale = pygame.transform.laplacian(screen_surface)  # Simulated deuteranopia filter
    screen.blit(grayscale, (0, 0))
    
    # Draw the filtered image onto the screen
def apply_colorblind_filter():
    if colorblind_mode == 0:
        return  # No filter applied

    # Get the current screen image
    screen_surface = pygame.display.get_surface()
    img = pygame.surfarray.array3d(screen_surface)

    # Apply color transformation matrix
    filter_matrix = COLORBLIND_FILTERS[colorblind_mode]
    filtered_img = np.dot(img, filter_matrix.T).clip(0, 255).astype(np.uint8)

    # Update the screen with the new filtered image
    pygame.surfarray.blit_array(screen_surface, filtered_img)

def draw():
    global game_over, winner,noen_mode

    if not game_over:
        screen.blit(main_background, (0, 0))
        screen.blit(background, (385, 120))
        blue.draw()
        red.draw()
        screen.blit(paper, (1150, 200))
        blue_tile = my_font.render(bluetile, False, (0, 0, 0))
        red_tile = my_font.render(redtile, False, (0, 0, 0))
        screen.blit(blue_tile, (1200, 330))
        screen.blit(red_tile, (1200, 480))

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
    else:
        # Game Over Screen
        screen.blit(main_background, (0, 0))
        if winner == "blue":
            screen.blit(you_win_image_blue, (360, 140))
        else:
            screen.blit(you_win_image_red, (360, 140))
        
        # Display restart prompt
        restart_text = my_font.render("Press R to Restart", False, (255, 255, 255))
        screen.blit(restart_text, (620, 560))
    if colorblind_mode:
        apply_colorblind_filter()
    if noen_mode:
        apply_neon_filter()

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

    global counterblue, counterred, bluepl, bluetile, redtile, dice, game_over, winner, colorblind_mode, noen_mode, err_channel, sound_channel

    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    elif key == keys.L:
        pgzrun.quit()
    elif key == keys.B:  # Toggle colorblind mode
        colorblind_mode = (colorblind_mode + 1) % 4  # 0 → 1 → 2 → 3 → 0
        print(f"Colorblind Mode: {colorblind_mode}") 
    elif key == keys.O:
        blue.x = sq[99]
    if key == keys.N:  # Toggle colorblind mode
        noen_mode = not noen_mode
    elif key == keys.R:
        if game_over:
            # Reset the game state
            game_over = False
            winner = None
            blue.x = sq[0]
            blue.y = 830
            counterblue = 0
            bluetile = "0"
            red.x = sq[0]
            red.y = 830
            counterred = 0
            redtile = "0"
        else:
            blue.x = sq[0]
            blue.y = 830
            counterblue = 0
            bluetile = "0"
            red.x = sq[0]
            red.y = 830
            counterred = 0
            redtile = "0"
    elif key == keys.UP:  # Increase volume
        vol = min(pygame.mixer.music.get_volume() + 0.1, 1.0)
        pygame.mixer.music.set_volume(vol)
    elif key == keys.DOWN:  # Decrease volume
        vol = max(pygame.mixer.music.get_volume() - 0.1, 0.0)
        pygame.mixer.music.set_volume(vol)

    if sound_channel.get_busy():
        err_sound = pygame.mixer.Sound("sounds/err.wav")
        err_channel.play(err_sound)
    else:    
        if key == keys.SPACE or key == "SELECT":  
            key == keys.RIGHT
            if not game_over:
                dice_sound.play()
                if bluepl:
                    dice = random.randint(1, 6)
                    counterblue += dice
                    if counterblue >= 99:
                        counterblue = 99
                        game_over = True
                        winner = "blue"

                    blue.x = sq[counterblue]
                    move_blue()
                    speaking = True

                    # Play dice sound
                    dice_audio = pygame.mixer.Sound(f"sounds/dice{dice}.wav")
                    sound_channel.play(dice_audio)

                    # Play space sound
                    space_audio = pygame.mixer.Sound(f"sounds/space{counterblue + 1}.wav")
                    sound_channel.play(space_audio)

                    speaking = False

                    # Check for snakes and ladders
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

                    bluetile = str((counterblue + 1))
                    bluepl = False

                else:
                    dice = random.randint(1, 6)
                    counterred += dice
                    if counterred >= 99:
                        counterred = 99
                        game_over = True
                        winner = "red"

                    red.x = sq[counterred]
                    move_red()
                    speaking = True
                    dice_audio = pygame.mixer.Sound(f"sounds/dice{dice}.wav")
                    sound_channel.play(dice_audio)
                    space_audio = pygame.mixer.Sound(f"sounds/space{counterred + 1}.wav")
                    sound_channel.play(space_audio)

                    speaking = False

                    # Check for snakes and ladders
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

                    redtile = str((counterred + 1))
                    bluepl = True
        

pgzrun.go()