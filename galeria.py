import pygame
import cv2
import sys
from music import *
from PIL import Image

pygame.init()
pygame.font.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

res = (WINDOW_WIDTH, WINDOW_HEIGHT)

window = pygame.display.set_mode(res)

def top_derp_frame_img_load():
    return pygame.image.load(top_derp_frame_path)

def top_derp_frame_img_scale():
    return pygame.transform.scale(top_derp_frame_image_load, (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4))

# Setting the path of images
bg_image_path = "./Galeria/BCHTD.png"
top_menu_image_path = "./Galeria/TopMenu.png"
top_derp_image_path = "./Galeria/TopDerpBcg.png"
arrow_image_path = "./Galeria/ArrowTD.png"
top_derp_frame_path = "./Galeria/TopDerpFrame.png"

# Loading images
bg_image_load = pygame.image.load(bg_image_path)
top_menu_image_load = pygame.image.load(top_menu_image_path)
top_derp_image_load = pygame.image.load(top_derp_image_path)
arrow_image_1_load = pygame.image.load(arrow_image_path)
arrow_image_2_load = pygame.image.load(arrow_image_path)
top_derp_frame_image_load = top_derp_frame_img_load()

# Set the scale of images
bg_image = pygame.transform.scale(bg_image_load, res)
top_menu_image = pygame.transform.scale(top_menu_image_load, (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4))
top_derp_image = pygame.transform.scale(top_derp_image_load, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
arrow_image_1 = pygame.transform.scale(arrow_image_1_load, (WINDOW_WIDTH / 6, WINDOW_HEIGHT / 6))
arrow_image_2 = pygame.transform.scale(arrow_image_2_load, (WINDOW_WIDTH / 6, WINDOW_HEIGHT / 6))
arrow_image_2 = pygame.transform.rotate(arrow_image_2, 180)
top_derp_frame_1 = top_derp_frame_img_scale()
top_derp_frame_2 = top_derp_frame_img_scale()
top_derp_frame_3 = top_derp_frame_img_scale()

def game_loop():
    is_running = True
    load_music()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        
        window.blit(bg_image, (0, 0))
        window.blit(top_derp_image, (WINDOW_WIDTH / 2 - 480, 0))
        window.blit(top_menu_image, (WINDOW_WIDTH / 2 - 240, 120))
        window.blit(arrow_image_1, (WINDOW_WIDTH / 4 - 240, WINDOW_HEIGHT / 3))
        window.blit(arrow_image_2, (WINDOW_WIDTH / 2 + 340, WINDOW_HEIGHT / 3))
        window.blit(top_derp_frame_1, (WINDOW_WIDTH / 2 - 740, WINDOW_HEIGHT / 2 + 80))
        window.blit(top_derp_frame_2, (WINDOW_WIDTH / 2 - 240, WINDOW_HEIGHT / 2 + 80))
        window.blit(top_derp_frame_3, (WINDOW_WIDTH / 2 + 260, WINDOW_HEIGHT / 2 + 80))

        # Update the frames of the screen
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

game_loop()