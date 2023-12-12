"""
How big is your heart?

Approximates the area between a smaller heart and a larger heart by throwing
darts onto a dartboard. Displays a plot and the approximated area
"""
from random import uniform
import matplotlib.pyplot as plt 

n=10000 #n darts are to be thrown
r=2.5 #the x and y coordinates of the darts can range from -r to r
s1=3 #size of bigger heart
s2=1 #size of smaller heart
# Set up the graph
plt.figure()            # creates new plot
ax= plt.gca()           # gets current axes
ax.set_aspect('equal')  # unit lengths on x- and y-axis are equal (equal scaling)
plt.axis((-r, r, -r, r)) # x and y axes both range from -r to r

# Simulate dart throwing
hits= 0   # no. of darts in between the two hearts so far
for k in range(n):
    # Throw dart
    x= uniform(-r, r)
    y= uniform(-r, r)
    if (x**2+y**2-s1)**3<=x**2*y**3:
        #dart is inside the bigger heart
        if (x**2+y**2-s2)**3<=x**2*y**3:
            #dart is in the smaller heart
            plt.plot(x, y, 'g+')
        else:
            #dart is in between the two hearts
            hits=hits+1
            plt.plot(x, y, 'r+')
    else:
        #dart is outside both hearts
        plt.plot(x, y, 'c+')
area=hits/n*(2*r)**2 #area approximation formula
plt.title(f'Outer heart (red part) has area {area:.2f} units squared')
plt.show()
