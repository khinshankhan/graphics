from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

'''
matrix = make_translate(5, 6, 7)
print_matrix(matrix)
'''
matrix = make_rotX(30)
print_matrix(matrix)
matrix = make_rotY(30)
print_matrix(matrix)
matrix = make_rotZ(30)
print_matrix(matrix)
matrix = make_scale(5, 10, 20)
print_matrix(matrix)
#parse_file( 'script', edges, transform, screen, color )
