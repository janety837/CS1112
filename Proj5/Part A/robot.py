# robot.py
from interval import Interval
from shapes import draw_disk
import matplotlib.pyplot as plt
import copy


class Robot:
    """
    A robot has an id_, a maximum weight it can pick up, a list of periods
    when it is occupied with tasks it has been assigned, a list of locations
    at each time step, and a list of items picked. A robot moves in the
    cardinal directions only--north, east, south, west (NESW)--and moves
    one unit distance in each time step.

    Attributes
    ----------
    _id_ : int
        The robot's identifier
    _max_weight : number
        maximum weight that the robot can pick up at each pickup
    _total_time : int
        Maximum number of time steps the robot can be on (moving, picking)
    _occupied_periods : list
        Each element of the list is an `Interval` when the robot is occupied 
        with a task.  The list is initially empty.
        Example: if the robot is assigned a task from time 1 to time 3 and
        another task from time 4 to time 5, then the list should be
            [Interval(1,3), Interval(4,5)]
    _locations : list
        Each element of the list is the location of the robot at a time step.
        Initially the list has just the starting location of the robot,
        corresponding to time 1. The maximum eventual length of the list 
        is `_total_time`.  Each location is itself a list of two ints: the 
        x-coordinate followed by the y-coordinate.
        Example: if `Robot` at position (4,5) is allocated a task that 
        requires it to move east 2 units of distance, then three consecutive
        rows of `_locations` would be
            [[4,5], [5,5], [6,5]]
        indicating that `Robot` moves two units east over two time steps.
    _items_picked : list
        Each element of the list is an item that the robot has picked up.  The
        list is initially empty.
    """

    def __init__(self, id_, max_weight, starting_location, total_time):
        """
        Initializes a `Robot` object

        Parameters
        ----------
        id_ : int
            Robot's identifier.
        max_weight : number
            maximum weight that the robot is able to pick up
        starting_location : list
            a length 2 list of the initial location (x- and y-coord) of the robot
        total_time : int
            Maximum number of time steps the robot can be on, positive
        """
        self._id_=id_
        self._max_weight=max_weight
        self._total_time=total_time
        self._occupied_periods=[] #robot starts off with no tasks,
                                  #so no occupied periods
        self._occupied_periods_str=[] #bc _occupied_periods only prints the id
                                      #of the interval, creating a list of the
                                      #intervals as strings helps with testing
        self._locations=[starting_location] #first item in _locations
                                            #is robot's starting position
        self._items_picked=[] #robot starts off with no items picked up
        self._items_picked_names=[] #bc _items_picked only prints the id of
                                    #the item, creating a list of the item
                                    #names helps with testing
    
    def get_id(self):
        """
        Returns (int) the `_id_` of the robot
        """
        return self._id_


    def get_items_picked(self):
        """
        Returns a copy of the `_items_picked`.
        """
        return copy.deepcopy(self._items_picked)
    


    def get_locations(self):
        """
        Return a copy of the `_locations`
        """
        return copy.deepcopy(self._locations)
    


    def where_am_i(self):
        """
        Determine the most recent location of the `Robot` along with the time
        it corresponded to.  The most recent location is the last location in
        `_locations`.  

        Returns a tuple (lis, time) where
        -------
        lis : list
            a new list of length 2 that stores the most recent location (x-y
            coordinate)
        time : int
            time of most the recent location
        """
        lis=self._locations[-1] #most recent location is the last item
                                #in the list of locations
        time=len(self._locations) #an item is added to _locations
                                  #at every time step, so the number of items
                                  #corresponds to the current time
        return (lis,time)
    


    def steps_to_arrival(self, loc):
        """
        Returns a valid list of locations for each time step of a path that the 
        robot can take from its current location to reach the location `loc`. 
        The path needs not be optimal.  The first location of the list is the 
        robot's current location; the last location of the list is `loc`.
        
        This method considers the path only and does not consider whether 
        there is enough time to reach `loc`.  

        Parameters
        ----------
        loc : list
            a length 2 list storing the destination x-y coordinate
        """
        (starting_location,starting_time)=self.where_am_i()
        path=[starting_location] #first location in the path is the
                                 #current location
        current_location=copy.deepcopy(starting_location)
        while current_location[0]!=loc[0]: #I chose for the robot to walk
                                           #in the x-direction first
            new=copy.deepcopy(path)
            #x-value either increases or decreases depending on
            #which direction the robot needs to head in
            if current_location[0]<loc[0]:
                current_location[0]+=1
            else:
                current_location[0]-=1
            new.append(current_location)
            path=new
        while current_location[1]!=loc[1]: #after the robot has walked
                                           #far enough in the x-direction,
                                           #it needs to walk in the y-direction
            new=copy.deepcopy(path)
            if current_location[1]<loc[1]:
                current_location[1]+=1
            else:
                current_location[1]-=1
            new.append(current_location)
            path=new
        return path


    def pick(self, item, do_pick=True):
        """
        Returns True if the robot is able to pick up the item; returns False otherwise.
        
        Determines whether the robot should pick up `item`.  If so, executes 
        the pick if `do_pick` is True.
        
        The robot should pick up `item` when the following are true:
          1. the robot's physical characteristics allows it to pick up `item`,
          2. the robot can travel to `item` and fully pick it up in time, and
          3. `item` can be picked up (it is not already scheduled for pickup).
        
        If the pickup does occur,
          1. Update `item`'s picked_window
          2. Update `Robot`'s `_locations`, `occupied_periods`, and
               `_items_picked`. The `Interval` appended to `occupied_periods` 
               should include both the travel time and pickup duration.
        No attributes should be updated if the pickup does not occur.

        Parameters
        ----------
        item : Item
            The item to be picked up by the robot

        do_pick : Boolean
            Indicates if the robot should execute the pick should it be possible.
            Default is True.

        Returns
        -------
        Boolean
            Whether the pick is possible
        """
        time_to_item=len(self.steps_to_arrival(item.loc))-1 #amount of time
                                                            #robot will take to
                                                            #get to the item
                                                            #from its current
                                                            #position
        if item.valid_pickup(self._max_weight,0)==True and\
        time_to_item+item.duration<=self._total_time and\
        item.picked_window==None: #conditions listed above
            do_pick=True
        else:
            do_pick=False
        if do_pick==True:
            current_time=len(self._locations)
            item.update_pickup_status(current_time+time_to_item)
            new_path=self.steps_to_arrival(item.loc)
            self._locations.pop() #before the new path is added,
                                  #the current location needs to be removed
                                  #from _locations because it's also listed
                                  #in new_path, which would create a duplicate
            for x in new_path:
                self._locations.append(x)
            for i in range(item.duration):
                self._locations.append(item.loc)
            self._occupied_periods.append(Interval(current_time,\
            current_time+time_to_item+item.duration))
            self._occupied_periods_str.append(str(Interval(current_time,\
            current_time+time_to_item+item.duration))) #intervals added
                                                       #as strings so they're
                                                       #easy to see
                                                       #when testing
            self._items_picked.append(item)
            self._items_picked_names.append(item.name) #the names of the items are
                                                 #appended so that it's easy to
                                                 #see which items were
                                                 #picked up when testing
        return do_pick


    def draw(self, t):
        """
        Draw a blue circle of diameter 1 to represent the robot at time `t`.
        Label the circle at the center with its `_id_`.
        
        Assumes figure window is already open.
        
        Parameter t: (int) the time. t>=1 
        """
        draw_disk(self._locations[t-1][0],self._locations[t-1][1],0.5,'b')
        s=str(self._id_)
        plt.text(self._locations[t-1][0],self._locations[t-1][1],s,\
                horizontalalignment="center")
    

