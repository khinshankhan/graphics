from display import *
from draw import *
from parsr import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
poly = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

#parse_file( 'script', edges, transform, screen, color )
parse_file( 'test', poly, edges, transform, screen, color )
