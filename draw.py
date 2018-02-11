from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
     #swaps to draw in one direction (left to right)
     if (x0 > x1):
          #print "swapped"
          draw_line( x1, y1, x0, y0, screen, color)
     #plotting is done
     if(x0 == x1 and y0 == y1):
          #print "done"
          return
     #plotting based on octets
     else:
          dx = x1 - x0
          dy = y1 - y0
          
          #print "dx %d"%dx
          #print "dy %d"%dy
          
          #determine the quadrant

          #1
          if(0 <= dy and dy <= dx):
               #print 1
               A = dy
               B = -dx
               d = (2 * A) + B
               x = x0
               y = y0
               while x<=x1:
                    plot(screen, color, x, y)
                    #print "x: %d, y: %d"%(x,y)
                    if(d > 0):
                         y+=1
                         d+= (2 * B)
                    x+=1
                    d+= (2 * A)
               #draw_line( A, B, x0, y0, screen, color)
               return
          #2
          if(dx < dy):
               #print 2
               A = dy
               B = -dx
               d = A + (2 * B)
               x = x0
               y = y0
               while y<=y1:
                    plot(screen, color, x, y)
                    if(d < 0):
                         x+=1
                         d+= (2 * A)
                    y+=1
                    d+= (2 * B)
               #draw_line( A, B, x0, y0, screen, color)
               return
          #7
          if(dy <= -dx):
               #print 7
               A = dy
               B = -dx
               d = A + (2 * B)
               x = x0
               y = y0
               while y>=y1:
                    plot(screen, color, x, y)
                    if(d < 0):
                         x+=1
                         d-= (2 * A)
                    y-=1
                    d+= (2 * B)
               #draw_line( A, B, x0, y0, screen, color)
               return
          #8
          if(-dx < dy and dy < 0):
               #print 8
               A = dy
               B = -dx
               d = (2 * A) + B
               x = x0
               y = y0
               while x<=x1:
                    plot(screen, color, x, y)
                    if(d > 0):
                         y-=1
                         d+= (2 * B)
                    x+=1
                    d-= (2 * A)
               #draw_line( A, B, x0, y0, screen, color)
               return


