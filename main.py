from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "start matrix"
#mess up matrix
for i in matrix:
    for j in range(len(matrix)):
        i[j] = 50

print_matrix(matrix)
print "end matrix"

print "start matrix"
ident(matrix)
print_matrix(matrix)
print "end matrix"

print "start matrix"
add_point(matrix, 9, 8, 7)
add_point(matrix, 0, 0, 0)
print_matrix(matrix)
print "end matrix"

print "start matrix"
add_edge(matrix, 9, 8, 7, 10, 9, 8)
print_matrix(matrix)
print "end matrix"

draw_lines( matrix, screen, color )
display(screen)
