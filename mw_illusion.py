# mw_illusion.py
"""
Module for drawing and displaying the Munker-White Illusion
"""
import shapes
import matplotlib.pyplot as plt
import numpy as np


def draw_illusion(n, w, cg, cs, f, a, b):
    """
    Display the Munker-White Illusion in the current figure window
    
    Parameters:
      n:  (int) number of grid rectangles, i.e., the long rectangles that span 
          the width of the diagram.  An int greater than 1.
      w:  (float or int) width of grid rectangles
      cg: (string) color of grid rectangles.  A predefined color name such as 
          'k', 'b', ..., etc.
      cs: (string) color of the two stacks of narrow rectangles. A predefined 
          color name such as 'k', 'b', ..., etc. 
      f:  (float) a fraction greater than 0 and less than 0.5.  The horizontal 
          width of the narrow rectangles is f*w. 
      a:  (float) the x-coordinate of the lower left corner of the diagram
      b:  (float) the y-coordinate of the lower left corner of the diagram

    The height of each rectangle is one. There are n-1 narrow rectangles in 
    each stack, and the two stacks are horizontally centered in the diagram, 
    with the same amount of space left of the left stack, between the stacks, 
    and right of the right stack.
    Check parameter f:  if f>=.5, set f to .3
    
    Returns None
    """
    if f>=0.5:
        f=0.3
    for i in range (n-1):    
        shapes.draw_rect(a,b+2*i,2*(w-2*f*w)/3+f*w,1,cg)
        shapes.draw_rect(a+2*(w-2*f*w)/3+2*f*w,b+2*i,(w-2*f*w)/3,1,cg)
        shapes.draw_rect(a+(w-2*f*w)/3,i*2+b+1,f*w,1,cs)
        shapes.draw_rect(a+2*(w-2*f*w)/3+f*w,b+2*i,f*w,1,cs)
    shapes.draw_rect(a,b+2*(n-1),w,1,cg)
    return None
#----
# Demonstration: draw three different Munker-White Illusions where the left 
# two are strong and the right one is weak.  All three diagrams are drawn on 
# one set of axes.  (Do not use subplots.)
#----
plt.close()
plt.figure(figsize=[9,3])  # Change figure size (default is [6.4, 4.8])
plt.axis('equal')

# TO-DO: complete the code below to draw the three illusions
# Example 1 Strong illusion
a=0; b=0  # coordinates of lower left corner of first illusion to draw
draw_illusion(8,15,'c',0.9*np.array([0,1,0]),0.3,a,b)
# Example 2 Strong illusion
a=20;b=0  # coordinates of lower left corner of second illusion to draw
draw_illusion(8,15,'k',0.9*np.array([0,1,0]),0.1,a,b)
# Example 3 Weak illusion
a=40;b=0  # coordinates of lower left corner of third illusion to draw
draw_illusion(8,15,0.95*np.array([0,1,0]),0.9*np.array([0,1,0]),0.45,a,b)
plt.show()


