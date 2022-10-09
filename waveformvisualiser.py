import pygame
import turtle_colour_palette_dictionaries
import math
import perlin

WINDOW_W = 1200
WINDOW_H = 1200

def update_screen():
    pygame.display.flip()

class WaveformVisualiser:

    def __init__(self, settings):
        pygame.init()

        self.settings = settings

        pygame.display.set_caption("Waveform Visualiser")
        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        self.surface = pygame.Surface((WINDOW_W, WINDOW_H))

        self.screen.fill(turtle_colour_palette_dictionaries.bg_colours[self.settings['bg colour']])

        self.offset = 15
        self.edge_margin = 20

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

        x = self.offset
        y_offset = self.offset

        counter = 0
        c_target = 100

        total = 0
        target_total = 30600

        running = True

        for digit in pi_string:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            if not running:
                break

            colour = turtle_colour_palette_dictionaries.palettes_dictionary[self.settings['digit colour palette']][digit]

            y = math.cos(int(digit)) * 3
            if x >= (WINDOW_W - self.edge_margin):
                x = self.edge_margin
                y_offset += self.offset
            pygame.draw.circle(self.screen, colour, (x, y + y_offset), 2, 2)
            x += 3
            counter += 1
            if counter == c_target:
                counter = 0
                update_screen()
            total += 1
            print(f"{total}")
            if total == target_total:
                break

        print("Finished. Saving image")
        pygame.image.save(self.screen, "waveform screenshot.png")