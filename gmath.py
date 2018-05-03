import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normal = normalize(normal)
    view = normalize(view)
    light[0] = normalize(light[0])

    a = calculate_ambient(alight, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)

    r = a[0] + d[0] + s[0]
    g = a[1] + d[1] + s[1]
    b = a[2] + d[2] + s[2]
    
    i = [r, g, b]
    return limit_color(i)

def calculate_ambient(alight, areflect):
    return alight * areflect

def calculate_diffuse(light, dreflect, normal):
    l = [normalize(normal), normalize(light[0]), normalize(normal)]
    return (2 * dot_product(reduce(dot_product,l), l[0]))

def calculate_specular(light, sreflect, view, normal):
    pass

def limit_color(color):
    #return 
    return map(lambda x: 255 if x > 255 else int(x), color)

#vector functions
def normalize(vector):
    m = (reduce(lambda x, y: x**2 + y**2, vector))**(0.5)
    return map(lambda x: (int((x/m) * 100))/100, vector)

def dot_product(a, b):
    return reduce(lambda x, y: (x[0] * x[1]) + (y[0] * y[1]), [a, b])

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
