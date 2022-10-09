import random

import pygame
import turtle_colour_palette_dictionaries
import math
from numberobject import NumberObject

WINDOW_W = 1200
WINDOW_H = 1200

FONT_SIZE = 30
TARGET = 10000

RANDOM_OFFSET_UPPER_BOUND = 20
RANDOM_OFFSET_LOWER_BOUND = 0

COLOUR_PALETTE = "peach and purple"

USE_RANDOM_COLOURS = False


def update_screen():
    pygame.display.flip()
    

class WebVisualiser:

    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Web Visualiser")
        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        self.surface = pygame.Surface((WINDOW_W, WINDOW_H))

        self.screen.fill(turtle_colour_palette_dictionaries.bg_colours["space black"])

        update_screen()

        self.offset = 15
        self.edge_margin = 20

        self.main_loop()

    def main_loop(self):
        NumberObject.fontSize = FONT_SIZE
        n_0 = NumberObject("0", 10, 10, (255, 255, 255))
        n_1 = NumberObject("1", 30, 10, (255, 255, 255))
        n_2 = NumberObject("2", 50, 10, (255, 255, 255))
        n_3 = NumberObject("3", 70, 10, (255, 255, 255))
        n_4 = NumberObject("4", 90, 10, (255, 255, 255))
        n_5 = NumberObject("5", 110, 10, (255, 255, 255))
        n_6 = NumberObject("6", 130, 10, (255, 255, 255))
        n_7 = NumberObject("7", 150, 10, (255, 255, 255))
        n_8 = NumberObject("8", 170, 10, (255, 255, 255))
        n_9 = NumberObject("9", 190, 10, (255, 255, 255))

        numberobjectdict = {
            "0": n_0,
            "1": n_1,
            "2": n_2,
            "3": n_3,
            "4": n_4,
            "5": n_5,
            "6": n_6,
            "7": n_7,
            "8": n_8,
            "9": n_9
        }

        n_list = []
        n_list.extend((n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9))

        centre_x = WINDOW_W / 2
        centre_y = WINDOW_H / 2
        radius = 500
        theta = math.radians(36)

        index = 0
        for item in n_list:
            angle = theta * index

            x = radius * math.sin(angle)
            y = radius * math.cos(angle)

            text_x = (radius + 40) * math.sin(angle)
            text_y = (radius + 40) * math.cos(angle)

            item.x_pos = centre_x + x
            item.y_pos = centre_y - y

            self.screen.blit(item.img, (centre_x + text_x, centre_y - text_y))

            index += 1

        update_screen()

        # get digits from text file
        with open("10milliondigitsofpi.txt") as f:
            pi_string = f.read()
            f.close()

        # remove everything that isn't a number
        pi_string.replace('\n', '')
        number_filter = filter(str.isdigit, pi_string)
        pi_string = "".join(number_filter)

        palette = turtle_colour_palette_dictionaries.palettes_dictionary[COLOUR_PALETTE]

        counter = 0
        update_interval = 1000
        for i in range(0, len(pi_string)):
            if counter == TARGET:
                print("hit target")
                break
            if i != len(pi_string):
                surface = pygame.Surface((WINDOW_W, WINDOW_H))
                surface.set_alpha(10)
                rand_offset = random.uniform(RANDOM_OFFSET_LOWER_BOUND, RANDOM_OFFSET_UPPER_BOUND)
                if USE_RANDOM_COLOURS:
                    r = random.uniform(0, 255)
                    g = random.uniform(0, 255)
                    b = random.uniform(0, 255)
                    pygame.draw.aaline(surface,
                                       (r, g, b),
                                       ((numberobjectdict[pi_string[i]].x_pos + rand_offset),
                                        (numberobjectdict[pi_string[i]].y_pos + rand_offset)),
                                       ((numberobjectdict[pi_string[i+1]].x_pos+ rand_offset),
                                        numberobjectdict[pi_string[i+1]].y_pos + rand_offset), 1)
                else:
                    pygame.draw.aaline(surface,
                                       (palette[pi_string[i]]),
                                       ((numberobjectdict[pi_string[i]].x_pos + rand_offset),
                                        (numberobjectdict[pi_string[i]].y_pos + rand_offset)),
                                       ((numberobjectdict[pi_string[i + 1]].x_pos + rand_offset),
                                        (numberobjectdict[pi_string[i + 1]].y_pos + rand_offset)), 1)
                self.screen.blit(surface, (0, 0))
                if (counter % update_interval) == 0:
                    update_screen()
            counter += 1
            print(f"{counter}/{TARGET}")

        pygame.image.save(self.screen, "web visualiser screenshot.png")

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
                if not waiting:
                    break
        pygame.quit()
