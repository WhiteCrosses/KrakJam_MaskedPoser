import pygame
import sys
from music import *

pygame.init()

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

res = (WINDOW_WIDTH, WINDOW_HEIGHT)

window = pygame.display.set_mode(res)
# White color of the button
start_color = (240, 240, 240)
# Light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (80, 80, 80)

pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 34)
start_game = font.render("Play", False, start_color)
quit_game = font.render("Quit", False, start_color)

def game_loop():
    is_running = True
    load_music()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                #If the mouse is clicked on the button the game is terminated
                if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT / 2 <= mouse[1] <= WINDOW_HEIGHT / 2 + 40:
                    #Move to the next stae in the game
                    #is_running = False
                    load_button_sound()
                    print("Play")

                # If the mouse is clicked on the button the game is terminated
                if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT / 2 + 60 <= mouse[1] <= WINDOW_HEIGHT / 2 + 120:
                    # Move to the next stae in the game
                    is_running = False

        window.fill((0, 0, 0))
        mouse = pygame.mouse.get_pos()

        #If mouse is hovered on a button it changes to lighter shade
        if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT/2 <= mouse[1] <= WINDOW_HEIGHT/2 + 40:  
            pygame.draw.rect(window,color_light,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2,260,50])    
        else:  
            pygame.draw.rect(window,color_dark,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2,260,50]) 

        #If mouse is hovered on a button it changes to lighter shade
        if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT/2 + 60 <= mouse[1] <= WINDOW_HEIGHT/2 + 120:  
            pygame.draw.rect(window,color_light,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2 + 60,260,80])  
        else:  
            pygame.draw.rect(window,color_dark,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2 + 60,260,80]) 

        window.blit(start_game, (WINDOW_WIDTH/2 - 40,WINDOW_HEIGHT/2))
        window.blit(quit_game, (WINDOW_WIDTH/2 - 40, WINDOW_HEIGHT/2 + 60))
        # Update the frames of the screen
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

game_loop()