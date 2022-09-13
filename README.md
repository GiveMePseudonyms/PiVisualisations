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


The hare.py class:
I found that python's inbuilt Turtle was slow and didn't offer the level of control/customisation I needed, so I build a faster version called the Hare. The Hare allows for more granularity over skipping frames, drawing speeds, etc.