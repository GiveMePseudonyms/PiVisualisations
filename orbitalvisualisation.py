import math
import random

import pygame
from orbitalbody import OrbitalBody
import turtle_colour_palette_dictionaries

GLOBAL_window_w = 1200
GLOBAL_window_h = 1200

GL_line_transparency = 70


def update_screen():
    pygame.display.flip()


class OrbitalVisualisation:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Orbital Visualiser")
        self.screen = pygame.display.set_mode((GLOBAL_window_w, GLOBAL_window_h))
        self.surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))

        self.screen.fill(turtle_colour_palette_dictionaries.bg_colours["space black"])

        update_screen()

        self.offset = 15
        self.edge_margin = 20

        self.main_loop()

    def main_loop(self):
        centre_x = GLOBAL_window_w / 2
        centre_y = GLOBAL_window_h / 2

        body_surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))

        line_surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))
        line_surface.set_colorkey((0, 0, 0))
        line_surface.set_alpha(GL_line_transparency)

        sun = OrbitalBody(50, (255, 255, 0), centre_x, centre_y, body_surface, 0)
        sun.draw_self()
        self.blit_onto_main(sun)

        earth = OrbitalBody(10, (0, 100, 255), centre_x + 100, centre_y, body_surface, 10)
        earth.distance_to_sun = sun.xpos - earth.xpos
        earth.draw_self()
        self.blit_onto_main(earth)

        pi_planet = OrbitalBody(5, (0, 255, 100), earth.xpos + 314, centre_y, body_surface, 31.415926)
        pi_planet.distance_to_sun = sun.xpos - pi_planet.xpos
        pi_planet.draw_self()
        self.blit_onto_main(pi_planet)

        update_screen()

        moving_body_list = [earth, pi_planet]

        index = 1

        line_interval = 1
        counter = 0

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            for item in moving_body_list:
                angle = (item.orbitspeed / 1000) * index
                item.xpos = centre_x + item.distance_to_sun * math.sin(angle)
                item.ypos = centre_y + item.distance_to_sun * math.cos(angle)
                index += 2
            body_surface.fill((0, 0, 0))
            earth.draw_self()
            pi_planet.draw_self()
            sun.draw_self()

            self.blit_onto_main(sun)
            self.blit_onto_main(earth)
            self.blit_onto_main(pi_planet)
            counter += 1

            if counter == line_interval:
                r = random.uniform(0, 255)
                g = random.uniform(0, 255)
                b = random.uniform(0, 255)
                counter = 0
                pygame.draw.aaline(line_surface, (r, g, b), (earth.xpos, earth.ypos), (pi_planet.xpos, pi_planet.ypos), 1)

            self.screen.blit(line_surface, (0, 0))

            update_screen()

        pygame.image.save(self.screen, "orbital visualisation.png")
        pygame.quit()

    def blit_onto_main(self, obj):
        self.screen.blit(obj.surface, (0, 0))
