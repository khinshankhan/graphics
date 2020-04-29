from display import *
from matrix import *
from draw import *
import os

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

# Returns True if End-Of-File is reached (helper method)
def EOF(f):
    current_pos = f.tell()
    file_size = os.fstat(f.fileno()).st_size
    return current_pos >= file_size

#real parse_file method
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
            #fixing a weird float issue
            for i in points:
                for j in range(len(i)):
                    i[j] = int(i[j])
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
