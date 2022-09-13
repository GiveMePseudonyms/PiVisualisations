import pygame

class NumberObject:

    fontSize = 24

    def __init__(self, number, xpos, ypos, colour):
        self.surface = pygame.Surface((800, 800))
        self.text = str(number)
        self.x_pos = xpos
        self.y_pos = ypos
        self.colour = colour
        self.font = pygame.font.SysFont(None, self.fontSize)
        self.img = self.font.render(self.text, True, self.colour)