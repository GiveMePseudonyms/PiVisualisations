import pygame.image
import os

"""
A general utilities tool for functions which aren't important enough to go in main, but I'll likely need to reuse
"""

def round_to(number, precision):
    fprecision = str("." + precision + 'f')
    return str(format(number, fprecision))

def calculate_fps(time_taken_this_frame, fps_timer_precision):
    time_taken_this_frame = float(time_taken_this_frame)
    fps = 1 / time_taken_this_frame
    fps = round_to(fps, fps_timer_precision)
    return str(fps)

def clear_console():
    os.system('clear')

