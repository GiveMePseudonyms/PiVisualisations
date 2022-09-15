import pygame
from pixelvisualiser import PixelVisualiser
from turtlevisualiser import TurtleVisualiser
from spiralvisualiser import SpiralVisualiser
from waveformvisualiser import WaveformVisualiser
from sandpilevisualiser import SandpileVisualiser
from webvisualiser import WebVisualiser
from orbitalvisualisation import OrbitalVisualisation
import tkinter

KEEP_ROOT_WINDOW = True
WINDOW = tkinter.Tk()

def entry_point():
    """
    Build the main GUI tool which can be used to choose which visualiser you want to see.
    """

    button_placement_offset = 30
    button_y_margin = 10
    button_x_margin = 20

    window_height = 300
    window_width = 200

    screen_width = WINDOW.winfo_screenwidth()
    screen_height = WINDOW.winfo_screenheight()

    x_coord = int((screen_width/ 2 - window_width/2))
    y_coord = int((screen_height/2 - window_height/2))

    button_settings = {
        "font": "Helvetica",
        "fontsize": 16,
        "bg": "grey",
    }

    font = "Helvetica"
    fontsize = 16
    

    WINDOW.title("Pi Visualisations")
    WINDOW.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coord, y_coord))

    btn_launch_pixel_visualiser = tkinter.Button(WINDOW, text="Pixel Visualiser", bg=button_settings["bg"],
                                                 font=(button_settings["font"], button_settings["fontsize"]), 
                                                 command=run_pixel_visualiser)

    btn_launch_turtle_visualiser = tkinter.Button(WINDOW, text="Turtle Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_turtle_visualiser)

    btn_launch_spiral_visualiser = tkinter.Button(WINDOW, text="Spiral Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_spiral_visualiser)

    btn_launch_waveform_visualiser = tkinter.Button(WINDOW, text="Waveform Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_waveform_visualiser)

    btn_launch_sandpile_visualiser = tkinter.Button(WINDOW, text="Sandpile Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_sandpile_visualiser)

    btn_launch_web_visualiser = tkinter.Button(WINDOW, text="Web Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_web_visualiser)

    btn_launch_orbital_visualiser = tkinter.Button(WINDOW, text="Orbital Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_orbital_visualiser)

    btn_launch_pixel_visualiser.place(x=button_x_margin, y=button_y_margin)

    btn_launch_turtle_visualiser.place(x=button_x_margin, y=button_placement_offset + button_y_margin)

    btn_launch_spiral_visualiser.place(x=button_x_margin, y=(button_placement_offset * 2) + button_y_margin)

    btn_launch_waveform_visualiser.place(x=button_x_margin, y=(button_placement_offset * 3) + button_y_margin)

    btn_launch_sandpile_visualiser.place(x=button_x_margin, y=(button_placement_offset * 4) + button_y_margin)

    btn_launch_web_visualiser.place(x=button_x_margin, y=(button_placement_offset * 5) + button_y_margin)

    btn_launch_orbital_visualiser.place(x=button_x_margin, y=(button_placement_offset * 6) + button_y_margin)

    WINDOW.mainloop()

def run_pixel_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    pixel_visualiser = PixelVisualiser()
    pixel_visualiser.main_loop()

def run_turtle_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    turtle_visualiser = TurtleVisualiser()

def run_spiral_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    spiral_visualiser = SpiralVisualiser()

def run_waveform_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    waveform_visualiser = WaveformVisualiser()

def run_sandpile_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    sandpile_visualiser = SandpileVisualiser()

def run_web_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    web_visualiser = WebVisualiser()

def run_orbital_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    orbital_visualiser = OrbitalVisualisation()