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

print "start matrix made into ident"
ident(matrix)
print_matrix(matrix)

print "add 3 points to the matrix"
add_point(matrix, 9, 8, 7)
add_point(matrix, 7, 7, 7)
add_point(matrix, 0, 0, 0)
print_matrix(matrix)

print "add an edge to matrix"
add_edge(matrix, 9, 8, 7, 10, 9, 8)
print_matrix(matrix)

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

matrixd = new_matrix()
add_edge( matrixd, 0, 0, 0, 0, 100, 0 )
add_edge( matrixd, 100, 0, 0, 100, 100, 0 )
add_edge( matrixd, 0, 0, 0, 100, 0, 0 )
add_edge( matrixd, 0, 100, 0, 100, 100, 0 )
print "matrix drawing"
print_matrix(matrixd)
draw_lines( matrixd, screen, color )

print "tranlating matrix 4 times, (print 1 eg on console)"
matrixt = new_matrix()
ident(matrixt)
matrixt[0][3] = 399
print_matrix(matrixt)
matrix_mult( matrixt, matrixd )

print "translated matrix drawing (square in every corner and center)\n (print 1 eg on console)"
print_matrix(matrixd)
draw_lines( matrixd, screen, color )

ident(matrixt)
matrixt[1][3] = 399
matrix_mult( matrixt, matrixd )
draw_lines( matrixd, screen, color )

ident(matrixt)
matrixt[0][3] = -399
matrix_mult( matrixt, matrixd )
draw_lines( matrixd, screen, color )

ident(matrixt)
matrixt[0][3] = 200
matrixt[1][3] = -200
matrix_mult( matrixt, matrixd )
add_edge(matrixd, 200, 200, 0, 300, 300, 0)
add_edge(matrixd, 200, 300, 0, 300, 200, 0)
add_edge(matrixd, 250, 300, 0, 250, 200, 0)
add_edge(matrixd, 200, 250, 0, 300, 250, 0)
print_matrix(matrixd)
draw_lines( matrixd, screen, color )
display(screen)
