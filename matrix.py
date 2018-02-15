import math


def print_matrix( matrix ):
    for i in matrix:
        print i

def ident( matrix ):
    #fill matrix up with 0s
    for i in matrix:
        for j in range(len(matrix)):
            i[j] = 0
    #make diagonal of 1
    for c, i in zip(range(4), matrix):
        i[c] = 1

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
