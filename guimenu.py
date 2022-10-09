import pygame
from pixelvisualiser import PixelVisualiser
from turtlevisualiser import TurtleVisualiser
from spiralvisualiser import SpiralVisualiser
from waveformvisualiser import WaveformVisualiser
from sandpilevisualiser import SandpileVisualiser
from webvisualiser import WebVisualiser
from orbitalvisualisation import OrbitalVisualisation
import tkinter
import SettingsData

KEEP_ROOT_WINDOW = True
WINDOW = tkinter.Tk()

def entry_point():
    """
    Build the main GUI tool which can be used to choose which visualiser you want to see.
    """

    button_placement_offset = 30
    button_y_margin = 10
    button_x_margin = 20

    window_height = 700
    window_width = 700

    screen_width = WINDOW.winfo_screenwidth()
    screen_height = WINDOW.winfo_screenheight()

    x_coord = int((screen_width/ 2 - window_width/2))
    y_coord = int((screen_height/2 - window_height/2))

    button_settings = {
        "font": "Helvetica",
        "fontsize": 16,
        "bg": "grey",
        "specialbg": "blue",
    }

    font = "Helvetica"
    fontsize = 16
    
    WINDOW.title("Pi Visualisations")
    WINDOW.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coord, y_coord))

    settings_data = SettingsData.SettingsData(WINDOW)

    btn_launch_pixel_visualiser = tkinter.Button(WINDOW, text="Pixel Visualiser", bg=button_settings["bg"],
                                                 font=(button_settings["font"], button_settings["fontsize"]), 
                                                 command=lambda: select_visualiser(settings_data, 'pixelvisualiser.py'))

    btn_launch_turtle_visualiser = tkinter.Button(WINDOW, text="Turtle Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=lambda: select_visualiser(settings_data, 'turtlevisualiser.py'))

    btn_launch_spiral_visualiser = tkinter.Button(WINDOW, text="Spiral Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=lambda: select_visualiser(settings_data, 'spiralvisualiser.py'))

    btn_launch_waveform_visualiser = tkinter.Button(WINDOW, text="Waveform Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=lambda: select_visualiser(settings_data, 'waveformvisualiser.py'))

    btn_launch_sandpile_visualiser = tkinter.Button(WINDOW, text="Sandpile Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=lambda: select_visualiser(settings_data, 'sandpilevisualiser.py'))

    btn_launch_web_visualiser = tkinter.Button(WINDOW, text="Web Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_web_visualiser)

    btn_launch_orbital_visualiser = tkinter.Button(WINDOW, text="Orbital Visualiser", bg=button_settings["bg"],
                                                  font=(button_settings["font"], button_settings["fontsize"]), 
                                                  command=run_orbital_visualiser)

    btn_test = tkinter.Button(WINDOW, text="Test", bg=button_settings['bg'],
                                                    font=(button_settings['font'], button_settings['fontsize']),
                                                    command=lambda: test(settings_data))

    btn_start = tkinter.Button(WINDOW, text="Start", bg=button_settings["specialbg"], fg=button_settings["specialbg"], 
                                                    font=(button_settings['font'], button_settings['fontsize']), 
                                                    command=lambda: start(settings_data))

    btn_list = []
    btn_list.extend([btn_launch_pixel_visualiser, btn_launch_turtle_visualiser, btn_launch_spiral_visualiser, btn_launch_waveform_visualiser,btn_launch_sandpile_visualiser,
    btn_launch_web_visualiser, btn_launch_orbital_visualiser,btn_test, btn_start])

    for _ in range(0, len(btn_list)):
        btn_list[_].grid(column=0, row=_, sticky=tkinter.W, pady=2, padx=30)

    WINDOW.mainloop()

def test(settings_data):
    settings_data.select_visualiser("test")
    expand_options(settings_data)

def clear_widgets_labels(settings_data):
    settings_data.grid_forget_all()

def select_visualiser(settings_data, visualiser):
    clear_widgets_labels(settings_data)

    if visualiser == 'pixelvisualiser.py':
        settings_data.select_visualiser("pixelvisualiser.py")
    elif visualiser == 'turtlevisualiser.py':
        settings_data.select_visualiser('turtlevisualiser.py')
    elif visualiser == 'spiralvisualiser.py':
        settings_data.select_visualiser('spiralvisualiser.py')
    elif visualiser == 'waveformvisualiser.py':
        settings_data.select_visualiser('waveformvisualiser.py')
    elif visualiser == 'sandpilevisualiser.py':
        settings_data.select_visualiser('sandpilevisualiser.py')
    
    expand_options(settings_data)

def expand_options(settings_data):
    if settings_data.selection == "test":
        for _ in range(0, len(settings_data.test_data.widgets)):
            settings_data.test_data.widgets[_].grid(column=3, row=_, sticky=tkinter.E)
    elif settings_data.selection == "pixelvisualiser.py":
        for label in settings_data.pixel_visualiser_options.labels:
            if label != None:
                label.grid(column=2, row=settings_data.pixel_visualiser_options.labels.index(label))
            else: pass
        
        for _ in range(0, len(settings_data.pixel_visualiser_options.widgets)):
            settings_data.pixel_visualiser_options.widgets[_].grid(column=3, row=_, sticky=tkinter.E, padx=5)
    
    elif settings_data.selection == "turtlevisualiser.py":
        for label in settings_data.turtle_visualiser_options.labels:
            if label != None:
                label.grid(column=2, row=settings_data.turtle_visualiser_options.labels.index(label))
            else: pass

        for _ in range(0, len(settings_data.turtle_visualiser_options.widgets)):
            settings_data.turtle_visualiser_options.widgets[_].grid(column=3, row=_, sticky=tkinter.E, padx=5)

    elif settings_data.selection == "spiralvisualiser.py":
        for label in settings_data.spiral_visualiser_options.labels:
            if label != None:
                label.grid(column=2, row=settings_data.spiral_visualiser_options.labels.index(label))
            else: pass
        
        for _ in range(0, len(settings_data.spiral_visualiser_options.widgets)):
            settings_data.spiral_visualiser_options.widgets[_].grid(column=3, row=_, sticky=tkinter.E, padx=5)

    elif settings_data.selection == 'waveformvisualiser.py':
        for label in settings_data.waveform_visualiser_options.labels:
            if label != None:
                label.grid(column=2, row=settings_data.waveform_visualiser_options.labels.index(label))
            else: pass

        for _ in range(0, len(settings_data.waveform_visualiser_options.widgets)):
            settings_data.waveform_visualiser_options.widgets[_].grid(column=3, row=_, sticky=tkinter.E, padx=5)

    elif settings_data.selection == "sandpilevisualiser.py":
        for label in settings_data.sandpile_visualiser_options.labels:
            if label != None:
                label.grid(column=2, row=settings_data.sandpile_visualiser_options.labels.index(label))
            else: pass

        for _ in range(0, len(settings_data.sandpile_visualiser_options.widgets)):
            settings_data.sandpile_visualiser_options.widgets[_].grid(column=3, row=_, sticky=tkinter.E, padx=5)

    elif settings_data.selection == "webvisualiser.py":
        pass
    elif settings_data.selection == "orbitalvisualisation.py":
        pass
    
    WINDOW.update()

def run_pixel_visualiser(settings):
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    print("Running pixel visualiser with settings: ")
    print(settings_data)
    pixel_visualiser = PixelVisualiser(settings)

def run_turtle_visualiser(settings):
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    turtle_visualiser = TurtleVisualiser(settings)

def run_spiral_visualiser(settings):
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    spiral_visualiser = SpiralVisualiser(settings)

def run_waveform_visualiser(settings):
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    waveform_visualiser = WaveformVisualiser(settings)

def run_sandpile_visualiser(settings):
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    sandpile_visualiser = SandpileVisualiser(settings)

def run_web_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    web_visualiser = WebVisualiser()

def run_orbital_visualiser():
    if not KEEP_ROOT_WINDOW:
        WINDOW.destroy()
    orbital_visualiser = OrbitalVisualisation()

def start(settings_data):
    if settings_data.selection == "test":
        print(f"Test selected and started.")
        if settings_data.test_data.checkbox.instate(['selected']):
            print("Checkbox is selected")
        else: print("Checkbox not selected")
        print(f"Textfield text = {settings_data.test_data.textfield.get()}")

    elif settings_data.selection == "pixelvisualiser.py":
        settings_data.pixel_visualiser_options.settings = generate_pixel_visualiser_settings(settings_data.pixel_visualiser_options)
        run_pixel_visualiser(settings_data.pixel_visualiser_options.settings)
        
    elif settings_data.selection == 'turtlevisualiser.py':
        settings_data.turtle_visualiser_options.settings = generate_turtle_visualiser_settings(settings_data.turtle_visualiser_options)
        run_turtle_visualiser(settings_data.turtle_visualiser_options.settings)

    elif settings_data.selection == 'spiralvisualiser.py':
        settings_data.spiral_visualiser_options.settings = generate_spiral_visualiser_settings(settings_data.spiral_visualiser_options)
        run_spiral_visualiser(settings_data.spiral_visualiser_options.settings)

    elif settings_data.selection == 'waveformvisualiser.py':
        settings_data.waveform_visualiser_options.settings = generate_waveform_visualiser_settings(settings_data.waveform_visualiser_options)
        run_waveform_visualiser(settings_data.waveform_visualiser_options.settings)

    elif settings_data.selection == 'sandpilevisualiser.py':
        settings_data.sandpile_visualiser_options.settings = generate_sandpile_visualiser_settings(settings_data.sandpile_visualiser_options)
        run_sandpile_visualiser(settings_data.sandpile_visualiser_options.settings)

def generate_pixel_visualiser_settings(settings_data):
    if settings_data.chk_animate.instate(['selected']):
        settings_data.settings['animate'] = True
    else: settings_data.settings['animate'] = False
    
    if settings_data.textfield_target.get() != "":
        settings_data.settings['target'] = int(settings_data.textfield_target.get())
    else: settings_data.settings['target'] = 50000

    if settings_data.chk_size_equals_digit.instate(['selected']):
        settings_data.settings['pixel size equals digit'] = True
    else: settings_data.settings['pixel size equals digit'] = False

    if settings_data.combobox_size_eq_digit_factor.get() != '':
        settings_data.settings['pixel size equals digit scaling factor'] = settings_data.combobox_size_eq_digit_factor.get()
    else: settings_data.settings['pixel size equals digit scaling factor'] = 0.5

    if settings_data.chk_scale_size_over_time.instate(['selected']):
        settings_data.settings['scale size over time'] = True
    else: settings_data.settings['scale size over time'] = False

    if settings_data.chk_highlight_123s.instate(['selected']):
        settings_data.settings['highlight 123s'] = True
    else: settings_data.settings['highlight 123s'] = False

    if settings_data.chk_offset_same_as_point_size.instate(['selected']):
        settings_data.settings['offset same as point size'] = True
    else: settings_data.settings['offset same as point size'] = False

    if settings_data.chk_offset_same_as_digit.instate(['selected']):
        settings_data.settings['offset same as digit'] = True
    else: settings_data.settings['offset same as digit'] = False

    if settings_data.combobox_point_size.get() != '':
        settings_data.settings['point size'] = settings_data.combobox_point_size.get()
    else: settings_data.settings['point size'] = 2

    if settings_data.combobox_highlight_colour.get() != '':
        if settings_data.combobox_highlight_colour.get() == 'Red':
            settings_data.settings['highlight colour'] = (255, 0, 0)
        elif settings_data.combobox_highlight_colour.get() == 'Green':
            settings_data.settings['highlight colour'] = (0, 255, 0)
        elif settings_data.combobox_highlight_colour.get() == 'Blue':
            settings_data.settings['highlight colour'] = (0, 0, 255)
    else: settings_data.settings['highlight colour'] = (255, 0, 0)

    if settings_data.chk_use_colour_dictionary.instate(['selected']):
        settings_data.settings['use colour dictionary'] = True
    else: settings_data.settings['use colour dictionary'] = False

    if settings_data.combobox_bg_colour.get() != '':
        if settings_data.combobox_bg_colour.get() == 'Space Black':
            settings_data.settings['bg colour'] = 'space_black'
        elif settings_data.combobox_bg_colour.get() == 'White':
            settings_data.settings['bg colour'] = 'white'
        elif settings_data.combobox_bg_colour.get() == 'Black':
            settings_data.settings['bg colour'] = 'black'
    else: settings_data.settings['bg colour'] = 'space_black'

    if settings_data.combobox_point_colour.get() != '':
        if settings_data.combobox_point_colour.get() == 'Starfield':
            settings_data.settings['point colour'] = 'starfield'
        elif settings_data.combobox_point_colour.get() == 'Organic':
            settings_data.settings['point colour'] = 'organic'
    else: settings_data.settings['point colour'] = 'starfield'

    return settings_data.settings

def generate_turtle_visualiser_settings(settings_data):
    settings = settings_data.settings

    if settings_data.chk_wait_until_done.instate(['selected']):
        settings['wait until done'] = True
    else: settings['wait until done'] = False

    if settings_data.combobox_pen_size.get() != '':
        settings['pen size'] = int(settings_data.combobox_pen_size.get())
    else: settings['pen size'] = 3

    if settings_data.combobox_frame_skip_interval.get() != '':
        settings['frame skip interval'] = int(settings_data.combobox_frame_skip_interval.get())
    else: settings['frame skip interval'] = 10000

    if settings_data.textfield_target.get() != '':
        settings['target'] = int(settings_data.textfield_target.get())
    else: settings['target'] = 1000000

    if settings_data.combobox_move_distance.get() != '':
        settings['move distance'] = int(settings_data.combobox_move_distance.get())
    else: settings['move distance'] = 0.8

    if settings_data.textfield_output_filename.get() != '':
        settings['output filename'] = settings_data.textfield_output_filename.get()
    else: settings['output filename'] = 'screenshot'

    if settings_data.chk_digit_is_colour.instate(['selected']):
        settings['digit is colour'] = True
    else: settings['digit is colour'] = False

    if settings_data.combobox_digit_colour_palette.get() != '':
        settings['digit colour palette'] = settings_data.combobox_digit_colour_palette.get().lower()
    else: settings['digit colour palette'] = 'starfield'

    if settings_data.chk_cycle_colours.instate(['selected']):
        settings['cycle colours'] = True
    else: settings['cycle colours'] = False

    if settings_data.combobox_cycle_palette.get() != '':
        settings['cycle palette'] = settings_data.combobox_cycle_palette.get().lower()
    else: settings['cycle palette'] = 'cherry blossom'

    if settings_data.combobox_cycle_change_rate.get() != '':
        settings['cycle change rate'] = int(settings_data.combobox_cycle_change_rate.get())
    else: settings['cycle change rate'] = 0.001

    if settings_data.chk_static_colours.instate(['selected']):
        settings['static colours'] = True
    else: settings['static colours'] = False

    if settings_data.chk_add_randomness_to_colour.instate(['selected']):
        settings['add randomness to colour'] = True
    else: settings['add randomness to colour'] = False

    if settings_data.combobox_bg_colour.get() != '':
        settings['bg colour'] = settings_data.combobox_bg_colour.get()
    else: settings['bg colour'] = 'space black'

    if settings_data.chk_digit_is_pen_size.instate(['selected']):
        settings['digit is pen size'] = True
    else: settings['digit is pen size'] = False

    if settings_data.combobox_digit_is_pen_size_scale_factor.get() != '':
        settings['digit pen size scale factor'] = int(settings_data.combobox_digit_is_pen_size_scale_factor.get())
    else: settings['digit pen size scale factor'] = 1

    return settings_data.settings

def generate_spiral_visualiser_settings(settings_data):
    settings = settings_data.settings

    if settings_data.combobox_bg_colour.get() != '':
        settings['bg colour'] = settings_data.combobox_bg_colour.get().lower()

    if settings_data.combobox_offset_increment.get() != '':
        settings['offset increment'] = int(settings_data.combobox_offset_increment.get())

    if settings_data.combobox_digit_colour_palette.get() != '':
        settings['digit colour palette'] = settings_data.combobox_digit_colour_palette.get().lower()

    return settings_data.settings

def generate_waveform_visualiser_settings(settings_data):
    settings = settings_data.settings

    if settings_data.combobox_bg_colour.get() != '':
        settings['bg colour'] = settings_data.combobox_bg_colour.get().lower()
    else: settings['bg colour'] = 'space black'

    if settings_data.combobox_digit_colour_palette.get() != '':
        settings['digit colour palette'] = settings_data.combobox_digit_colour_palette.get().lower()
    else: settings['digit colour palette'] = 'starfield'
    
    return settings_data.settings

def generate_sandpile_visualiser_settings(settings_data):
    settings = settings_data.settings
    
    if settings_data.combobox_bg_colour.get() != '':
        settings['bg colour'] = settings_data.combobox_bg_colour.get().lower()
    else: settings['bg colour'] = 'white'

    if settings_data.combobox_colour_scheme.get() != '':
        settings['colour scheme'] = settings_data.combobox_colour_scheme.get().lower()
    else: settings['colour scheme'] = 'sandyboi'

    if settings_data.combobox_update_interval.get() != '':
        settings['update interval'] = int(settings_data.combobox_update_interval.get())
    else: settings['update interval'] = 20

    return settings_data.settings

if __name__ == '__main__':
    entry_point()