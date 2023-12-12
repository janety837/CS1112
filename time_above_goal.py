"""
How much time does it spend above a certain height

determines how much time a rocket spends above a user-entered height\
    for various possible burn times
"""
import math
import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
#given constants
m_R=100
q=1
u=8000
g=32.2
#prompts user to enter a height until a positive value is entered
h=float(input('Enter a height for the rocket in ft: '))
while h<=0:
    h=float(input('Height must be positive. Enter another value: '))
max_b=100 #max value of b given in prompt
for b in range(1, max_b+1,2): #loops through burn times starting from 1 to 101
                              #with a step size of 2 seconds
    m_0=m_R+q*b #calculates rocket's initial mass, including fuel,
                #based on value of b and the given formula
    v_b=u*math.log(m_0/(m_0-q*b))-g*b #rocket's velocity
                                      #when it runs out of fuel, based on b
    h_b=u/q*(m_0-q*b)*math.log(m_0-q*b)+u*(math.log(m_0)+1)*b-g*(b**2)/2\
        -u*m_0/q*math.log(m_0) #rocket's height when it runs out of fuel,
                               #depending on value of b
    h_p=h_b+v_b**2/(2*g) #rocket's peak height depending on b
    #if the rocket never reaches the user-entered height h
    #or h is the peak height, the rocket is above h for 0 seconds
    if h_p<=h:
        duration=0
    else:
        t_initial=0
        h_t=0
        #if the rocket does go over h,
        #calculates height at increasing values of time t_initial
        #until h is reached
        while h_t<h:
            t_initial=t_initial+0.1
            if t_initial<b:
                h_t=u/q*(m_0-q*t_initial)*math.log(m_0-q*t_initial)\
                    +u*(math.log(m_0)+1)*t_initial-g*(t_initial**2)/2\
                    -u*m_0/q*math.log(m_0)
            else: #once the rocket runs out of fuel,
                  #a different formula must be used to calculate height
                h_t=h_b+v_b*(t_initial-b)-g*((t_initial-b)**2)/2
        t_final=t_initial
        #calculates height at increasing values of time t_final
        #until height h is reached again on the way down
        while h_t>h:
            t_final=t_final+0.1
            if t_final<b:
                h_t=u/q*(m_0-q*t_final)*math.log(m_0-q*t_final)\
                    +u*(math.log(m_0)+1)*t_final-g*(t_final**2)/2\
                    -u*m_0/q*math.log(m_0)
            else:
                h_t=h_b+v_b*(t_final-b)-g*((t_final-b)**2)/2
        duration=t_final-t_initial #the time the rocket is above h is
                                   #the time between the rocket reaches h
                                   #on the way up and on the way down
    plt.plot(b, duration, 'b*')
plt.xlabel('Burn Time (seconds)')
plt.ylabel('Duration (seconds)')
plt.title(f'Duration above {h:.1f} feet')
plt.show()