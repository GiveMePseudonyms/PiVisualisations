import pygame
import math
import time
import random

import turtle_colour_palette_dictionaries

GLOBAL_window_w = 1300
GLOBAL_window_h = 1300

GLOBAL_offset_increment = 0.5

GLOBAL_screen_centre = (GLOBAL_window_w / 2, GLOBAL_window_h / 2)


def update_screen():
    pygame.display.flip()


class SpiralVisualiser:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((GLOBAL_window_w, GLOBAL_window_h))
        self.surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))

        self.screen.fill(turtle_colour_palette_dictionaries.bg_colours["space black"])

        self.main_loop()

    def main_loop(self):
        # get digits from text file
        with open("10milliondigitsofpi.txt") as f:
            pi_string = f.read()
            f.close()

        # remove everything that isn't a number
        pi_string.replace('\n', '')
        number_filter = filter(str.isdigit, pi_string)
        pi_string = "".join(number_filter)

        distance = 1
        angle = 0.1
        size = 1
        counter = 0
        target = 10
        dist_off = 0.000002
        running = True

        for digit in pi_string:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            if not running:
                break

            x = distance * math.sin(angle)
            y = distance * math.cos(angle)

            target_x = x + GLOBAL_window_w / 2
            target_y = y + GLOBAL_window_h / 2
            coord = (target_x, target_y)

            colour = turtle_colour_palette_dictionaries.starfield[digit]

            pygame.draw.circle(self.screen, colour, coord, size, size)

            angle += 0.1168
            distance += 0.1168 + dist_off
            dist_off += int(digit)/1000000
            if counter == target:
                pygame.display.flip()
                counter = 0
            else:
                counter += 1

        pygame.image.save(self.screen, "spiral screenshot.png")
