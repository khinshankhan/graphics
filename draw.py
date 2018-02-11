from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #swaps to draw in one direction (left to right)
     if (x0 > x1):
         draw_line( x1, y1, x0, y0, screen, color)
         return
     if(x0 == x1 or y0 == y1):
         print done
         return
    # changes
     else:
         dx = x1 - x0
         dy = y1 - y0

         print "dx %d"%dx
         print "dy %d"%dy
        
         #determine the quadrant
        
         #1
         if(0 < dy and dy < dx):
             A = dy
             B = -dx
             d = (2 * A) + B
             x = x0
             y = y0
             while x<=x1:
                 plot(screen, color, x, y)
                 print "x: %d, y: %d"%(x,y)
                 if(d > 0):
                     y+=1
                     d+= (2 * B)
                 x+=1
                 d+= (2 * A)
             #print "dx %d"%dx
             #print "dy %d"%dy
             draw_line( A, B, x0, y0, screen, color)

         #2
         if(dx < dy):
             A = dy
             B = -dx
             d = A + (2 * B)
             x = x0
             y = y0
             while x<=x1:
                 plot(screen, color, x, y)
                 print "x: %d, y: %d"%(x,y)
                 if(d < 0):
                     x+=1
                     d+= (2 * A)
                 y+=1
                 d+= (2 * B)
             pass

         #7
         if(dy < -dx):
             print 7
             pass

         #8
         if(-dx < dy and dy < 0):
             print 8
             pass
