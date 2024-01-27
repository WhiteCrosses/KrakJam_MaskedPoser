import pygame
import sys

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

res = (WINDOW_WIDTH, WINDOW_HEIGHT)

class Gui:
    def __init__(self):
        pygame.init()

        

        self.window = pygame.display.set_mode(res)
        # White color of the button
        self.start_color = (240, 240, 240)
        # Light shade of the button
        self.color_light = (170, 170, 170)
        # dark shade of the button
        self.color_dark = (80, 80, 80)



        pygame.font.init()

        self.font = pygame.font.SysFont("Comic Sans MS", 34)
        self.start_game = self.font.render("Play", False, self.start_color)
        self.quit_game = self.font.render("Quit", False, self.start_color)



    def game_loop(self):
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    #If the mouse is clicked on the button the game is terminated
                    if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT / 2 <= mouse[1] <= WINDOW_HEIGHT / 2 + 40:
                        #Move to the next stae in the game
                        #is_running = False
                        print("Play")

                    # If the mouse is clicked on the button the game is terminated
                    if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT / 2 + 60 <= mouse[1] <= WINDOW_HEIGHT / 2 + 120:
                        # Move to the next stae in the game
                        is_running = False

            self.window.fill((0, 0, 0))
            mouse = pygame.mouse.get_pos()

            #If mouse is hovered on a button it changes to lighter shade
            if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT/2 <= mouse[1] <= WINDOW_HEIGHT/2 + 40:  
                pygame.draw.rect(self.window,self.color_light,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2,260,50])    
            else:  
                pygame.draw.rect(self.window,self.color_dark,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2,260,50]) 

            #If mouse is hovered on a button it changes to lighter shade
            if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT/2 + 60 <= mouse[1] <= WINDOW_HEIGHT/2 + 120:  
                pygame.draw.rect(self.window,self.color_light,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2 + 60,260,80])  
            else:  
                pygame.draw.rect(self.window,self.color_dark,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2 + 60,260,80]) 

            self.window.blit(self.start_game, (WINDOW_WIDTH/2 - 40,WINDOW_HEIGHT/2))
            self.window.blit(self.quit_game, (WINDOW_WIDTH/2 - 40, WINDOW_HEIGHT/2 + 60))
            # Update the frames of the screen
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()
        sys.exit()