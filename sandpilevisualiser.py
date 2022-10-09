import pygame
import sandpile_colour_schemes
<<<<<<< HEAD
import pathlib
=======
>>>>>>> 27af6b481d7aeae2b9c21bcbc408334de27dda09

WINDOW_W = 1200
WINDOW_H = 1200

class SandpileVisualiser:
    def __init__(self, settings):

        pygame.init()

        self.settings = settings
        self.colour_scheme = sandpile_colour_schemes.colour_schemes[self.settings['colour scheme']]
        self.bg_colour = sandpile_colour_schemes.bg_colours[self.settings['bg colour']]
        self.update_interval = self.settings['update interval']

        pygame.display.set_caption("Sandpile Visualiser")
        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        self.surface = pygame.Surface((WINDOW_W, WINDOW_H))

        self.centre_weight = 31415
        self.pixel_size = 6

        self.draw_call_counter = 0

        self.rows = int(WINDOW_H / self.pixel_size)
        self.cols = int(WINDOW_W / self.pixel_size)

        # make a 2d array for the grid of window size, all containing a 0
        self.grid = [[0] * self.cols for _ in range(self.rows)]

        self.main_loop()

    def main_loop(self):
        running = True

        # set the central item to a 1
        centre_x = int(self.cols / 2)
        centre_y = int(self.rows / 2)
        self.grid[centre_x][centre_y] = self.centre_weight

        # set up every column and every row with initial conditions
        self.screen.fill((0, 0, 0))
        self.update_display()
        print("Finished setting up. Starting simulation.")

        counter = 0
        count_target = self.update_interval

        while True:
            for x in range(self.rows):
                for y in range(self.cols):
                    if self.grid[x][y] > 3:
                        if x != 0 and x != self.rows - 1:
                            if y != 0 and y != self.cols - 1:
                                self.overflow(x, y)

            if not running:
                break

            counter += 1
            if counter == count_target and running:
                counter = 0
                self.update_display()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

        self.update_display()
        print("Finished or interrupted, saving screenshot!")
        path = pathlib.Path('outputs/Sandpile/sandpile screenshot.png')
        pygame.image.save(self.screen, path)

    def update_display(self):
        self.draw_grid()
        pygame.display.flip()

    def draw_grid(self):
        # I can speed this up using a dispatch dictionary (dict of functions which will be called in each case)
        # I could also use numpy to vectorise the arrays
        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] > 3:
                    pygame.draw.rect(self.screen, self.colour_scheme[">3"],
                                     pygame.Rect(x * self.pixel_size, y * self.pixel_size, self.pixel_size,
                                                 self.pixel_size))
                elif self.grid[x][y] == 3:
                    pygame.draw.rect(self.screen, self.colour_scheme["3"],
                                     pygame.Rect(x * self.pixel_size, y * self.pixel_size, self.pixel_size,
                                                 self.pixel_size))
                elif self.grid[x][y] == 2:
                    pygame.draw.rect(self.screen, self.colour_scheme["2"],
                                     pygame.Rect(x * self.pixel_size, y * self.pixel_size, self.pixel_size,
                                                 self.pixel_size))
                elif self.grid[x][y] == 1:
                    pygame.draw.rect(self.screen, self.colour_scheme["1"],
                                     pygame.Rect(x * self.pixel_size, y * self.pixel_size, self.pixel_size,
                                                 self.pixel_size))
                elif self.grid[x][y] == 0:
                    pygame.draw.rect(self.screen, sandpile_colour_schemes.bg_colours[self.settings['bg colour']],
                                     pygame.Rect(x * self.pixel_size, y * self.pixel_size, self.pixel_size,
                                                 self.pixel_size))
        self.draw_call_counter += 1
        print(f"Grid drawn ({self.draw_call_counter} times)")

    def overflow(self, x, y):
        self.grid[x][y] -= 4
        self.grid[x][y - 1] += 1
        self.grid[x - 1][y] += 1
        self.grid[x + 1][y] += 1
        self.grid[x][y + 1] += 1
        