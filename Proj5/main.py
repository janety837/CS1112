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
            
            if tokens[0]=='Robot': #this means the line gives data for a robot
                #remove the brackets from the strings obtained from the file
                #and obtain integers from the results
                x_loc_str=tokens[3].strip(" [")
                y_loc_str=tokens[4].strip(" ]")
                x_loc_int=int(x_loc_str)
                y_loc_int=int(y_loc_str)
                robots.append(Robot(int(tokens[1]),float(tokens[2]),\
                [x_loc_int,y_loc_int],sim_time)) #appends a new instance of
                                                 #Robot to list robots
            else: #this means the line gives data for an item
                #remove the brackets from the strings obtained from the file
                #and obtain integers from the results
                x_loc_str=tokens[5].strip(" [")
                y_loc_str=tokens[6].strip(" ]")
                x_loc_int=int(x_loc_str)
                y_loc_int=int(y_loc_str)
                items.append(Item(int(tokens[1]), tokens[2], float(tokens[3]),\
                int(tokens[4]),int(tokens[7]),[x_loc_int,y_loc_int])) #appends
                                                                      #a new
                                                                      #instance
                                                                      #of Robot
                                                                      #to list
                                                                      #robots
            
                
        ##############################################################
        # End of TASK 1
        ##############################################################
   
    # Do a task allocation
    allocated_robots, items_remaining = simple_allocation(robots, items)

    # Animate the simulation
    animate(robots, items, sim_time, room_size)
"""
    # Print descriptive output
    output_results(robots)

    # OPTIONAL TODO: check for collisions
    #   Uncomment the check_collisions call below if you have implemented
    #   this OPTIONAL function
    #
    # collisions = check_collisions(allocated_robots)
    
"""

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
    #initiate lisR and lisI
    lisR=[]
    lisI=[]
    for i in items:
        for r in robots:
            r.pick(i) #assigns item to a robot using pick method
        if i.picked_window==None: #the item did not get picked up
            lisI.append(i)
    for r in robots:
        if r.get_items_picked()!=[]: #the robot's list of items picked isn't empty,
                                #meaning it's picked up at least one item
            lisR.append(r)
    return (lisR,lisI)
    


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
        #animates each item
        for i in items:
            i.draw(t)
        for r in robots:
            locations=r.get_locations()
            #if t has not yet exceeded the length of the list of the robot's
            #locations, the draw method can be called without an error
            if t<=len(locations):
                r.draw(t)
            #if t has exceeded the  length of the list of the robot's
            #locations, the draw method will result in an error,
            #so we will just use the last item in the locations list for the
            #draw method
            else:
                r.draw(len(locations)-1)
        plt.pause(1)

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
    for r in robots:
        print (f"Robot {r.get_id()} picked {len(r.get_items_picked())} items in\
               {len(r.get_locations())} timesteps")
        for i in Robot._items_picked:
            print(f"     {i.name} (ID {i.id_}): Assigned at time \
            {i.picked_window.left}, picked up at time {i.picked_window.right}")


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
