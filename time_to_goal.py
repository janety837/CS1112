"""
Flight of a rocket

Calculates how long a rocket will take to reach a certain height based\
    on its burn time, the time it takes to consume all its fuel
"""
import math
#given constants
m_R=100
q=1
u=8000
g=32.2
#prompts user to enter a burn time until user enters a positive value
b=float(input('Enter burn time in seconds: '))
while b<=0:
    b=float(input('Burn time must be positive. Enter another value: '))
#prompts user to enter a height until user enters a positive value 
h=float(input('Enter a height for the rocket in ft: '))
while h<=0:
    h=float(input('Height must be positive. Enter another value: '))
m_0=m_R+q*b #calculates rocket's initial mass, including fuel,
            #based on the given formula
h_b=u/q*(m_0-q*b)*math.log(m_0-q*b)+u*(math.log(m_0)+1)*b-g*(b**2)/2\
    -u*m_0/q*math.log(m_0) #rocket's height when it runs out of fuel
v_b=u*math.log(m_0/(m_0-q*b))-g*b #rocket's velocity when it runs out of fuel
h_p=h_b+v_b**2/(2*g) #maximum height rocket can reach based on its burn time
tolerance=1e-5
t=0
if abs(h-h_p)<=tolerance:
    t=b+v_b/g #if the user-specified height h equals the peak height,
              #then the time the rocket takes to reach h can be calculated
              #using the given formula for amount of time the rocket will take
              #to reach peak height
    print(f'It will take {t} seconds to reach {h} ft')
elif h<h_p:
    h_t=0
    #calculates the height of the rocket at increasing values of time t
    #until h is reached
    while h_t<h:
        t=t+0.1
        if t<b:
            h_t=u/q*(m_0-q*t)*math.log(m_0-q*t)+u*(math.log(m_0)+1)*t\
                -g*(t**2)/2-u*m_0/q*math.log(m_0)
        else: #once the rocket runs out of fuel,
              #a different formula must be used to calculate height
            h_t=h_b+v_b*(t-b)-g*((t-b)**2)/2
    print(f'It will take {t} seconds to reach {h} ft')
else: #if h is not less than or equal to the peak height,
      #then will not be reached
    print('Rocket will not reach that height')