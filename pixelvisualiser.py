import time
import sys

import pygame
import time as t

pi_string = ""
pi = []

screen_width = 10000
screen_height = 10000


"""FUN SETTINGS"""
animate = False

GLOBAL_target = 500000

pixel_size_equals_digit = True
GLOBAL_pixel_size_equals_digit_scaling_factor = 0.5

scale_size_over_time = True
scale_size_over_time_scale_offset = True
GLOBAL_scale_over_time_division_factor = 1000000000

highlight_420s = False
highlight_69s = False
highlight_230297 = True

offset_same_as_point_size = False
offset_same_as_digit = False
GLOBAL_offset = 1

"""minimum 1 v"""
GLOBAL_point_size = 3

GLOBAL_highlight_colour = (255, 0, 0)

GLOBAL_use_colour_dictionary = True

GLOBAL_bg_colour = "space_black"
GLOBAL_point_colour = "starfield"

GLOBAL_bg_colour_dictionary = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "space_black": (21, 24, 33)
}

CD_organic = {
    "0": (130, 180, 194),
    "1": (134, 170, 188),
    "2": (137, 159, 183),
    "3": (140, 149, 177),
    "4": (144, 138, 172),
    "5": (147, 127, 167),
    "6": (150, 117, 161),
    "7": (153, 106, 156),
    "8": (157, 95, 151),
    "9": (160, 85, 145)
}

CD_starfield = {
    "0": (248, 202, 55),
    "1": (112, 108, 76),
    "2": (21, 68, 234),
    "3": (239, 149, 33),
    "4": (249, 254, 249),
    "5": (56, 109, 204),
    "6": (234, 226, 193),
    "7": (145, 110, 78),
    "8": (45, 67, 35),
    "9": (225, 200, 125)
}

GLOBAL_colour_dictionary = {
    "organic": (CD_organic),
    "starfield": (CD_starfield)
}


class PixelVisualiser:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill(GLOBAL_bg_colour_dictionary[GLOBAL_bg_colour])
        pygame.display.set_caption("Pi Visualiser")
        self.flip_display()

    def main_loop(self):
        """Set up local vars from globals"""
        point_size = GLOBAL_point_size
        offset = GLOBAL_offset
        if offset_same_as_point_size:
            offset = point_size

        # get digits from text file
        with open("1milliondigitsofpi.txt") as f:
            pi_string = f.read()
            f.close()

        # remove everything that isn't a number
        pi_string.replace('\n', '')
        number_filter = filter(str.isdigit, pi_string)
        pi_string = "".join(number_filter)

        # shift digits into array
        for i in pi_string:
            pi.append(i)

        print(str(len(pi)))

        x_index = 0
        y_index = 0
        centre_x = (screen_width / 2)
        centre_y = (screen_height / 2)
        screen = self.screen
        direction = "R"

        step_target = 1
        steps_taken = 0

        times_target_hit = 0
        counter = 0
        running = True

        while running:
            start_time = t.time()
            for digit in pi:
                # Detect quits again so the program doesn't freeze when calculating
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                        pygame.quit()
                        sys.exit()

                if counter == len(pi):
                    self.export_image()
                    self.flip_display()
                    running - False
                    break

                if self.check_for_quits():
                    running = False
                    pygame.quit()

                if counter == GLOBAL_target:
                    self.export_image()
                    self.flip_display()
                    running = False
                    break

                """INJECT PI-BASED CONDITIONS HERE v"""

                if offset_same_as_digit:
                    offset = int(digit)

                if pixel_size_equals_digit:
                    point_size = GLOBAL_pixel_size_equals_digit_scaling_factor * (int(digit))

                if scale_size_over_time:
                    point_size += counter / GLOBAL_scale_over_time_division_factor
                    if scale_size_over_time_scale_offset:
                        offset += counter / GLOBAL_scale_over_time_division_factor

                colour_ind = ((int(digit)+1) * 25)
                rect_colour = (colour_ind, colour_ind, colour_ind)

                """INJECT COLOUR CONDITIONS HERE v"""

                if GLOBAL_use_colour_dictionary:
                    colour_dictionary = GLOBAL_colour_dictionary[GLOBAL_point_colour]
                    rect_colour = colour_dictionary[digit]

                if highlight_420s:
                    if digit == "4" and pi[counter + 1] == "2" and pi[counter + 2] == "0":
                        rect_colour = GLOBAL_highlight_colour
                    if digit == "2" and pi[counter - 1] == "4" and pi[counter + 1] == "0":
                        rect_colour = GLOBAL_highlight_colour
                    if digit == "0" and pi[counter - 1] == "2" and pi[counter - 2] == "4":
                        rect_colour = GLOBAL_highlight_colour

                if highlight_69s:
                    if digit == "6" and pi[counter + 1] == "9":
                        rect_colour = GLOBAL_highlight_colour
                    if digit == "9" and pi[counter - 1] == "6":
                        rect_colour = GLOBAL_highlight_colour

                if steps_taken != step_target:
                    if direction == "R":
                        x_index += offset
                        steps_taken += 1
                    elif direction == "U":
                        y_index -= offset
                        steps_taken += 1
                    elif direction == "L":
                        x_index -= offset
                        steps_taken += 1
                    elif direction == "D":
                        y_index += offset
                        steps_taken += 1

                elif steps_taken == step_target:
                    if times_target_hit != 2:
                        times_target_hit += 1
                        steps_taken = 0
                    elif times_target_hit == 2:
                        steps_taken = 0
                        step_target += 1
                        times_target_hit = 1

                    if direction == "R":
                        x_index += offset
                        direction = "U"
                    elif direction == "U":
                        y_index -= offset
                        direction = "L"
                    elif direction == "L":
                        x_index -= offset
                        direction = "D"
                    elif direction == "D":
                        y_index += offset
                        direction = "R"

                rect_x_position = centre_x - (point_size / 2) + x_index
                rect_y_position = centre_y - (point_size / 2) + y_index
                if animate:
                    self.draw_animated(screen, rect_colour, rect_x_position, rect_y_position, point_size)
                else:
                    self.draw_not_animated(screen, rect_colour, rect_x_position, rect_y_position, point_size)

                counter += 1
                print(str(counter), "/" + str(GLOBAL_target) + " digits drawn")

                pygame.display.set_caption("Pi Visualiser -- " + str(counter) + "/" + str(GLOBAL_target) + " pixels drawn")

        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

    def draw_animated(self, screen, colour, x_position, y_position, point_size):
        pygame.draw.rect(screen, colour, pygame.Rect(x_position, y_position, point_size, point_size))
        pygame.display.flip()

    def draw_not_animated(self, screen, colour, x_position, y_position, point_size):
        pygame.draw.rect(screen, colour, pygame.Rect(x_position, y_position, point_size, point_size))

    def flip_display(self):
        pygame.display.flip()

    def export_image(self):
        pygame.image.save(self.screen, "pixel screenshot.png")

    def check_for_quits(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return True
