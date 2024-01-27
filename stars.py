import pygame


class Stars:
    def __init__(self):
        self.screen = pygame.Surface((265, 870), pygame.SRCALPHA)

    def get_stars(self, score):
        if score == 3:
            tmp = pygame.image.load("./Mockup/ThreeStars.png")
            
        elif score == 2:
            tmp = pygame.image.load("./Mockup/TwoStars.png")
        else:
            tmp = pygame.image.load("./Mockup/OneStar.png")
        
        tmp = pygame.transform.scale(tmp, (265, 870))
        self.screen.blit(tmp, (0, 0))
        return self.screen