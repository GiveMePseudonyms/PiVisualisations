import pygame
import math
import time
import random

import turtle_colour_palette_dictionaries

WINDOW_W = 1300
WINDOW_H = 1300

OFFSET_INCREMENT = 0.5

SCREEN_CENTRE = (WINDOW_W / 2, WINDOW_H / 2)

def update_screen():
    pygame.display.flip()


class SpiralVisualiser:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        self.surface = pygame.Surface((WINDOW_W, WINDOW_H))

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
        dist_offset = 0.000002
        running = True

        for digit in pi_string:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            if not running:
                break

            x = distance * math.sin(angle)
            y = distance * math.cos(angle)

            target_x = x + WINDOW_W / 2
            target_y = y + WINDOW_H / 2
            coord = (target_x, target_y)

            colour = turtle_colour_palette_dictionaries.starfield[digit]

            pygame.draw.circle(self.screen, colour, coord, size, size)

            angle += 0.1168
            distance += 0.1168 + dist_offset
            dist_offset += int(digit)/1000000
            if counter == target:
                pygame.display.flip()
                counter = 0
            else:
                counter += 1

        pygame.image.save(self.screen, "spiral screenshot.png")
