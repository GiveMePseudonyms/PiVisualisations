import pygame


class OrbitalBody:
    def __init__(self, radius, colour, xpos, ypos, surface, orbitspeed):
        self.surface = surface
        self.radius = radius
        self.colour = colour
        self.xpos = xpos
        self.ypos = ypos
        self.distance_to_sun = xpos
        self.orbitspeed = orbitspeed

    def draw_self(self):
        pygame.draw.circle(self.surface, self.colour, (self.xpos, self.ypos), self.radius, self.radius)