# game_of_life.py
"""
CS1112 Project 4 Game of Life

Refer to the Project 4 description for details and other helpful information.

To to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).

"""
import numpy as np
import matplotlib.pyplot as plt
import random


def create_world(nr, nc, data_mode):
    """
    Returns an nr-by-nc array of ints representing the game of life world
    
    Parameters
    ----------
    nr : the number of rows in the world.  An int > 5.
    
    nc : the number of columns in the world.  An int > 5.
    
    data_mode : (string) can be one of two kinds:
        
    - The string "random".  Then the initial state is to be randomly generated.
      The element at [i,j] is 1 with probability 1/(abs(i-j)+2); otherwise 0.
        
    - The string name of a plain text file storing the initial state.  If the
      world read from the file is bigger than nr-by-nc, use only the rows and
      columns of data that fit on the nr-by-nc array to be returned
    """
    if data_mode=='random':
        w=np.zeros((nr,nc)) #creates an array of zeros that will be modified
        for i in range(nr):
            for j in range(nc):
                #determines whether cell is alive (1) or dead (0) based on probability
                random_float=random.random()
                if random_float<=1/(abs(i-j)+2):
                    w[i,j]=1
    else:
        w_0=np.loadtxt(data_mode, 'int', '#')
        w=w_0[0:nr,0:nc] #creates a subarray of w_0 that shows only the first
                         #nr rows and nr columns w_0
    return w
    


def one_generation_later(w, add_rule):
    """
    Returns a new array representing the world matrix w after ONE generation
    according to the rules of the game of life

    Parameters
    ----------
    w : the world matrix, a 2-d array.
    
    add_rule: (bool) If True, apply extra-life-rule; 
              otherwise do not apply extra-life-rule.
    """
    (numrows,numcols)=np.shape(w)
    new_w=np.zeros((numrows,numcols)) #creates a new array of zeros that will
                                      #be modified
    for i in range(numrows):
        for j in range(numcols):
            count=0
            if i==0:
                if j==0:
                    if w[i][j+1]==1:
                        count+=1
                    if w[i+1][j]==1:
                        count+=1
                    if w[i+1][j+1]==1:
                        count+=1
                elif j==numcols-1:
                    if w[i][j-1]==1:
                        count+=1
                    if w[i+1][j-1]==1:
                        count+=1
                    if w[i+1][j]==1:
                        count+=1
                else:
                    if w[i][j-1]==1:
                        count+=1
                    if w[i][j+1]==1:
                        count+=1
                    if w[i+1][j-1]==1:
                        count+=1
                    if w[i+1][j]==1:
                        count+=1
                    if w[i+1][j+1]==1:
                        count+=1
            elif i==numrows-1:
                if j==0:
                    if w[i-1][j]==1:
                        count+=1
                    if w[i-1][j+1]==1:
                        count+=1
                    if w[i][j+1]==1:
                        count+=1
                elif j==numcols-1:
                    if w[i-1][j]==1:
                        count+=1
                    if w[i-1][j-1]==1:
                        count+=1
                    if w[i][j-1]==1:
                        count+=1
                else:
                    if w[i][j-1]==1:
                        count+=1
                    if w[i][j+1]==1:
                        count+=1
                    if w[i-1][j-1]==1:
                        count+=1
                    if w[i-1][j]==1:
                        count+=1
                    if w[i-1][j+1]==1:
                        count+=1
            else:
                if j==0:
                    if w[i-1][j]==1:
                        count+=1
                    if w[i-1][j+1]==1:
                        count+=1
                    if w[i][j+1]==1:
                        count+=1
                    if w[i+1][j]==1:
                        count+=1
                    if w[i+1][j+1]==1:
                        count+=1
                elif j==numcols-1:
                    if w[i-1][j]==1:
                        count+=1
                    if w[i-1][j-1]==1:
                        count+=1
                    if w[i][j-1]==1:
                        count+=1
                    if w[i+1][j-1]==1:
                        count+=1
                    if w[i+1][j]==1:
                        count+=1
                else:
                    if w[i-1][j-1]==1:
                        count+=1
                    if w[i-1][j]==1:
                        count+=1
                    if w[i-1][j+1]==1:
                        count+=1
                    if w[i][j-1]==1:
                        count+=1
                    if w[i][j+1]==1:
                        count+=1
                    if w[i+1][j-1]==1:
                        count+=1
                    if w[i+1][j]==1:
                        count+=1
                    if w[i+1][j+1]==1:
                        count+=1
            if count<2:
                new_w[i,j]=0
            elif count==2:
                new_w[i,j]=w[i,j]
            elif count==3:
                new_w[i,j]=1
            else:
                if add_rule==True:
                    if w[i,j]==0:
                        random_float=random.random()
                        if random_float<=0.4:
                            new_w[i,j]=1
                        else:
                            new_w[i,j]=0
                    else:
                        new_w[i,j]=0
                else:
                    new_w[i,j]=0
    return new_w

def simulate(n, nr, nc, data_mode, add_rule, blink):
    """
    Returns the world matrix after simulating n generations of the game of life
    
    Parameters
    ----------
    n : the number of generations (steps), a non-negative int
    
    nr : the number of rows in the world.  An int > 5.
    
    nc : the number of columns in the world.  An int > 5.
    
    data_mode : (string) can be one of two things:
        
     - The string "random". Then the initial state is to be randomly generated.
     The element at [i,j] is 1 with probability 1/(abs(i-j)+2); otherwise 0.
        
     - The string name of a plain text file storing the initial state.  If the
        world read from the file is bigger than nr-by-nc, use only the rows and
        columns of data that fit on the nr-by-nc array to returned
    
    add_rule: (bool) If True, apply extra-life-rule; 
              otherwise do not apply extra-life-rule.
              
    blink : a positive float.  blink > 1 means no animation
            blink <= 1 is the blink rate of the animation, i.e., the pause time
            in seconds between generations 
    """
    world=create_world(nr,nc,data_mode)
    #animation for original grid
    plt.close()
    fig, ax=plt.subplots()
    ax.matshow(world)
    ax.set_title('Generation 0')
    plt.pause(blink)
    #print(world)
    for i in range(n):
        world=one_generation_later(world, add_rule)
        animate(ax, i+1, world, blink)
        #print(world)
        
    
#### TO-DO: Specify and implement at least one helper function here
def animate(axes, generation, w, time):
    """
    Returns None
    
    Parameters
    ----------
    axes: axes reference
    generation: how many times generations have been generated
    w: the world matrix
    time: blink
    """

    axes.clear()
    axes.matshow(w)
    axes.set_title(f'Generation {generation}')
    plt.pause(time)



#### Script code
if __name__ == "__main__":
    # This is a convenient place to write code to test your functions 
    # individually as you develop your program!!

    # TO-DO: Add more code here and execute the script for testing
    
    nr= 5
    nc= 8
    add_rule=True
    generations=2
    value_source="seeds_p48.txt"
    blink=0.5
    world= simulate(generations, nr, nc, value_source, add_rule, blink)
