from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

matrix = make_translate(5, 6, 7)
print_matrix(matrix)
#parse_file( 'script', edges, transform, screen, color )
