# main6.py
#
# For dynamic graphics, first use this command in the Spyder Python Console:
#     %matplotlib qt
"""
Module for Project 6 Robot Task Allocation, with Subclasses of Robot
"""

from robot import Robot, FastRobot, LimbedRobot
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
        robots = []  # list of robots
        items = []  # list of items
        for line in fid:
            # split `line` into a list of strings, with comma as separator
            tokens = line.strip().split(',')

            if tokens[0][0] == 'I':
                id_ = int(tokens[1])
                name = tokens[2].strip()
                weight = float(tokens[3])
                arms_required = float(tokens[4])
                x_loc = int(tokens[5].strip()[1:])
                y_loc = int(tokens[6].strip()[0:-1])
                loc = [x_loc, y_loc]
                duration = int(tokens[7].strip())
                items.append(Item(id_, name, weight, arms_required,
                                  duration, loc))
            elif tokens[0][0] == 'R':
                id_ = int(tokens[1])
                max_weight = float(tokens[2])
                x_loc = int(tokens[3].strip()[1:])
                y_loc = int(tokens[4].strip()[0:-1])
                loc = [x_loc, y_loc]
                robots.append(Robot(id_, max_weight, loc, sim_time))
            elif tokens[0][0] == 'F':
                id_ = int(tokens[1])
                max_weight = float(tokens[2])
                x_loc = int(tokens[3].strip()[1:])
                y_loc = int(tokens[4].strip()[0:-1])
                loc = [x_loc, y_loc]
                speed_multiplier = float(tokens[5])
                robots.append(FastRobot(id_, max_weight, loc, sim_time,
                                        speed_multiplier))
            elif tokens[0][0] == 'L':
                id_ = int(tokens[1])
                max_weight = float(tokens[2])
                x_loc = int(tokens[3].strip()[1:])
                y_loc = int(tokens[4].strip()[0:-1])
                loc = [x_loc, y_loc]
                slow_multiplier = float(tokens[5])
                max_payload = int(tokens[6])
                num_arms = int(tokens[7])
                robots.append(LimbedRobot(id_, max_weight, loc, sim_time,
                                         num_arms, slow_multiplier, max_payload))


    # Do a task allocation
    #allocated_robots, items_remaining = simple_allocation(robots, items)
    allocated_robots, items_remaining = create_allocation(robots, items)

    # Animate the simulation
    animate(robots, items, sim_time, room_size)

    # Print descriptive output
    output_results(robots)


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

    allocated_robots = []
    items_remaining = []

    for item in items:
        for robot in robots:
            if robot.pick(item):
                allocated_robots.append(robot)
        if item.picked_window is None:
            items_remaining.append(item)

    return allocated_robots, items_remaining


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

    for t in range(1, sim_time + 1):
        plt.clf()  # clear figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis([0, room_size[0] + 1, 0, room_size[1] + 1])
        plt.autoscale(False)
        plt.title(f"Time = {t}")
        for item in items:
            item.draw(t)
        for robot in robots:
            _, t_robot = robot.where_am_i()
            robot.draw(min(t, t_robot - 1))  # So keeps drawing Robot at final location
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
    print("-------------------------------")
    for robot in robots:
        picked = robot.get_items_picked()
        t = robot.where_am_i()[1]
        print(f"Robot {robot.get_id()} picked {len(picked)} items in {t} timesteps")
        for item in picked:
            print(f"  {item.name} (ID {item.id_}): Assigned at time",
                  f"{item.picked_window.left}, picked up at time {item.picked_window.right}")
    print("-------------------------------")


def create_allocation(robots, items):
    """
    Allocate item pickups to robots. All items need to be picked only by
    robots that have the correct physical capabilities. Robots must move
    according to their physical limitations. All pickups included must only be
    within the total time.

    Parameters
        ----------
        robots : list
            non-empty list of unique `Robot` references
        items : list
            non-empty list of unique `Item` references

    Algorithm:  For each item, look through the robots to find the robot that
    minimizes the objective 
    
        0.8*time_needed + 0.2*time_ratio

    and make it perform the pick.  time_needed is the total time the robot 
    needs to pick an item (steps to get there and picking it up).  time_ratio 
    is the time_needed divided by the time the robot has left in its run before
    travelling to perform the pick.

    Returns
    -------
    lisR : list
        list of the `Robot`s that picked up `Item`s
    lisI : list
        list of remaining `Item`s that didn't get picked up
    """
    a = 0.8  # weight for the time_needed objective
    b = 0.2  # weight for the time_ratio objective
    # TODO: Add your code below
    #initializes lists to be returned
    lisR=[]
    lisI=[]
    for i in items:
        available_robots=[] #intializes list of robots that are physically
                            #capable of picking up the item
        for r in robots:
            #calling pick with do_pick parameter set to False allows the
            #function to return whether or not the robot can pick up the item
            #without actually having the robot pick it up. If the robot can
            #pick the item up, it's added to available_robots
            if r.pick(i,False)==True:
                available_robots.append(r)
        #if available_robots is empty, that means the item cannot be picked up,
        #so it's added to lisI
        if available_robots==[]:
            lisI.append(i)
        #if available_robots is not empty, at least one robot can pick up the item
        else:
            #the following code goes through each robot in available_robots
            #to see which one will result in the smallest value of w1h1+w2h2,
            #which is stored in min_opt_val. before the loop, min_opt_val is set
            #to the w1h1+w2h2 of the first robot in available_robots
            time_needed=len(available_robots[0].steps_to_arrival(i.loc))-1+i.duration
            time_so_far = len(available_robots[0].get_locations())
            time_remaining = available_robots[0].get_total_time() - time_so_far
            time_ratio=time_needed/time_remaining
            min_opt_val=a*time_needed+b*time_ratio
            best_index=0 #the index of the robot in available_robots
                         #corresponding to the current value of min_opt_val
            for j in range(1,len(available_robots)):
                r=available_robots[j]
                time_needed=len(r.steps_to_arrival(i.loc))-1+i.duration
                time_so_far = len(r.get_locations())
                time_remaining = r.get_total_time() - time_so_far
                time_ratio=time_needed/time_remaining
                opt_val=a*time_needed+b*time_ratio
                if opt_val<min_opt_val:
                     min_opt_val=opt_val
                     best_index=j
            available_robots[best_index].pick(i) #executes pick function using the
                                                 #robot with the lowest
                                                 #w1h1+w2h2 value
            #if the robot used is not in lisR, it's added
            if available_robots[best_index] not in lisR:
                lisR.append(robots[best_index])
    return lisR, lisI
        
            


if __name__ == '__main__':
    #run_robots("room2.txt")
    run_robots("room3.txt")

