import math

def make_translate( x, y, z ):
    matrix = new_matrix(4,3)
    ident(matrix)
    matrix.append( [x, y, z, 1] )
    return matrix
def make_scale( x, y, z ):
    matrix = new_matrix()
    ident(matrix, x, y, z)
    return matrix

#helper methods for rotation, makes angles easier
def cos( theta ):
    return round(math.cos(math.radians(theta)), 2)
def sin( theta ):
    return round(math.sin(math.radians(theta)), 2)

def make_rotZ( theta ):    
    matrix = new_matrix()
    ident(matrix)
    c = cos(theta)
    s = sin(theta)
    matrix[0][0] = matrix[1][1] = c
    matrix[0][1] = s
    matrix[1][0] = -s
    return matrix

def make_rotX( theta ):
    matrix = new_matrix()
    ident(matrix)
    c = cos(theta)
    s = sin(theta)
    matrix[1][1] = matrix[2][2] = c
    matrix[1][2] = s
    matrix[2][1] = -s
    return matrix

def make_rotY( theta ):
    matrix = new_matrix()
    ident(matrix)
    c = cos(theta)
    s = sin(theta)
    matrix[0][0] = matrix[2][3] = c
    matrix[2][0] = s
    matrix[0][3] = -s
    return matrix

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + '\t'
        s+= '\n'
    print s

def ident( matrix, x = 1, y = 1, z = 1 ):
    nums = [x, y, z]
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            i  = 1#customizable diagonal
            if(r < 3):
                i = nums[r]
            if r == c:
                matrix[c][r] = i
            else:
                matrix[c][r] = 0
    return matrix

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
