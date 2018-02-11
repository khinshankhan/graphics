from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 0 ]

color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color3 = [ 0, 0, 255 ]
color4 = [ 255, 255, 0 ]
color5 = [ 0, 255, 255 ]
color6 = [ 150, 150, 0 ]
color7 = [ 255, 192, 203 ]
color8 = [ 0, 150, 150 ]

draw_line(0, 250, 250, 250, screen, color1)
draw_line(250, 250, 500, 250, screen, color2)
draw_line(250, 0, 250, 250, screen, color3)
draw_line(250, 250, 250, 500, screen, color4)
draw_line(0, 0, 250, 250, screen, color5)
draw_line(500, 500, 250, 250, screen, color6)
draw_line(250, 250, 500, 0, screen, color7)
draw_line(0, 500, 250, 250, screen, color8)

display(screen)
save_extension(screen, 'img.png')
