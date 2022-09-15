"""
TO DO:
Make a "general settings" dict in separate py file so i can have settings held out of main.
    ALSO add settings to launcher window so I can change things during use, then send them into the settings dict

Make function to scale the created image to fit into the window
(maybe look at how this worked for 4k images from the pixel version
    Done-ish. Will look for a better way to handle this.
    COULD track the cartesian of each line, then add some padding and make a surface to match the size, then scale it.
        this would also help with centring the image.

Implement transparency for new version (needs to make a new surface per line since
transparency is done per surface, shouldn't be too hard)
    Still working on this. Making a new surface for each line creates lag, ignore for now.
"""

import pygame.time

import turtle_colour_palette_dictionaries
import turtle
import hare
from turtle import *
from PIL import Image
import time as t
import cProfile

import utils

WINDOW_W = 800
WINDOW_H = 800

WAIT_UNTIL_DONE = True
FRAME_SKIP_INTERVAL = 10000

TARGET = 1000000

MOVE_DISTANCE = 0.8

OUTPUT_FILENAME = "screenshot"

DIGIT_IS_COLOUR = False
DIGIT_COLOUR_PALETTE = "starfield"

CYCLE_COLOURS = True
CYCLE_PALETTE = "cy cherry blossom"
CYCLE_CHANGE_RATE = 0.001

STATIC_COLOURS = False
PALETTE = "blue autumn"

ADD_RANDOMNESS_TO_COLOUR = True

BG_COLOUR = "space black"

DIGIT_IS_PEN_SIZE = False
DIPS_SCALE_FACTOR = 1

PEN_SIZE = 0.1
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
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.hare = hare.Hare(TARGET)
        self.main_loop()

    def main_loop(self):
        # pr = cProfile.Profile()

        self.hare.move_to(2050, 2050)
        self.hare.fill_screen(turtle_colour_palette_dictionaries.bg_colours[BG_COLOUR])
        self.hare.line_colour = (0, 0, 0)
        self.hare.fill_screen(turtle_colour_palette_dictionaries.bg_colours[BG_COLOUR])
        self.hare.line_width = PEN_SIZE

        if CYCLE_COLOURS:
            colour_palette = turtle_colour_palette_dictionaries.palettes_dictionary[CYCLE_PALETTE]
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

        if DIGIT_IS_COLOUR:
            palette = turtle_colour_palette_dictionaries.palettes_dictionary[DIGIT_COLOUR_PALETTE]

        self.hare.trsurface.set_alpha(TRANSPARENCY)

        start_time = t.time()
        for digit in pi_string:

            if counter >= TARGET:
                break

            if DIGIT_IS_COLOUR:
                self.hare.line_colour = palette[digit]

            if DIGIT_IS_PEN_SIZE:
                self.hare.line_width = int(digit) * DIPS_SCALE_FACTOR

            if CYCLE_COLOURS and not STATIC_COLOURS:
                if not DIGIT_IS_COLOUR:
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
                        r += CYCLE_CHANGE_RATE
                    else:
                        r -= CYCLE_CHANGE_RATE

                    if g_sign == "positive":
                        g += CYCLE_CHANGE_RATE
                    else:
                        g -= CYCLE_CHANGE_RATE

                    if b_sign == "positive":
                        b += CYCLE_CHANGE_RATE
                    else:
                        b -= CYCLE_CHANGE_RATE

                    self.hare.line_colour = (r, g, b)

            angle = ANGLE_DICTIONARY[digit]

            p1 = self.hare.position
            p2 = self.hare.calculate_p2(p1, angle, MOVE_DISTANCE)
            if not DIGIT_IS_PEN_SIZE:
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
        print(f"{TARGET} lines drawn in {elapsed} seconds")

        print("Finished. Saving image")
        pygame.image.save(self.hare.surface, "turtle screenshot.png")

        waiting = True

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
            if not waiting:
                pygame.quit()