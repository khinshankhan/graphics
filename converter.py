import os
import sys

windows_replace = {'parser':'parsr', 'parser.py':'parsr.py', 'save_extension(screen, args[0])':'save_ppm(screen, args[0])'}
revert_replace = {'parsr':'parser', 'parsr.py':'parser.py', 'save_ppm(screen, args[0])':'save_extension(screen, args[0])'}
wordReplacements = {'hi':'hello'}

def transform_line(line, choice):
    if (choice == "windows"):
            wordReplacements = windows_replace
    elif (choice == "revert"):
        wordReplacements = revert_replace
    
    for key, value in wordReplacements.iteritems():
        line = line.replace(key, value)
    wordReplacements = {'hi':'hello'}
    return line

def replace_file(fname, choice):
    with open("temp_file", "w") as output_file, open(fname) as input_file:
        for line in input_file:
            output_file.write(transform_line(line, choice))
    os.remove(fname)
    os.rename("temp_file", fname)

def run():
    sys.stdout.flush()
    print 'windows will convert files to work with a windows system'
    print 'note your script shouldnt use display, and should save as a ppm'
    print 'revert will convert files back to normal linux use'
    print
    print 'Now choose either: windows or revert'
    sys.stdout.flush()
    choice = raw_input()
    if (choice == "windows" or choice == "revert"):
        if (choice == "windows"):
            os.rename("parser.py", "parsr.py")
            replace_file("parsr.py", choice)
        elif (choice == "revert"):
            os.rename("parsr.py", "parser.py")
            replace_file("parser.py", choice)
            
        replace_file("makefile", choice)
        replace_file("main.py", choice)
    else:
        print
        print 'Invalid choice'
    
run()
