import math

#assumes 2d matrix
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
    result = new_matrix(len(m2[0]), len(m2))
    for i in range(len(m1)):
        for j in range(len(m2[0])): 
            for k in range(len(m2)): 
                result[i][j] += m1[i][k] * m2[k][j]
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            m2[i][j] = result[i][j]
    return m2



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
