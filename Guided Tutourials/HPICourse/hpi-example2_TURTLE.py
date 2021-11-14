# Using the TURLE libraries for graphical interfaces
"""Syntax when calling a library
   from <libraryname> import <functionname>"""

from turtle import *

# Specifiy a moving directions from 0,0
# "forward" "backward" is number of pixels in that directions
# "right" "left" is the degrees that the object turns on the graph
# "speed" increase of lower the speed of the cursor (0-10)
forward (100)
right (90)
forward (100)

# Specify x,y  coordinates
goto (100,100)

# "pendown()" draws a line when moving across the grid (on by default)
# "penup()" lets you move with out drawing a line
# "pencolor()" changes the color of the line (default is black)
# "bgcolor()" changes the color of the grid (default is white)
# "fillcolor()" changes the color of the space inside of a drawn shape
fillcolor("red")
begin_fill()
forward(100)
right(90)
forward(100)
end_fill()

# Put coordinates into a variable and call via the "shape" function
register_shape("my-shape", ((0,10), (5,0), (15,0), (20,10)))
shape("my-shape")

