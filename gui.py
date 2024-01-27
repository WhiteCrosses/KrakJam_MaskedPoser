import pygame
import pygame_gui
import sys
import cam
import numpy as np
import cv2
import font_map
import stars


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

res = (WINDOW_WIDTH, WINDOW_HEIGHT)

class Gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        # Ugly
        # Create cam object
        self.game_cam = cam.CamManager()
        self.font_manager = font_map.FontMap()
        self.stars_manager = stars.Stars()

        # Create game window with "res" resolution
        self.menu_window = pygame.display.set_mode(res)
        self.game_window = pygame.display.set_mode(res)


        self.bg_image_path = "./Mockup/BCG.png"
        self.clock_bg_image_path = "./Mockup/Timer.png"
        self.frame_image_path = "./Mockup/Frame.png"


        self.bg_image = pygame.image.load(self.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, res)
        
        self.timer_image = pygame.image.load(self.clock_bg_image_path)
        self.timer_image = pygame.transform.scale(self.timer_image, (230, 230))


        self.frame_image = pygame.image.load(self.frame_image_path)
        self.frame_image = pygame.transform.scale(self.frame_image, (1380, 990))


        self.timer_image_offset = (20, WINDOW_HEIGHT/2 - self.timer_image.get_height()/2)
        self.frame_image_offset = (WINDOW_WIDTH/2 - self.frame_image.get_width()/2, WINDOW_HEIGHT/2 - self.frame_image.get_height()/2)

        # Static color definitions
        # White color of the button
        self.start_color = (240, 240, 240)
        # Light shade of the button
        self.color_light = (170, 170, 170)
        # dark shade of the button
        self.color_dark = (80, 80, 80)

        self.star_score = 1

        self.font_config()

        self.manager = pygame_gui.UIManager(res)
        self.clock = pygame.time.Clock()

        timer_layout_rect = pygame.Rect(WINDOW_HEIGHT/2, WINDOW_WIDTH/2, 50, 50)


    def font_config(self):
        self.font = pygame.font.SysFont("Comic Sans MS", 34)
        self.start_game = self.font.render("Play", False, self.start_color)
        self.quit_game = self.font.render("Quit", False, self.start_color)

    def game_loop(self):
        isGameRunning = True
        self.menu_window.fill((0, 0, 0))
        while(isGameRunning):


            time_delta = self.clock.tick(60)/1000.0

            self.star_score = self.game_cam.get_percentage(self.game_cam.cam_loop())
            self.stars_surf = self.stars_manager.get_stars(self.star_score)

            opencv_image= self.convert_opencv_img_to_pygame(self.game_cam.cam_loop())
            opencv_image = pygame.transform.scale(opencv_image, (1320, 934))


            rect = pygame.Rect(WINDOW_WIDTH/2 - opencv_image.get_width()/2, WINDOW_HEIGHT/2 - opencv_image.get_height()/2, 100, 100)
            
            tmp = self.font_manager.draw_text("Hello World")

            

            self.menu_window.blit(self.bg_image, (0, 0))
            self.menu_window.blit(self.timer_image, self.timer_image_offset)
            self.menu_window.blit(opencv_image, (rect.x, rect.y))
            self.menu_window.blit(self.frame_image, self.frame_image_offset)
            self.menu_window.blit(stars, (self.menu_window.get_width() - 150, WINDOW_HEIGHT/2 - 435/2))
            
            self.menu_window.blit(tmp, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            self.manager.draw_ui(self.menu_window)
            pygame.display.update()

    def convert_opencv_img_to_pygame(self, frame):
        frame=np.rot90(frame)
        frame=pygame.surfarray.make_surface(frame) #I think the color error lies in this line?
        return frame

    def background_capture_screen(self):
        while(not self.game_cam.isBg):
            
            opencv_image= self.convert_opencv_img_to_pygame(self.game_cam.get_background())
            
            self.game_window.blit(opencv_image, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            self.manager.draw_ui(self.game_window)
            pygame.display.update()
            #pygame.display.flip()

    def gui_loop(self):
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
                        is_running = False

                    # If the mouse is clicked on the button the game is terminated
                    if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT / 2 + 60 <= mouse[1] <= WINDOW_HEIGHT / 2 + 120:
                        # Move to the next stae in the game
                        pygame.quit()
                        sys.exit()

            self.menu_window.fill((0, 0, 0))
            mouse = pygame.mouse.get_pos()

            #If mouse is hovered on a button it changes to lighter shade
            if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT/2 <= mouse[1] <= WINDOW_HEIGHT/2 + 40:  
                pygame.draw.rect(self.menu_window,self.color_light,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2,260,50])    
            else:  
                pygame.draw.rect(self.menu_window,self.color_dark,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2,260,50]) 

            #If mouse is hovered on a button it changes to lighter shade
            if WINDOW_WIDTH/2 <= mouse[0] <= WINDOW_WIDTH/2 + 130 and WINDOW_HEIGHT/2 + 60 <= mouse[1] <= WINDOW_HEIGHT/2 + 120:  
                pygame.draw.rect(self.menu_window,self.color_light,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2 + 60,260,80])  
            else:  
                pygame.draw.rect(self.menu_window,self.color_dark,[WINDOW_WIDTH/2 - 120,WINDOW_HEIGHT/2 + 60,260,80]) 

            self.menu_window.blit(self.start_game, (WINDOW_WIDTH/2 - 40,WINDOW_HEIGHT/2))
            self.menu_window.blit(self.quit_game, (WINDOW_WIDTH/2 - 40, WINDOW_HEIGHT/2 + 60))
            # Update the frames of the screen
            pygame.display.update()
            pygame.display.flip()
        
        self.game_loop()