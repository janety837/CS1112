import fun
def approx_trapezoids (a, b, n):
    """
    Approximate the integral of the mathematical function coded in
    fun.function() from a to b using n trapezoids.
    Parameters :
    a (float): The lower limit of integration
    b (float): The upper limit of integration
    n (int): The number of trapezoids to use in the approximation
    Returns as a tuple:
    inte (float): The approximated integral
    fvals (list or array): The list or array of the n +1 function values
    evaluated, using fun.function(), in performing the approximation.
    """
    h=(b-a)/n
    inte=0 #initializes inte, the total area that has been calculated so far
    fvals=[] #initialzes the list of values that will eventually be returned
    for i in range(n+1):
        f=fun.function(i*h+a)
        fvals.append(f)
    for i in range(n):
        inte=inte+(fvals[i]+fvals[i+1])*h/2
    return inte,fvals
