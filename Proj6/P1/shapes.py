"""
Functions to draw rectangle, disk, star

The shape is added to the current plot if a figure window is active.  Otherwise
a new figure window will open.
"""


import matplotlib.pyplot as plt 
import numpy as np


def draw_rect(a, b, w, h, c):
    """
    Adds a rectangle to the plot.

    The rectangle has vertices (a,b), (a+w,b), (a+w,b+h), and (a,b+h) 
    and color c where c is one of 'r', 'g', 'y', etc.

    Parameters:
        a (float): The x-coordinate of the lower left corner of the rectangle
        b (float): The y-coordinate of the lower left corner of the rectangle
        w (float): The width of the rectangle
        h (float): The height of the rectangle
        c (str): The color of the rectangle
    """
    x= [a, a+w, a+w, a]
    y= [b, b, b+h, b+h]
    plt.fill(x, y, color=c)
    
    
def draw_disk(xc, yc, r, c):
    """
    Adds a circular disk to the plot.

    The disk has radius r, center (xc,yc), and 
    color c where c is one of 'r', 'g', 'y', etc.

    Parameters:
        xc (float): The x-coordinate of the center of the disk
        yc (float): The y-coordinate of the center of the disk
        r (float): The radius of the disk
        c (str): The color of the disk
    """
    theta= np.linspace(0, 2*np.pi, 100)
    cosines= np.cos(theta)
    sines= np.sin(theta)
    plt.fill(xc + r*cosines, yc + r*sines, color=c)
    
    
def draw_star(xc, yc, r, c):
    """
    Adds a 5-pointed star to the plot.

    The star has radius r, center (xc,yc), and color c where c is one of 'r', 
    'g', 'y', etc. Center is the center of the disk on which the 5 points of  
    the stars lie. Radius is the distance from center to any of the 5 points.

    Parameters:
        xc (float): The x-coordinate of the center of the star
        yc (float): The y-coordinate of the center of the star
        r (float): The radius of the star
        c (str): The color of the star
    """
    n= 5  # number of points of the star
    ri= r/(2*(1+np.sin(np.pi/(n*2))))  # radius of the inner 5 vertices
    x= np.zeros(n*2)
    y= np.zeros(n*2)
    for k in range(n*2):
        theta= (2*k-1)*np.pi/(n*2)
        if k%2 == 1:
            x[k]= xc + r*np.cos(theta)
            y[k]= yc + r*np.sin(theta)
        else:
            x[k]= xc + ri*np.cos(theta)
            y[k]= yc + ri*np.sin(theta)     
    plt.fill(x, y, color=c)
           
    
    


    
    
