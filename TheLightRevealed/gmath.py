import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, alight, light, areflect, dreflect, sreflect ):
    normal = normalize(normal)
    view = normalize(view)
    light[LOCATION] = normalize(light[LOCATION])

    a = calculate_ambient(alight, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)

    r = a[0] + d[0] + s[0]
    g = a[1] + d[1] + s[1]
    b = a[2] + d[2] + s[2]
    
    i = [r, g, b]
    return limit_color(i)

def calculate_ambient(alight, areflect):
    return map(lambda x: x[0] * x[1], zip(alight, areflect))
    
def calculate_diffuse(light, dreflect, normal):
    dp = dot_product(normal, light[LOCATION])
    return map(lambda x: x[0] * x[1] * dp, zip(light[COLOR], dreflect))
  
def calculate_specular(light, sreflect, view, normal):
    s = [0, 0, 0]
    m = 2 * dot_product(normal, light[LOCATION])
    normal = map(lambda x: x * m, normal)
    r = normal[:]
    r= map(lambda x: x[0] - x[1], zip(r, light[LOCATION]))
    dp = dot_product(view, r)
    dp = (dp ** SPECULAR_EXP) if dp > 0 else 0
    return map(lambda x: x[0] * x[1] * dp, zip(light[COLOR], sreflect))

def limit_color(color): 
    maxes = map(lambda x: 255 if x > 255 else x, color)
    return map(lambda x: 0 if x < 0 else int(x), maxes)

#vector functions
def normalize(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return map(lambda x: x / length, vector)
    
def dot_product(a, b):
    return (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])

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
