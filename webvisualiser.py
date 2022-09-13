import random

import pygame
import turtle_colour_palette_dictionaries
import math
from numberobject import NumberObject

"""
TO-DO:

"""
"""
DONE
2. add transparency to lines.
    make new surface for each line so they blend nicely.

1. make lines different colours depending on start and end number colour. 
    Can I do this as a gradient?

3. the lines intersect the numbers at the top since they are aiming for the top left of the number rect.
    I can fix this by making a target coord with a smaller radius and centred rect.

4. add a tiny bit of randomness to each end pos so the lines don't overlap completely?
"""

GLOBAL_window_w = 1200
GLOBAL_window_h = 1200

GL_font_size = 30
GL_target = 10000

GL_rand_offset_ub = 20
GL_rand_offset_lb = 0

GL_palette = "peach and purple"

GL_rand_colours = False


def update_screen():
    pygame.display.flip()


class WebVisualiser:

    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Web Visualiser")
        self.screen = pygame.display.set_mode((GLOBAL_window_w, GLOBAL_window_h))
        self.surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))

        self.screen.fill(turtle_colour_palette_dictionaries.bg_colours["space black"])

        update_screen()

        self.offset = 15
        self.edge_margin = 20

        self.main_loop()

    def main_loop(self):
        NumberObject.fontSize = GL_font_size
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

        centre_x = GLOBAL_window_w / 2
        centre_y = GLOBAL_window_h / 2
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

        palette = turtle_colour_palette_dictionaries.palettes_dictionary[GL_palette]

        counter = 0
        update_interval = 1000
        for i in range(0, len(pi_string)):
            if counter == GL_target:
                print("hit target")
                break
            if i != len(pi_string):
                surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))
                surface.set_alpha(10)
                rand_offset = random.uniform(GL_rand_offset_lb, GL_rand_offset_ub)
                if GL_rand_colours:
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
            print(f"{counter}/{GL_target}")

        pygame.image.save(self.screen, "web visualiser screenshot.png")

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
                if not waiting:
                    break
        pygame.quit()
