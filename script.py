import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [0,
              255,
              255]]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 20

    p = mdl.parseFile(filename)
    
    if p:
        #print p
        (commands, symbols) = p
        print '###################'
        print commands
        #print len(commands)
        #print len(commands[1])
        print '###################'
        #print symbols
                
        for i in range(0, len(commands)):
            command = commands[i][0]
            args = []
            for j in range(1, len(commands[i])):
                args.append(commands[i][j])
            #print (command, args)
            execute(command, args)
    else:
        print "Parsing failed."
        return

def execute(command, args):
    pass
