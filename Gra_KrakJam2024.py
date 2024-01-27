import pygame
import sys
from music import *

pygame.init()

width = input("Enter the width of the window: ")
height = input("Enter the height of the window: ")
screen_width = int(width)
screen_height = int(height)
res = (screen_width, screen_height)

window = pygame.display.set_mode(res)
# White color of the button
start_color = (240, 240, 240)
# Light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (80, 80, 80)

is_running = True

pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 34)
start_game = font.render("Play", False, start_color)
quit_game = font.render("Quit", False, start_color)

load_music()

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            #If the mouse is clicked on the button the game is terminated
            if screen_width/2 <= mouse[0] <= screen_width/2 + 130 and screen_height / 2 <= mouse[1] <= screen_height / 2 + 40:
                #Move to the next stae in the game
                #is_running = False
                load_button_sound()
                print("Play")

            # If the mouse is clicked on the button the game is terminated
            if screen_width/2 <= mouse[0] <= screen_width/2 + 130 and screen_height / 2 + 60 <= mouse[1] <= screen_height / 2 + 120:
                # Move to the next stae in the game
                load_button_sound()
                is_running = False

    window.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()

    #If mouse is hovered on a button it changes to lighter shade
    if screen_width/2 <= mouse[0] <= screen_width/2 + 130 and screen_height/2 <= mouse[1] <= screen_height/2 + 40:  
        pygame.draw.rect(window,color_light,[screen_width/2 - 120,screen_height/2,260,50])    
    else:  
        pygame.draw.rect(window,color_dark,[screen_width/2 - 120,screen_height/2,260,50]) 

    #If mouse is hovered on a button it changes to lighter shade
    if screen_width/2 <= mouse[0] <= screen_width/2 + 130 and screen_height/2 + 60 <= mouse[1] <= screen_height/2 + 120:  
        pygame.draw.rect(window,color_light,[screen_width/2 - 120,screen_height/2 + 60,260,80])  
    else:  
        pygame.draw.rect(window,color_dark,[screen_width/2 - 120,screen_height/2 + 60,260,80]) 

    window.blit(start_game, (screen_width/2 - 40,screen_height/2))
    window.blit(quit_game, (screen_width/2 - 40, screen_height/2 + 60))
    # Update the frames of the screen
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()