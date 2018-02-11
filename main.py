from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 0 ]

color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color3 = [ 0, 0, 255 ]
color4 = [ 255, 255, 0 ]
draw_line(0, 250, 250, 250, screen, color1)
draw_line(250, 250, 500, 250, screen, color2)
draw_line(250, 0, 250, 250, screen, color3)
draw_line(250, 250, 250, 500, screen, color4)

display(screen)
save_extension(screen, 'img.png')
