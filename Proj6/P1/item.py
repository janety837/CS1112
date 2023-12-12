# item.py

from interval import Interval
from shapes import draw_rect
import matplotlib.pyplot as plt


class Item:
    """
    An Item has an id_, a name, a weight, the number of arms required to lift 
    it, a location, the amount of time required to pick it up, and a time 
    window when pick-up is scheduled.
    """

    def __init__(self, id_, name, weight, arm_requirement, duration, loc=[1, 1]):
        """
        Initializes an Item object
        
        Parameters:
        -----------
        id_: The item's identifier, an int
        
        name: The item's name, a string
        
        weight: The item's weight, a float
        
        arm_requirement: Number of arms required to pick up the item, an int
        
        duration: Time units necessary to fully pick up the item, an int
        
        loc: Location of the item, a list of length 2 (x coordinate followed
             by a y coordinate).  Default: [1, 1].
        """
        self.loc = loc
        self.id_ = id_
        self.name = name
        self.weight = weight
        self.arm_requirement = arm_requirement
        self.duration = duration
        self.picked_window = None

    def valid_pickup(self, payload, num_arms):
        """
        Returns True if a robot with a max picking capability of `payload` and 
        `num_arms` number of arms is able to pick up the item; returns False
        otherwise.        
        
        Parameters:
            payload: (int, non-negative) the maximum weight that the picking robot can pick up
            num_arms: (int, non-negative) the number of arms of the picking robot
        """

        if payload >= self.weight and num_arms >= self.arm_requirement:
            return True
        else:
            return False

    def update_pickup_status(self, pickup_time):
        """
        Updates attribute `picked_window` to be an Interval indicating the time
        window that the item is scheduled to be picked.
        
        Parameter pickup_time: (int, non-negative) the time at which the robot reaches the 
            item's location and begins to pick it up
            
        The end point of `picked_window` should be `pickup_time` plus the 
        duration required to pick up the item.
            
        Returns None
        """

        self.picked_window = Interval(pickup_time,
                                      pickup_time + self.duration)

    def draw(self, t):
        """
        Draws a red square of side length 1 centered over the item's location 
        at timestep `t` if and only if the item is not yet fully picked up at 
        time `t`.  (An item is fully picked up at the end of its 
        `picked_window` and so should not be drawn at that time value.)
        
        Assumes figure window is already open.
        
        Parameter t: (int, non-negative) the time 
        """

        if self.picked_window is None or t < self.picked_window.right:
            side = 1
            draw_rect(self.loc[0] - side / 2, self.loc[1] - side / 2, side, side, 'r')
            plt.text(self.loc[0], self.loc[1], str(self.id_),
                     horizontalalignment='center')
