import pygame
from pixelvisualiser import PixelVisualiser
from turtlevisualiser import TurtleVisualiser
from spiralvisualiser import SpiralVisualiser
from waveformvisualiser import WaveformVisualiser
from sandpilevisualiser import SandpileVisualiser
from webvisualiser import WebVisualiser
from orbitalvisualisation import OrbitalVisualisation
import tkinter


GLOBAL_window_height = 300
GLOBAL_window_width = 200
GLOBAL_keep_root_window = True

button_placement_offset = 30
button_y_margin = 10
button_x_margin = 20

window = tkinter.Tk()


def entry_point():
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()

    window_width = GLOBAL_window_width
    window_height = GLOBAL_window_height

    x_coord = int((screenwidth/ 2 - window_width/2))
    y_coord = int((screenheight/2 - window_height/2))

    window.title("Pi Visualisations")
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coord, y_coord))

    btn_launch_pixel_visualiser = tkinter.Button(window, text="Pixel Visualiser", bg='grey',
                                                 font=("Helvetica", 16), command=run_pixel_visualiser)

    btn_launch_turtle_visualiser = tkinter.Button(window, text="Turtle Visualiser", bg='grey',
                                                  font=("Helvetica", 16), command=run_turtle_visualiser)

    btn_launch_spiral_visualiser = tkinter.Button(window, text="Spiral Visualiser", bg='grey',
                                                  font=("Helvetica", 16), command=run_spiral_visualiser)

    btn_launch_waveform_visualiser = tkinter.Button(window, text="Waveform Visualiser", bg='grey',
                                                  font=("Helvetica", 16), command=run_waveform_visualiser)

    btn_launch_sandpile_visualiser = tkinter.Button(window, text="Sandpile Visualiser", bg='grey',
                                                  font=("Helvetica", 16), command=run_sandpile_visualiser)

    btn_launch_web_visualiser = tkinter.Button(window, text="Web Visualiser", bg='grey',
                                                  font=("Helvetica", 16), command=run_web_visualiser)

    btn_launch_orbital_visualiser = tkinter.Button(window, text="Orbital Visualiser", bg='grey',
                                                  font=("Helvetica", 16), command=run_orbital_visualiser)

    btn_launch_pixel_visualiser.place(x=20, y=button_y_margin)

    btn_launch_turtle_visualiser.place(x=20, y=button_placement_offset + button_y_margin)

    btn_launch_spiral_visualiser.place(x=20, y=(button_placement_offset * 2) + button_y_margin)

    btn_launch_waveform_visualiser.place(x=20, y=(button_placement_offset * 3) + button_y_margin)

    btn_launch_sandpile_visualiser.place(x=20, y=(button_placement_offset * 4) + button_y_margin)

    btn_launch_web_visualiser.place(x=20, y=(button_placement_offset * 5) + button_y_margin)

    btn_launch_orbital_visualiser.place(x=20, y=(button_placement_offset * 6) + button_y_margin)

    window.mainloop()


def run_pixel_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    pixel_visualiser = PixelVisualiser()
    pixel_visualiser.main_loop()


def run_turtle_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    turtle_visualiser = TurtleVisualiser()


def run_spiral_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    spiral_visualiser = SpiralVisualiser()


def run_waveform_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    waveform_visualiser = WaveformVisualiser()


def run_sandpile_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    sandpile_visualiser = SandpileVisualiser()


def run_web_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    web_visualiser = WebVisualiser()

def run_orbital_visualiser():
    if not GLOBAL_keep_root_window:
        window.destroy()
    orbital_visualiser = OrbitalVisualisation()