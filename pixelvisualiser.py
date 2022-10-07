import time
import sys

import pygame
import time as t

PI_STRING = ""
PI_ARRAY = []

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

BG_COLOUR_DICTIONARY = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "space_black": (21, 24, 33)
}

CD_ORGANIC = {
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

CD_STARFIELD = {
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

COLOUR_DICTIONARY = {
    "organic": (CD_ORGANIC),
    "starfield": (CD_STARFIELD)
}


class PixelVisualiser():
    def __init__(self, settings):
        self.settings = settings

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill(BG_COLOUR_DICTIONARY[self.settings['bg colour']])
        pygame.display.set_caption("Pi Visualiser")
        self.flip_display()
        

        self.main_loop()

    def main_loop(self):
        """Set up local vars from globals"""
        point_size = self.settings["point size"]
        offset = self.settings["offset"]
        if self.settings["offset same as point size"]:
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
            PI_ARRAY.append(i)

        print(str(len(PI_ARRAY)))

        x_index = 0
        y_index = 0
        centre_x = (SCREEN_WIDTH / 2)
        centre_y = (SCREEN_HEIGHT / 2)
        screen = self.screen
        direction = "R"

        step_target = 1
        steps_taken = 0

        times_target_hit = 0
        counter = 0
        running = True

        while running:
            start_time = t.time()
            for digit in PI_ARRAY:
                # Detect quits again so the program doesn't freeze when calculating
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                        pygame.quit()
                        sys.exit()

                if counter == len(PI_ARRAY):
                    self.export_image()
                    self.flip_display()
                    running - False
                    break

                if self.check_for_quits():
                    running = False
                    pygame.quit()

                if counter == self.settings["target"]:
                    self.export_image()
                    self.flip_display()
                    running = False
                    break

                """INJECT PI-BASED CONDITIONS HERE v"""

                point_size = int(self.settings['point size'])

                if self.settings['offset same as digit']:
                    offset = int(digit)

                if self.settings["pixel size equals digit"]:
                    point_size = int(self.settings['pixel size equals digit scaling factor']) * (int(digit))

                if self.settings['scale size over time']:
                    point_size += counter / self.settings['scale over time division factor']
                    if self.settings['scale size over time offset']:
                        offset += counter / self.settings['scale over time division factor']

                colour_ind = ((int(digit)+1) * 25)
                rect_colour = (colour_ind, colour_ind, colour_ind)

                """INJECT COLOUR CONDITIONS HERE v"""

                if self.settings['use colour dictionary']:
                    colour_dictionary = COLOUR_DICTIONARY[self.settings['point colour']]
                    rect_colour = colour_dictionary[digit]

                if self.settings['highlight 123s']:
                    if digit == "1" and PI_ARRAY[counter + 1] == "2" and PI_ARRAY[counter + 2] == "3":
                        rect_colour = self.settings['highlight colour']
                    if digit == "2" and PI_ARRAY[counter - 1] == "1" and PI_ARRAY[counter + 1] == "3":
                        rect_colour = self.settings['highlight colour']
                    if digit == "3" and PI_ARRAY[counter - 1] == "2" and PI_ARRAY[counter - 2] == "1":
                        rect_colour = self.settings['highlight colour']

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
                if self.settings["animate"]:
                    self.draw_animated(screen, rect_colour, rect_x_position, rect_y_position, point_size)
                else:
                    self.draw_not_animated(screen, rect_colour, rect_x_position, rect_y_position, point_size)

                counter += 1
                print(str(counter), "/" + str(self.settings["target"]) + " digits drawn")

                pygame.display.set_caption("Pi Visualiser -- " + str(counter) + "/" + str(self.settings['target']) + " pixels drawn")

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
