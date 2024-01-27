import pygame




class FontMap:
    def __init__(self):
        self.screen = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.draw_text("Hello World")



    def draw_text(self, text):
        self.char_list = [*text]
        print(self.char_list)
        index = 0
        for character in self.char_list:
            if character != " ":
                tmp = pygame.image.load("Font/"+character+".png")
                tmp = pygame.transform.scale(tmp, (20, 20))
                self.screen.blit(tmp, (index, 30))
            index += 20

        return self.screen