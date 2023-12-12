"""
Plots the trajectory of a rocket,
depending on its exhaust velocity or burn time
"""
import math
import matplotlib.pyplot as plt
def approx_flight (mR, q, b, u):
    """
    Return the tracjectory (time and altitude) of a rocket

    Parameters
        mR: (float or int) mass of rocket without fuel, in slugs
        q: (float or int) burn rate of fuel, in slugs/s
        b: (float or int) burn time, seconds
        u: (float or int) exhaust velocity, ft/s

    Returns as a tuple
        t: a list or array of numbers of at least 200 time values in seconds,
            from 0 to tf, where tf is the flight time (from takeoff to landing)
        h: a list or array of altitude values in feet,
           corresponding to the list (or array) of time values.
    """
    g=32.2 #given value of g
    #given formulas
    m_0=mR+q*b
    h_b=u/q*(m_0-q*b)*math.log(m_0-q*b)+u*(math.log(m_0)+1)*b-g*(b**2)/2\
        -u*m_0/q*math.log(m_0)
    v_b=u*math.log(m_0/(m_0-q*b))-g*b
    h_p=h_b+v_b**2/(2*g)
    t_p=b+v_b/g
    tf=t_p+math.sqrt(2*h_p/g)
    #initializes the arrays that contain values of time
    #and the corresponding heights
    t=[]
    h=[]
    time=0 #first value of time that will be used to calculate rocket height
    while time<tf:
        t.append(time) #adds value of time to the array t
        #the formula used for calculating height
        #depends on whether the rocket has run out of fuel
        if time<=b:
            Height=u/q*(m_0-q*time)*math.log(m_0-q*time)\
                +u*(math.log(m_0)+1)*time-g*(time**2)/2-u*m_0/q*math.log(m_0)
        else:
            Height=h_b+v_b*(time-b)-g*((time-b)**2)/2
        h.append(Height) #adds value of Height to the array t
        time=time+tf/200 #increments time to the next value used
                         #to calculate rocket height
    Height=0
    #adds final data point to the t and h arrays
    t.append(tf)
    h.append(Height)
    return t,h
def plot_test_u(u):
    """
    plots height of rocket vs time using different exhaust velocities
    
    u: (float or int) exhaust velocity, ft/s
    
    returns None
    """
    (t,h)=approx_flight(100,1,80,u)
    legend_text=f'u={u} ft/s'
    plt.plot(t,h,label=legend_text)
    return None
#Create and plot first graph (sensitivty to changes in exhaust velocity)
plt.figure(1)
#plots graphs using different exhaust velocities
plot_test_u(6000)
plot_test_u(7000)
plot_test_u(8000)
plot_test_u(8500)
plt.grid()
plt.legend()
plt.title('Rocket Height vs Time Based on Exhaust Velocity')
plt.show()
def plot_test_b(b):
    """
    plots height of rocket vs time using different burn times
    
    b: (float or int) bur time, s
    
    returns None
    """
    (t,h)=approx_flight(100,1,b,8000)
    legend_text=f'b={b} s'
    plt.plot(t,h,label=legend_text)
    return None
#Create and plot second graph (sensitivty to changes in burn time)
plt.figure(2)
for burn in range (60,101,8): #plots graphs using different burn times
    plot_test_b(burn)
plt.grid()
plt.legend()
plt.title('Rocket Height vs Time Based on Burn Time')
plt.show()
