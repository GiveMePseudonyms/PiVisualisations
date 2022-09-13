import math

import pygame
from pygame.math import Vector2

UP = Vector2(0, -1)
GLOBAL_window_h = 1400
GLOBAL_window_w = 1400

GL_adjusted_window_h = GLOBAL_window_h * 3
GL_adjusted_window_w = GLOBAL_window_w * 3

GLOBAL_bg_colour = None

GLOBAL_use_frame_skip = True


def set_caption(caption):
    pygame.display.set_caption(caption)


def get_rotation_vector(angle):
    radians = angle * (math.pi / 180)
    rotation_vector = Vector2(math.cos(radians), math.sin(radians))
    return rotation_vector


class Hare:
    GLOBAL_frame_skip = 1000000
    GLOBAL_frame_counter = 1
    num_draw_calls = 0

    def __init__(self, target):
        pygame.init()
        self.target = target

        self.screen = pygame.display.set_mode((GLOBAL_window_w, GLOBAL_window_h))

        self.surface = pygame.Surface((GL_adjusted_window_w, GL_adjusted_window_h))
        self.trsurface = pygame.Surface((GL_adjusted_window_w, GL_adjusted_window_h), pygame.SRCALPHA)

        self.direction = Vector2(UP)

        self.x_position = 0
        self.y_position = 0
        self.position = Vector2(self.x_position, self.y_position)
        self.last_position = (0, 0)
        self.velocity = Vector2(0, 0)

        self.pen_active = True
        self.line_colour = (0, 0, 0)
        self.line_width = 1
        self.angle = 0
        self.aablend = 1

        self.update_screen()

    def pen_up(self):
        self.pen_active = False

    def move_to(self, x, y):
        self.position = Vector2(x, y)
        self.x_position = x
        self.y_position = y

    def pen_down(self):
        self.pen_active = True

    def fill_screen(self, colour):
        self.GLOBAL_bg_colour = colour
        self.screen.fill(colour)
        self.surface.fill(colour)
        self.trsurface.fill(colour)
        self.update_screen()

    def calculate_p2(self, p1, angle, distance):
        rotation_vector = get_rotation_vector(angle)
        p2 = self.position + rotation_vector * distance

        self.position = p2
        self.last_position = p1
        # print(f"Old position: {p1} - rotation vector = {rotation_vector) - new position: {p2}")
        return p2

    def draw_aaline(self, p1, p2, transparency):
        if transparency != 0:
            pygame.draw.aaline(self.trsurface, self.line_colour, p1, p2, self.aablend)
        else:
            pygame.draw.aaline(self.surface, self.line_colour, p1, p2, self.aablend)

        if GLOBAL_use_frame_skip:
            if self.GLOBAL_frame_counter >= self.GLOBAL_frame_skip:
                if transparency != 0:
                    self.scale_image()
                else:
                    self.screen.blit(self.surface, (0, 0))
                self.update_screen()
                self.GLOBAL_frame_counter = 0
            else:
                self.GLOBAL_frame_counter += 1
        else:
            self.update_screen()

        self.num_draw_calls += 1
        print(f"{self.num_draw_calls}/{self.target} lines drawn")

    def draw_line(self, p1, p2, transparency):
        if transparency != 0:
            pygame.draw.line(self.trsurface, self.line_colour, p1, p2, self.line_width)
        else:
            pygame.draw.line(self.surface, self.line_colour, p1, p2, self.line_width)

        if GLOBAL_use_frame_skip:
            if self.GLOBAL_frame_counter >= self.GLOBAL_frame_skip:
                if transparency != 0:
                    self.scale_image()
                else:
                    self.screen.blit(self.surface, (0, 0))
                self.update_screen()
                self.GLOBAL_frame_counter = 0
            else:
                self.GLOBAL_frame_counter += 1
        else:
            self.update_screen()

        self.num_draw_calls += 1
        print(f"{self.num_draw_calls}/{self.target} lines drawn")

    def update_screen(self):
        pygame.display.flip()

    def blit_normal_surface(self):
        self.screen.blit(self.surface, (0, 0))

    def blit_tr_surface(self):
        self.screen.blit(self.trsurface, (0, 0))

    def scale_image(self):
        scaled_surf = pygame.transform.scale(self.surface, (self.screen.get_width(), self.screen.get_height()))
        self.screen.fill((255, 255, 255))
        self.screen.blit(scaled_surf, (0, 0))
        self.update_screen()