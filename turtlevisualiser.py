import pygame.time

import turtle_colour_palette_dictionaries
import turtle
import hare
from turtle import *
from PIL import Image
import time as t
import cProfile
import pathlib

import utils

WINDOW_W = 800
WINDOW_H = 800

WAIT_UNTIL_DONE = True #never implemented, remove from settings options?
FRAME_SKIP_INTERVAL = 10000 #''

# TARGET = 1000000

# MOVE_DISTANCE = 0.8

OUTPUT_FILENAME = "screenshot" #never implemented, remove

# DIGIT_IS_COLOUR = False
# DIGIT_COLOUR_PALETTE = "starfield"

# self.settings['cycle colours'] = True
# self.settings['cycle palette'] = "cy cherry blossom"
# self.settings['cycle change rate'] = 0.001

# self.settings['static colours'] = False
# self.settings['palette'] = "blue autumn"

# self.settings['add randomness to colour'] = True

# self.settings['bg colour'] = "space black"

# self.settings['digit is pen size'] = False
# self.settings['digit pen size scale factor'] = 1

# self.settings['pen size'] = 0.1
TRANSPARENCY = 0

ANGLE_DICTIONARY = {
    "0": 36,
    "1": 72,
    "2": 108,
    "3": 144,
    "4": 180,
    "5": 216,
    "6": 252,
    "7": 288,
    "8": 324,
    "9": 360
}


class TurtleVisualiser:
    def __init__(self, settings):
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.hare = hare.Hare(self.settings['target'])
        self.main_loop()

    def main_loop(self):
        # pr = cProfile.Profile()

        self.hare.move_to(2050, 2050)
        self.hare.fill_screen(turtle_colour_palette_dictionaries.bg_colours[self.settings['bg colour']])
        self.hare.line_colour = (0, 0, 0)
        self.hare.fill_screen(turtle_colour_palette_dictionaries.bg_colours[self.settings['bg colour']])
        self.hare.line_width = self.settings['pen size']

        if self.settings['cycle colours']:
            colour_palette = turtle_colour_palette_dictionaries.palettes_dictionary[self.settings['cycle palette']]
            r = colour_palette["r"]
            g = colour_palette["g"]
            b = colour_palette["b"]

            r_sign = "positive"
            g_sign = "positive"
            b_sign = "positive"

        counter = 0
        interval = 10000
        ticker = 0

        # get digits from text file
        with open("10milliondigitsofpi.txt") as f:
            pi_string = f.read()
            f.close()

        # remove everything that isn't a number
        pi_string.replace('\n', '')
        number_filter = filter(str.isdigit, pi_string)
        pi_string = "".join(number_filter)

        if self.settings['digit is colour']:
            palette = turtle_colour_palette_dictionaries.palettes_dictionary[self.settings['digit colour palette']]

        self.hare.trsurface.set_alpha(TRANSPARENCY)

        start_time = t.time()
        for digit in pi_string:

            if counter >= self.settings['target']:
                break

            if self.settings['digit is colour']:
                self.hare.line_colour = palette[digit]

            if self.settings['digit is pen size']:
                self.hare.line_width = int(digit) * self.settings['digit pen size scale factor']

            if self.settings['cycle colours'] and not self.settings['static colours']:
                if not self.settings['digit is colour']:
                    if r >= 255:
                        r_sign = "negative"
                    elif r <= 0:
                        r_sign = "positive"

                    if g >= 255:
                        g_sign = "negative"
                    elif g <= 0:
                        g_sign = "positive"

                    if b >= 255:
                        b_sign = "negative"
                    elif b <= 0:
                        b_sign = "positive"

                    if r_sign == "positive":
                        r += self.settings['cycle change rate']
                    else:
                        r -= self.settings['cycle change rate']

                    if g_sign == "positive":
                        g += self.settings['cycle change rate']
                    else:
                        g -= self.settings['cycle change rate']

                    if b_sign == "positive":
                        b += self.settings['cycle change rate']
                    else:
                        b -= self.settings['cycle change rate']

                    self.hare.line_colour = (r, g, b)

            angle = ANGLE_DICTIONARY[digit]

            p1 = self.hare.position
            p2 = self.hare.calculate_p2(p1, angle, self.settings['move distance'])
            if not self.settings['digit is pen size']:
                self.hare.draw_aaline(p1, p2, TRANSPARENCY)
            else:
                self.hare.draw_line(p1, p2, TRANSPARENCY)

            counter += 1

        if TRANSPARENCY != 0:
            self.hare.update_screen()
        else:
            self.hare.blit_tr_surface()

        self.hare.scale_image()

        finish_time = t.time()
        elapsed = (finish_time - start_time)
        elapsed = utils.round_to(elapsed, "2")
        print(f"{self.settings['target']} lines drawn in {elapsed} seconds")

        print("Finished. Saving image")

        path = pathlib.Path('outputs/Turtle/turtle screenshot.png')
        pygame.image.save(self.hare.surface, path)

        waiting = True

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
            if not waiting:
                pygame.quit()