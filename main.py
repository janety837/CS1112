# main.py
"""
Module for Project 5 Robot Task Allocation

To to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).
"""

from robot import Robot
from item import Item
import numpy as np
import matplotlib.pyplot as plt


def run_robots(data_filename):
    """
    Create an allocation of robots to pickup items given a data file in the
    necessary format.
    :param data_filename:
    """
    with open(data_filename, 'r') as fid:
        # Process the first line of the file
        line = fid.readline()  
        sim_info = line.strip().split(',')
        sim_time = int(sim_info[0])
        horiz_dim = float(sim_info[1])
        vert_dim = float(sim_info[2])
        room_size = np.array([horiz_dim, vert_dim])

        # Process the remaining lines of the file
        
        ##############################################################
        # TODO
        # TASK 1: Modify the code below to create a list of Robots and
        #         a list of Items.
        ##############################################################
        robots = []  # list of robots
        items = []   # list of items
        for line in fid:
            # split `line` into a list of strings, with comma as separator   
            tokens = line.strip().split(',')
            
            
                
        ##############################################################
        # End of TASK 1
        ##############################################################
       
    # Do a task allocation
    allocated_robots, items_remaining = simple_allocation(robots, items)

    # Animate the simulation
    animate(robots, items, sim_time, room_size)

    # Print descriptive output
    output_results(robots)

    # OPTIONAL TODO: check for collisions
    #   Uncomment the check_collisions call below if you have implemented
    #   this OPTIONAL function
    #
    # collisions = check_collisions(allocated_robots)
    


def simple_allocation(robots, items):
    """
    Given a list of items and a list of robots, allocate item pickups to the robots.
        
    Parameters
    ----------
    robots : list
        non-empty list of unique `Robot` references
    items : list
        non-empty list of unique `Item` references

    Algorithm: for each `Item` in `items`, look for the first `Robot` in 
        `robots` that is capable of picking it up to pick it up.

    Returns
    -------
    lisR : list
        list of the `Robot`s that picked up `Item`s
    lisI : list
        list of remaining `Item`s that didn't get picked up
    """
    # TODO TASK 2: implement this function
    pass
    


def animate(robots, items, sim_time, room_size):
    """
    Animate the robots and items in space for `sim_time` timesteps.  At each
    time step, call the `draw` method for each `Item` and for each `Robot`. 
    
    Assume that the bottom left corner is at (0,0) for room_size

    Parameters
    ----------
    robots : list
        list of `Robot` references
    items : list
        list of `Item` references
    sim_time : int
        number of timesteps
    roomsize : list
        length 2 list that represents the dimensions of the room
    """
    plt.close('all')
    plt.figure()
    plt.pause(1)

    for t in range(1, sim_time+1):
        plt.clf()  # clear figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis([0, room_size[0] + 1, 0, room_size[1] + 1])
        plt.autoscale(False)
        plt.title(f"Time = {t}")
        ############################################
        # TODO: Add your code here for the animation 
        ############################################



def output_results(robots):
    """
    Prints the results of task allocation. Show the stats and tasks for each 
    `Robot` in `robots`:
        - Print the number of `Item`s picked and the total timesteps taken
        - Print out each `Item` picked and the time period taken to navigate 
          to the object and pick it.
    See the print format in the project description.
    
    Parameter robots: (list) Each element is a `Robot` in the simulation.

    """
    # TODO Task 3: implement this method
    pass



def check_collisions(allocated_robots):
    """
    Check for and report on collisions.
    
    OPTIONAL TO DO: write the specifications for this function

    Parameter allocated_robots: (list) Each element is a `Robot` that has been
        allocated at least one task

    """
    # OPTIONAL TO DO: implement this function
    pass






if __name__ == '__main__':
    run_robots("room1.txt")
