from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
'''
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
'''

#https://i.stack.imgur.com/oFncU.png

m1 = new_matrix(0,4) 
m2 = new_matrix(0,4)
add_point(m1, 5, 0, 3)
add_point(m1, 2, 6, 8)
m1[3][1] = 8
add_point(m1, 6, 2, 1)
m1[3][2] = 5
add_point(m1, 1, 0, 4)
m1[3][3] = 6

add_point(m2, 7, 1, 9)
m2[3][0] = 5
add_point(m2, 5, 8, 4)
m2[3][1] = 3
add_point(m2, 8, 2, 3)
m2[3][2] = 7
add_point(m2, 0, 6, 8)
m2[3][3] = 9

print "m1"
print_matrix(m1)
print "m2"
print_matrix(m2)
print "m1xm2"
matrix_mult( m1, m2 )
print_matrix(m2)
#draw_lines( matrix, screen, color )
#display(screen)
