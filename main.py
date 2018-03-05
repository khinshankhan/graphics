from display import *
from draw import *
#from parser import *
from matrix import *
import os

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

'''
print "Translation Matrix Creation"
matrix = make_translate(5, 6, 7)
print_matrix(matrix)

print "Rot X Matrix Creation"
matrix = make_rotX(30)
print_matrix(matrix)
print "Rot Y Matrix Creation"
matrix = make_rotY(30)
print_matrix(matrix)
print "Rot z Matrix Creation"
matrix = make_rotZ(30)
print_matrix(matrix)

print "Scale Matrix Creation"
matrix = make_scale(5, 10, 20)
print_matrix(matrix)

'''
# Returns True if End-Of-File is reached
def EOF(f):
    current_pos = f.tell()
    file_size = os.fstat(f.fileno()).st_size
    return current_pos >= file_size

def parse_file( fname, points, transform, screen, color ):
    f = open(fname) #open file
    
    line = f.readline().strip() #setup initial line
    while(True):
        if(line == 'line'):
            nums = f.readline().strip().split(' ')
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            add_edge(points, nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
            #print_matrix(points)
        elif line == 'ident': 
			ident(transform)
	elif line == 'scale':
            nums = f.readline().strip().split(' ')
            for i in range(len(nums)):
                nums[i] = int(nums[i])
	    scale = make_scale(nums[0], nums[1], nums[2])
            matrix_mult(scale, transform)
        elif line == 'move':
            nums = f.readline().strip().split(' ')
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            trans = make_translate(nums[0], nums[1], nums[2])
            matrix_mult(trans, transform)
        elif line == 'rotate':
            rot = f.readline().strip().split(' ')
            rot[1] = int(rot[1])
            if rot[0] == 'x': 
                rot = make_rotX(rot[1])
            if rot[0] == 'y': 
                rot = make_rotY(rot[1])
            if rot[0] == 'z': 
                rot = make_rotZ(rot[1])
            matrix_mult(rot, transform)
        elif line == 'apply': 
	    matrix_mult(transform, points)
        elif line == 'display':
            clear_screen(screen)
	    draw_lines(points, screen, color)
	    display(screen)
        elif line == 'save':
	    save_extension(screen, f.readline().strip())
                
        #next run set up
        line = f.readline().strip()
        if(EOF(f) or line == 'quit'):
            break
        
    f.close() #close file

parse_file( 'script', edges, transform, screen, color )
