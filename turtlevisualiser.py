"""
TO DO:
Make a "general settings" dict in separate py file so i can have settings held out of main.
    ALSO add settings to launcher window so I can change things during use, then send them into the settings dict

Make function to scale the created image to fit into the window
(maybe look at how this worked for 4k images from the pixel version
    Done-ish. Might be a better way than brute force but cba. It works.
    COULD track the cartesian of each line, then add some padding and make a surface to match the size, then scale it.
        this would also help with centring the image.

Implement transparency for new version (needs to make a new surface per line since
transparency is done per surface, shouldn't be too hard
    Still working on this. Making a new surface for each line creates bullshit lag, ignore for now.

Reimplement screenshot feature. Can it be saved as PDF to preserve quality?
    done, png works, scaled up canvas size to get better resolution, see scaling notes above.
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

GLOBAL_window_width = 800
GLOBAL_window_height = 800

GLOBAL_wait_until_done = True
GLOBAL_frame_skip_interval = 10000

GLOBAL_target = 1000000

GLOBAL_move_distance = 0.8

GLOBAL_output_filename = "screenshot"

GLOBAL_digit_is_colour = False
GLOBAL_digit_palette = "starfield"

GLOBAL_colour_cycling = True
GLOBAL_colour_cycling_palette = "cy cherry blossom"
GLOBAL_color_change_offset = 0.001

GLOBAL_static_colours = False
GLOBAL_palette = "blue autumn"

GLOBAL_add_randomness_to_colour = True

GLOBAL_bg_colour = "space black"

GLOBAL_digit_is_pen_size = False
GLOBAL_digit_is_pen_size_scale_factor = 1

GLOBAL_pen_size = 0.1
GLOBAL_transparency = 0

angle_dictionary = {
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
        self.hare = hare.Hare(GLOBAL_target)
        self.main_loop()

    def main_loop(self):
        # pr = cProfile.Profile()

        self.hare.move_to(2050, 2050)
        self.hare.fill_screen(turtle_colour_palette_dictionaries.bg_colours[GLOBAL_bg_colour])
        self.hare.line_colour = (0, 0, 0)
        self.hare.fill_screen(turtle_colour_palette_dictionaries.bg_colours[GLOBAL_bg_colour])
        self.hare.line_width = GLOBAL_pen_size

        if GLOBAL_colour_cycling:
            colour_palette = turtle_colour_palette_dictionaries.palettes_dictionary[GLOBAL_colour_cycling_palette]
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

        if GLOBAL_digit_is_colour:
            palette = turtle_colour_palette_dictionaries.palettes_dictionary[GLOBAL_digit_palette]

        self.hare.trsurface.set_alpha(GLOBAL_transparency)

        start_time = t.time()
        for digit in pi_string:

            if counter >= GLOBAL_target:
                break

            if GLOBAL_digit_is_colour:
                self.hare.line_colour = palette[digit]

            if GLOBAL_digit_is_pen_size:
                self.hare.line_width = int(digit) * GLOBAL_digit_is_pen_size_scale_factor

            if GLOBAL_colour_cycling and not GLOBAL_static_colours:
                if not GLOBAL_digit_is_colour:
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
                        r += GLOBAL_color_change_offset
                    else:
                        r -= GLOBAL_color_change_offset

                    if g_sign == "positive":
                        g += GLOBAL_color_change_offset
                    else:
                        g -= GLOBAL_color_change_offset

                    if b_sign == "positive":
                        b += GLOBAL_color_change_offset
                    else:
                        b -= GLOBAL_color_change_offset

                    self.hare.line_colour = (r, g, b)

            angle = angle_dictionary[digit]

            p1 = self.hare.position
            p2 = self.hare.calculate_p2(p1, angle, GLOBAL_move_distance)
            if not GLOBAL_digit_is_pen_size:
                self.hare.draw_aaline(p1, p2, GLOBAL_transparency)
            else:
                self.hare.draw_line(p1, p2, GLOBAL_transparency)

            counter += 1

        if GLOBAL_transparency != 0:
            self.hare.update_screen()
        else:
            self.hare.blit_tr_surface()

        self.hare.scale_image()

        finish_time = t.time()
        elapsed = (finish_time - start_time)
        elapsed = utils.round_to(elapsed, "2")
        print(f"{GLOBAL_target} lines drawn in {elapsed} seconds")

        print("Finished. Saving image")
        pygame.image.save(self.hare.surface, "turtle screenshot.png")

        waiting = True

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
            if not waiting:
                pygame.quit()