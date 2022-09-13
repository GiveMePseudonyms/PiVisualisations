import pygame
import turtle_colour_palette_dictionaries
import math
import perlin

GLOBAL_window_w = 1200
GLOBAL_window_h = 1200


def update_screen():
    pygame.display.flip()


class WaveformVisualiser:

    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Waveform Visualiser")
        self.screen = pygame.display.set_mode((GLOBAL_window_w, GLOBAL_window_h))
        self.surface = pygame.Surface((GLOBAL_window_w, GLOBAL_window_h))

        self.screen.fill(turtle_colour_palette_dictionaries.bg_colours["space black"])

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

            colour = turtle_colour_palette_dictionaries.starfield[digit]
            y = math.cos(int(digit)) * 3
            if x >= (GLOBAL_window_w - self.edge_margin):
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