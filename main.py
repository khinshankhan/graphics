from display import *
from draw import *

screen = new_screen()
color = [ 0, 150, 0 ]

color1 = [ 255, 0, 0 ]
color2 = [ 0, 255, 0 ]
color3 = [ 0, 0, 255 ]
color4 = [ 255, 255, 0 ]

radius1 = 500
radius2 = 0
x = 250
y = 250

for i in range(1,500):
    draw_line(x, y, radius1 + (20 * i), radius1 - (20 * i), screen, color1)
    draw_line(x, y, radius1 - (20 * i), radius1 + (20 * i), screen, color2)
    draw_line(x, y, radius2 + (20 * i), radius2 - (20 * i), screen, color3)
    draw_line(x, y, radius2 - (20 * i), radius2 + (20 * i), screen, color4)

#mystery yellow in the middle might be fun actually
#draw_line(x, y, 250, 500, screen, color)

display(screen)
save_extension(screen, 'img.png')
