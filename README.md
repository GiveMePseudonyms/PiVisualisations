# PiVisualisations

## General Info:
This is a project I started in August 2022 in order to visualise millions of digits of Pi.

Users can choose a visualiser and choose their own settings using the settings GUI:
<img width="700" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/195142695-399f3b74-60d0-4e88-a214-fca69a915e72.png">

### The hare.py class
I found that python's inbuilt Turtle was slow and didn't offer the level of control/customisation I needed, so I built a faster version called the Hare. The Hare allows for more granularity over skipping frames, drawing speeds, and is much faster than the Turtle.

### The Orbital Visualiser:
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619337-e19636b0-6b8b-4f49-a55d-61e056b6683b.png">
The orbital visualiser is a rough emulation of two bodies orbiting a central star. Lines are drawn between the two orbiting bodies at a given interval (in this case 314 - the first 3 digits of Pi). Orbits are determined by a distance to the sun (radius) and a speed which are plugged into basic sin/cos equations to produce circular motion.

### The Pixel Visualiser:
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619428-d2ab6898-9787-4c77-92d9-7ecaf8f284e1.png">
The pixel visualiser produces an outward-moving square spiral. The colour, size and distance offset of each 'pixel' can be linked to each successive digit of Pi. This was the first visualiser I created.

### The Sandpile Visualiser (self-organising criticality sim):
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619470-0f364881-12a3-4ba7-a66b-7f70d69481f8.png">
The sandpile visualiser is a self-organising criticality simulator based upon the Abelian sandpile model. In this version, 31415 'grains' of sand are placed in the central cell. You can learn more about Abelian Sandpiles here: https://www.youtube.com/watch?v=1MtEUErz7Gg

### The Spiral Visualiser:
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619499-7c20e0fd-8748-46d2-8e64-3f1d09ef32d8.png">
The spiral visualiser works in a similar way to the Pixel visualiser except for the fact that it uses a perfect spiral to create visualisations. Often visualisations look like galaxies or sunflowers (especially when the angular offset is close to the golden ratio of 1: 1.1168).

### The Turtle Visualiser:
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619583-9b49f66a-6603-4f18-ae01-0055ea76ab4d.png">
The turtle visualiser uses a 'turtle' object which creates lines based upon the path it takes. The angle at which it turns is based upon the digit of Pi given to it. This means that Pi can be 'mapped out'.

### The Waveform Visualiser:
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619829-981cff50-5dfc-47cb-9d2b-720f9edcac06.png">
The waveform visualiser prints each digit of Pi line by line. Each digit is represented by a coloured square whose position, colour, and size can depend on the corresponding digit of Pi.

### The Web Visualiser:
<img width="600" height="600" alt="image" src="https://user-images.githubusercontent.com/113452530/194619669-28bf537a-fb4d-4077-aa99-a8fb70198ca2.png">
The web visualiser maps the path of Pi and the prevelence of connections between digits. The visualiser features the digits 0-9 in a circle. For each sequence of digits, a line is drawn from the first digit to the next. This creates 'web' patterns.
