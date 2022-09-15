# PiVisualisations

A project I created in August 2022 to visualise millions of digits of Pi. This is a work in progress!

Todo:
Standardisation:
    
At the moment, many global vars like window size are declare per visualiser since they were build individually. This should be standardised with the entry point overhaul below.

There are also differing naming conventions across files which need to be standardised. An example of this is that in some files, global vars are prefixed with GLOBAL, but in others I have shortened it to GL.
    
Major entry point overhaul:
        
Allow the user to select a visualiser and see a preview image of it as well as choose the settings they want to use

Just pass them in as commands and use tkinter to get them from the user. This will require checking for empty fields.
    
General overhaul to allow the user to choose to save a screenshot of the canvas they create.
    
General bugfixes incl image quality, window sizes etc.

General Info:
This is a project I started in August 2022 in order to visualise millions of digits of Pi.

Stack:
In Python,
Pygame,
Tkinter,


Colour Schemes:
Many of the visualisers below can make use of the various colour scheme dictionary files.

The hare.py class:
I found that python's inbuilt Turtle was slow and didn't offer the level of control/customisation I needed, so I built a faster version called the Hare. The Hare allows for more granularity over skipping frames, drawing speeds, and is much faster than the Turtle.

The Orbital Visualiser:
The orbital visualiser is a rough emulation of two bodies orbiting a central star. Lines are drawn between the two orbiting bodies at a given interval (in this case 314 - the first 3 digits of Pi). Orbits are determined by a distance to the sun (radius) and a speed which are plugged into basic sin/cos equations to produce circular motion.

The Pixel Visualiser:
The pixel visualiser produces an outward-moving square spiral. The colour, size and distance offset of each 'pixel' can be linked to each successive digit of Pi. This was the first visualiser I created.

The Sandpile Visualiser (self-organising criticality sim):
The sandpile visualiser is a self-organising criticality simulator based upon the Abelian sandpile model. In this version, 31415 'grains' of sand are placed in the central cell. You can learn more about Abelian Sandpiles here: https://www.youtube.com/watch?v=1MtEUErz7Gg

The Spiral Visualiser:
The spiral visualiser works in a similar way to the Pixel visualiser except for the fact that it uses a perfect spiral to create visualisations. Often visualisations look like galaxies or sunflowers (especially when the angular offset is close to the golden ratio of 1: 1.1168).

The Turtle Visualiser:
The turtle visualiser uses a 'turtle' object which creates lines based upon the path it takes. The angle at which it turns is based upon the digit of Pi given to it. This means that Pi can be 'mapped out'.

The Waveform Visualiser:
The waveform visualiser prints each digit of Pi line by line. Each digit is represented by a coloured square whose position, colour, and size can depend on the corresponding digit of Pi.

The Web Visualiser:
The web visualiser maps the path of Pi and the prevelence of connections between digits. The visualiser features the digits 0-9 in a circle. For each sequence of digits, a line is drawn from the first digit to the next. This creates 'web' patterns.