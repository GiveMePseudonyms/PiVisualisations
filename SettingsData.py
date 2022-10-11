import tkinter as tk
from tkinter import ttk
import HelpButtonInfo

def mbox_help(window, prompt):
    tk.messagebox.Message(master=window)
    tk.messagebox.showinfo(title='Target', message=HelpButtonInfo.tooltips[prompt], icon='info')

class SettingsData:
    def __init__(self, WINDOW):
        self.WINDOW = WINDOW
        self.pixel_visualiser_options = self.PixelVisualiserOptions(self.WINDOW)
        self.turtle_visualiser_options = self.TurtleVisualiserOptions(self.WINDOW)
        self.spiral_visualiser_options = self.SpiralVisualiserOptions(self.WINDOW)
        self.waveform_visualiser_options = self.WaveformVisualiserOptions(self.WINDOW)
        self.sandpile_visualiser_options = self.SandPileVisualiserOptions(self.WINDOW)
        self.web_visualiser_options = self.WebVisualiserOptions(self.WINDOW)
        self.orbital_visualiser_options = self.OrbitalVisualiserOptions(self.WINDOW)

        self.all_widgets = [
            self.pixel_visualiser_options.widgets,
            self.turtle_visualiser_options.widgets,
            self.spiral_visualiser_options.widgets,
            self.waveform_visualiser_options.widgets,
            self.sandpile_visualiser_options.widgets,
            self.web_visualiser_options.widgets,
            self.orbital_visualiser_options.widgets,
        ]

        self.all_labels = [
            self.pixel_visualiser_options.labels,
            self.turtle_visualiser_options.labels,
            self.spiral_visualiser_options.labels,
            self.waveform_visualiser_options.labels,
            self.sandpile_visualiser_options.labels,
            self.web_visualiser_options.labels,
            self.orbital_visualiser_options.labels,
        ]

        self.all_hlp_buttons = [
            self.pixel_visualiser_options.help_buttons,
            self.turtle_visualiser_options.help_buttons,
            self.spiral_visualiser_options.help_buttons,
            self.waveform_visualiser_options.help_buttons,
            self.sandpile_visualiser_options.help_buttons,
            self.web_visualiser_options.help_buttons,
            self.orbital_visualiser_options.help_buttons,
        ]

        self.selection = ''

    def select_visualiser(self, selection):
        self.selection = selection

    def grid_forget_all(self):
        for widgetlist in self.all_widgets:
            for widget in widgetlist:
                widget.grid_forget()

        for labellist in self.all_labels:
            for label in labellist:
                if label != None:
                    label.grid_forget()

        for buttons in self.all_hlp_buttons:
            for button in buttons:
                if button != None:
                    button.grid_forget()
     
        self.WINDOW.update()
    
    class PixelVisualiserOptions:
        def __init__(self, WINDOW):

            self.settings = {
                "animate" : False,
                "target" : 500000,
                "pixel size equals digit" : True,
                "pixel size equals digit scaling factor" : 0.5,
                "scale size over time" : True,
                "scale size over time offset" : True,
                "scale over time division factor" : 1000000000,
                "highlight 123s" : False,
                "offset same as point size" : False,
                "offset same as digit" : False,
                "offset" : 1,
                "point size" : 3,
                "highlight colour" : (255, 0, 0),
                "use colour dictionary" : True,
                "bg colour" : "space_black",
                "point colour" : "starfield",
                }   

            self.chk_animate = ttk.Checkbutton(WINDOW, text="Animate")
            
            self.lbl_texfield_target = ttk.Label(WINDOW, text="Target")
            self.textfield_target = ttk.Entry(WINDOW)
            self.hlp_textfield_target = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'target'))
            
            self.chk_size_equals_digit = ttk.Checkbutton(WINDOW, text="Size = Digit")
            self.hlp_size_equals_digit = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'pixel size equals digit'))
            
            self.lbl_scale_factor = ttk.Label(WINDOW, text="Scale Factor")
            self.combobox_size_eq_digit_factor = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_size_eq_digit_factor['values'] = ('0.25', '0.5', '0.75', '1')
            self.hlp_combobox_size_eq_digit_factor = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'pixel size equals digit scaling factor'))

            self.chk_scale_size_over_time = ttk.Checkbutton(WINDOW, text='Scale size over time')
            self.hlp_chk_scale_size_over_time = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'scale size over time'))

            self.chk_highlight_123s = ttk.Checkbutton(WINDOW, text="Highlight 123s")
            self.hlp_chk_highligh_123s = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'highlight 123s'))

            self.chk_offset_same_as_point_size = ttk.Checkbutton(WINDOW, text="Offset same as point size")
            self.hlp_chk_offset_same_as_point_size = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'offset same as point size'))

            self.chk_offset_same_as_digit = ttk.Checkbutton(WINDOW, text="Offset same as digit")
            self.hlp_chk_offset_same_as_digit = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'offset same as digit'))

            self.lbl_point_size = ttk.Label(WINDOW, text="Point Size")
            self.combobox_point_size = ttk.Combobox(WINDOW)
            self.combobox_point_size['values'] = ('1', '2','3','4','5','6','7','8','9','10')
            self.combobox_point_size.state(['readonly'])
            self.hlp_combobox_point_size = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'point size'))

            self.lbl_combobox_highlight_colour = ttk.Label(WINDOW, text="Highlight colour")
            self.combobox_highlight_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_highlight_colour['values'] = ('Red', 'Green', 'Blue')
            self.hlp_combobox_highlight_colour = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'highlight colour'))

            self.chk_use_colour_dictionary = ttk.Checkbutton(WINDOW, text='Use colour dictionary')
            self.hlp_chk_use_colour_dictionary = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'use colour dictionary'))

            self.lbl_combobox_bg_colour = ttk.Label(WINDOW, text="Background Colour")
            self.combobox_bg_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_bg_colour['values'] = ('Black', 'White', 'Space Black')
            self.hlp_combobox_bg_colour = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'background colour'))

            self.lbl_combobox_point_colour = ttk.Label(WINDOW, text="Point Colour")
            self.combobox_point_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_point_colour['values'] = ('Organic', 'Starfield')
            self.hlp_combobox_point_colour = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'point colour'))

            self.widgets = []
            self.widgets.extend([
                self.chk_animate, 
                self.textfield_target, 
                self.chk_size_equals_digit,
                self.combobox_size_eq_digit_factor,
                self.chk_scale_size_over_time,
                self.chk_highlight_123s,
                self.chk_offset_same_as_point_size,
                self.chk_offset_same_as_digit,
                self.combobox_point_size,
                self.combobox_highlight_colour,
                self.chk_use_colour_dictionary,
                self.combobox_bg_colour,
                self.combobox_point_colour
                                ])

            self.labels = [
                None,
                self.lbl_texfield_target,
                None,
                self.lbl_scale_factor,
                None,
                None,
                None,
                None,
                self.lbl_point_size,
                self.lbl_combobox_highlight_colour,
                None,
                self.lbl_combobox_bg_colour,
                self.lbl_combobox_point_colour
            ]

            self.help_buttons = [
                None,
                self.hlp_textfield_target,
                self.hlp_size_equals_digit,
                self.hlp_combobox_size_eq_digit_factor,
                self.hlp_chk_scale_size_over_time,
                self.hlp_chk_highligh_123s,
                self.hlp_chk_offset_same_as_point_size,
                self.hlp_chk_offset_same_as_digit,
                self.hlp_combobox_point_size,
                self.hlp_combobox_highlight_colour,
                self.hlp_chk_use_colour_dictionary,
                self.hlp_combobox_bg_colour,
                self.hlp_combobox_point_colour,
            ]

    class TurtleVisualiserOptions:
        def __init__(self, WINDOW):
            
            self.settings = {
                'pen size': 5,
                "wait until done": True,
                "frame skip interval": 10000,
                'target': 1000000,
                'move distance': 0.8,
                'output filename': 'screenshot',
                'digit is colour': False,
                'digit colour palette': 'starfield',
                'cycle colours': True,
                'cycle palette': 'cy cherry blossom',
                'cycle change rate': 0.001,
                'static colours': False,
                'palette': 'blue autumn',
                'add randomness to colour': True,
                'bg colour': 'space black',
                'digit is pen size': False,
                'digit pen size scale factor': 1
            }

            self.lbl_combobox_pen_size = ttk.Label(WINDOW, text='Pen size')
            self.combobox_pen_size = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_pen_size['values'] = ['3', '6', '9', '12', '15']
            self.hlp_combobox_pen_size = tk.Button(WINDOW, text='?', command=lambda: mbox_help(WINDOW, 'pen size'))

            self.chk_wait_until_done = ttk.Checkbutton(WINDOW, text='Wait until done')
            self.hlp_wait_until_done = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'wait until done'))

            self.lbl_combobox_frame_skip_interval = ttk.Label(WINDOW, text='Frame skip interval')
            self.combobox_frame_skip_interval = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_frame_skip_interval['values'] = ['5000', '10000', '15000', '20000']
            self.hlp_combobox_frame_skip_interval = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'frame skip interval'))

            self.lbl_textfield_target = ttk.Label(WINDOW, text='Target')
            self.textfield_target = ttk.Entry(WINDOW)
            self.hlp_textfield_target = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'target'))

            self.lbl_combobox_move_distance = ttk.Label(WINDOW, text='Move distance')
            self.combobox_move_distance = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_move_distance['values'] = ['0.2', '0.4', '0.6', '0.8', '1']
            self.hlp_combobox_move_distance = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'move distance'))
            
            self.lbl_textfield_output_filename = ttk.Label(WINDOW, text='Screenshot filename')
            self.textfield_output_filename = ttk.Entry(WINDOW)
            self.hlp_textfield_output_filename = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'output filename'))

            self.chk_digit_is_colour = ttk.Checkbutton(WINDOW, text='Digit corresponds to colour')
            self.hlp_chk_digit_is_colour = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'digit is colour'))

            self.lbl_combobox_digit_colour_palette = ttk.Label(WINDOW, text='Digit colour palette')
            self.combobox_digit_colour_palette = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_digit_colour_palette['values'] = ['Starfield', 'Yellow and Purple', 'Mint']
            self.hlp_combobox_digit_colour_palette = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'digit colour palette'))

            self.chk_cycle_colours = ttk.Checkbutton(WINDOW, text='Cycle colours')
            self.hlp_chk_cycle_colours = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'cycle colours'))

            self.lbl_combobox_cycle_palette = ttk.Label(WINDOW, text='Cycle Palette')
            self.combobox_cycle_palette = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_cycle_palette['values'] = ['Cherry Blossom', 'All Black', 'Metallic Flake', 'Blue Autumn']
            self.hlp_combobox_cycle_palette = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'cycle palette'))

            self.lbl_combobox_cycle_change_rate = ttk.Label(WINDOW, text='Cycle change rate')
            self.combobox_cycle_change_rate = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_cycle_change_rate['values'] = ['0.001', '0.003', '0.005', '0.007']
            self.hlp_combobox_cycle_change_rate = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'cycle change rate'))

            self.chk_static_colours = ttk.Checkbutton(WINDOW, text='Static Colours')
            self.hlp_chk_static_colours = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'static colours'))

            self.chk_add_randomness_to_colour = ttk.Checkbutton(WINDOW, text='Add randomness to colour')
            self.hlp_chk_add_randomness_to_colour = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'add randomness to colour'))

            self.lbl_combobox_bg_colour = ttk.Label(WINDOW, text='Background Colour')
            self.combobox_bg_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_bg_colour['values'] = ['White', 'Black', 'Space Black', 'Red', 'Green', 'Blue']
            self.hlp_combobox_bg_colour = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'background colour'))

            self.chk_digit_is_pen_size = ttk.Checkbutton(WINDOW, text='Digit is pen size')
            self.hlp_chk_digit_is_pen_size = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'digit is pen size'))
            
            self.lbl_combobox_digit_is_pen_size_scale_factor = ttk.Label(WINDOW, text='Pen size scaling factor')
            self.combobox_digit_is_pen_size_scale_factor = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_digit_is_pen_size_scale_factor['values'] = ['0.5', '1', '1.5']
            self.hlp_combobox_digit_is_pen_size_scale_factor = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'pen size scaling factor'))

            self.widgets = []
            self.widgets.extend([
                self.chk_wait_until_done,
                self.combobox_pen_size,
                self.combobox_frame_skip_interval,
                self.textfield_target,
                self.combobox_move_distance,
                self.textfield_output_filename,
                self.chk_digit_is_colour,
                self.combobox_digit_colour_palette,
                self.chk_cycle_colours,
                self.combobox_cycle_palette,
                self.combobox_cycle_change_rate,
                self.chk_static_colours,
                self.chk_add_randomness_to_colour,
                self.combobox_bg_colour,
                self.chk_digit_is_pen_size,
                self.combobox_digit_is_pen_size_scale_factor
            ])

            self.labels = [
                None,
                self.lbl_combobox_pen_size,
                self.lbl_combobox_frame_skip_interval,
                self.lbl_textfield_target,
                self.lbl_combobox_move_distance,
                self.lbl_textfield_output_filename,
                None,
                self.lbl_combobox_digit_colour_palette,
                None,
                self.lbl_combobox_cycle_palette,
                self.lbl_combobox_cycle_change_rate,
                None,
                None,
                self.lbl_combobox_bg_colour,
                None,
                self.lbl_combobox_digit_is_pen_size_scale_factor
            ]

            self.help_buttons = [
                self.hlp_wait_until_done,
                self.hlp_combobox_pen_size,
                self.hlp_combobox_frame_skip_interval,
                self.hlp_textfield_target,
                self.hlp_combobox_move_distance,
                self.hlp_textfield_output_filename,
                self.hlp_chk_digit_is_colour,
                self.hlp_combobox_digit_colour_palette,
                self.hlp_chk_cycle_colours,
                self.hlp_combobox_cycle_palette,
                self.hlp_combobox_cycle_change_rate,
                self.hlp_chk_static_colours,
                self.hlp_chk_add_randomness_to_colour,
                self.hlp_combobox_bg_colour,
                self.hlp_chk_digit_is_pen_size,
                self.hlp_combobox_digit_is_pen_size_scale_factor,
            ]
    
    class SpiralVisualiserOptions:
        def __init__(self, WINDOW):
            self.settings = {
                'bg colour' : 'space black',
                "offset increment": 0.5,
                'digit colour palette': 'starfield'
            }

            self.lbl_combobox_bg_colour = ttk.Label(WINDOW, text='Background colour')
            self.combobox_bg_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_bg_colour['values'] = ['Space Black', 'White', 'Black', 'Red', 'Green', 'Blue']
            self.hlp_combobox_bg_colour = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'background colour'))

            self.lbl_combobox_offset_increment = ttk.Label(WINDOW, text='Offset increment')
            self.combobox_offset_increment = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_offset_increment['values'] = ['0.25', '0.5', '0.75', '1']
            self.hlp_combobox_offset_increment = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'offset increment'))

            self.lbl_combobox_digit_colour_palette = ttk.Label(WINDOW, text='Digit colour palette')
            self.combobox_digit_colour_palette = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_digit_colour_palette['values'] = ['Starfield', 'Yellow and Purple', 'Mint', 'Peach and Purple']
            self.hlp_combobox_digit_colour_palette = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'digit colour palette'))

            self.widgets= [
                self.combobox_bg_colour,
                self.combobox_offset_increment,
                self.combobox_digit_colour_palette,
            ]

            self.labels = [
                self.lbl_combobox_bg_colour,
                self.lbl_combobox_offset_increment,
                self.lbl_combobox_digit_colour_palette,
            ]

            self.help_buttons = [
                self.hlp_combobox_bg_colour,
                self.hlp_combobox_offset_increment,
                self.hlp_combobox_digit_colour_palette,
            ]

    class WaveformVisualiserOptions:
        def __init__(self, WINDOW):
            self.settings = {
                'bg colour': 'space black',
                'digit colour palette' : 'starfield', 
            }

            self.lbl_combobox_bg_colour = ttk.Label(WINDOW, text='Background colour')
            self.combobox_bg_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_bg_colour['values'] = ['Space Black', 'White', 'Black', 'Red', 'Green', 'Blue']
            self.hlp_combobox_bg_colour = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'background colour'))

            self.lbl_combobox_digit_colour_palette = ttk.Label(WINDOW, text='Digit colour palette')
            self.combobox_digit_colour_palette = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_digit_colour_palette['values'] = ['Starfield', 'Yellow and Purple', 'Mint', 'Peach and Purple']
            self.hlp_combobox_digit_colour_palette = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'digit colour palette'))

            self.widgets = [
                self.combobox_bg_colour,
                self.combobox_digit_colour_palette,
            ]

            self.labels = [
                self.lbl_combobox_bg_colour,
                self.lbl_combobox_digit_colour_palette,
            ]

            self.help_buttons = [
                self.hlp_combobox_bg_colour,
                self.hlp_combobox_digit_colour_palette,
            ]

    class SandPileVisualiserOptions:
        def __init__(self, WINDOW):
            self.settings = {
                'bg colour': 'white',
                'colour scheme': 'sandyboi',
                'update interval': 20,
            }

            self.lbl_combobox_bg_colour = ttk.Label(WINDOW, text='Background colour')
            self.combobox_bg_colour = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_bg_colour['values'] = ['Space Black', 'White', 'Black', 'Red', 'Green', 'Blue']
            self.hlp_combobox_bg_colour = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'background colour'))

            self.lbl_combobox_colour_scheme = ttk.Label(WINDOW, text='Colour scheme')
            self.combobox_colour_scheme = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_colour_scheme['values'] = ['Sand', 'Pastels', 'Square', 'Washed Pastels']
            self.hlp_combobox_colour_scheme = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'colour scheme'))

            self.lbl_combobox_update_interval = ttk.Label(WINDOW, text='Update interval')
            self.combobox_update_interval = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_update_interval['values'] = ['1', '10', '20', '50', '100', '250', '1000']
            self.hlp_combobox_update_interval = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'frame skip interval'))

            self.widgets = [
                self.combobox_bg_colour,
                self.combobox_colour_scheme,
                self.combobox_update_interval,
            ]

            self.labels = [
                self.lbl_combobox_bg_colour,
                self.lbl_combobox_colour_scheme,
                self.lbl_combobox_update_interval,
            ]

            self.help_buttons = [
                self.hlp_combobox_bg_colour, 
                self.hlp_combobox_colour_scheme,
                self.hlp_combobox_update_interval,
            ]

    class WebVisualiserOptions:
        def __init__(self, WINDOW):
            self.settings = {
                'target': 10000,
                'random offset upper bound': 20,
                'random offset lower bound': 0,
                'colour palette': 'peach and purple',
                'use random colours': False,
                'update interval': 1000,
            }

            self.lbl_textfield_target = ttk.Label(WINDOW, text='Target')
            self.textield_target = ttk.Entry(WINDOW)
            self.hlp_textfield_target = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'target'))

            self.lbl_textfield_update_interval = ttk.Label(WINDOW, text='Update interval')
            self.textfield_update_interval = ttk.Entry(WINDOW)
            self.hlp_textfield_update_interval = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'frame skip interval'))

            self.lbl_combobox_random_offset_upper_bound = ttk.Label(WINDOW, text='Random offset upper bound')
            self.combobox_random_offset_upper_bound = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_random_offset_upper_bound['values'] = ['10', '20', '30', '40', '50']
            self.hlp_combobox_random_offset_upper_bound = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'random offset bound'))

            self.lbl_combobox_random_offset_lower_bound = ttk.Label(WINDOW, text='Random offset lower bound')
            self.combobox_random_offset_lower_bound = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_random_offset_lower_bound['values'] = ['0', '1', '2', '3', '4', '5']
            self.hlp_combobox_random_offset_lower_bound = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'random offset bound'))

            self.lbl_combobox_colour_palette = ttk.Label(WINDOW, text='Colour palette')
            self.combobox_colour_palette = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_colour_palette['values'] = ['Starfield', 'Yellow and Purple', 'Mint', 'Peach and Purple']
            self.hlp_combobox_colour_palette = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'colour palette'))

            self.chk_use_random_colours = ttk.Checkbutton(WINDOW, text='Use random colours')

            self.widgets = [
                self.textield_target,
                self.textfield_update_interval,
                self.combobox_random_offset_upper_bound,
                self.combobox_random_offset_lower_bound,
                self.combobox_colour_palette,
                self.chk_use_random_colours,
            ]

            self.labels = [
                self.lbl_textfield_target,
                self.lbl_textfield_update_interval,
                self.lbl_combobox_random_offset_upper_bound,
                self.lbl_combobox_random_offset_lower_bound,
                self.lbl_combobox_colour_palette,
                None,
            ]

            self.help_buttons = [
                self.hlp_textfield_target,
                self.hlp_textfield_update_interval,
                self.hlp_combobox_random_offset_upper_bound,
                self.hlp_combobox_random_offset_lower_bound,
                self.hlp_combobox_colour_palette,
            ]

    class OrbitalVisualiserOptions:
        def __init__(self, WINDOW):
            self.settings = {
                'line opacity': 70,
            }
            
            self.lbl_combobox_line_opacity = ttk.Label(WINDOW, text='Line opacity')
            self.combobox_line_opacity = ttk.Combobox(WINDOW, state='readonly')
            self.combobox_line_opacity['values'] = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
            self.hlp_combobox_line_opacity = tk.Button(WINDOW, text='?', command= lambda: mbox_help(WINDOW, 'line opacity'))

            self.widgets = [
                self.combobox_line_opacity,
            ]

            self.labels = [
                self.lbl_combobox_line_opacity,
            ]

            self.help_buttons = [
                self.hlp_combobox_line_opacity,
            ]