from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

#parse_file( 'script', edges, transform, screen, color )

add_polygon(edges, 100, 50, 0, 250, 250, 0, 400, 50, 0)
print_matrix(edges)

draw_polygons(edges, screen, color)

display(screen)
