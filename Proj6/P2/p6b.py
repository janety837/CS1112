import random
def select_r ( lis , k ):
    """
    Returns ( int or float ) the kth smallest value in list lis , selected by
    using a RANDOM splitter , using RECURSION .
    Parameters
    lis : a non - empty list or array of numbers
    k : an int in [0.. n -1] where n is the length of lis
    """
    n=len(lis)
    i=random.randint(0,n-1) #index of splitter
    splitter=lis[i]
    
    #initiates lists
    little_vals=[]
    big_vals=[]
    
    #the following code determines whether the other terms belong in little_vals
    #or big_vals. Skips over index i because that's splitter.
    for j in range(i):
        temp_val=lis[j]
        if temp_val<splitter:
            little_vals.append(temp_val)
        else:
            big_vals.append(temp_val)
    for j in range(i+1,n):
        temp_val=lis[j]
        if temp_val<splitter:
            little_vals.append(temp_val)
        else:
            big_vals.append(temp_val)
    
    #recursive call
    if k<len(little_vals):
        val=select_r(little_vals,k)
    #base case
    elif k==len(little_vals):
        val=splitter
    #recursive call
    else:
        val=select_r(big_vals, k-len(little_vals)-1)
    return val

def my_median ( lis ):
    """
    Returns ( int or float ) the median of list lis
    Parameter lis : a non - empty list or array of numbers
    Makes effective use of select_r .
    Does not use predefined functions median or sort .
    """
    m=int(len(lis)/2)
    if len(lis)%2==1:
        med=select_r(lis,m)
    else:
        med=(select_r(lis,m)+select_r(lis,m-1))/2
    return med

def select_m ( lis , k ):
    """
    Returns ( int of float ) the kth smallest value in list lis , selected by
    using a MIDDLE splitter , using RECURSION . If lis has an even length ,
    define middle as int ( len ( lis )/2).
    Parameters
    lis : a non - empty list or array of numbers
    k : an int in [0.. n -1] where n is the length of lis
    """
    n=len(lis)
    i=int(n/2) #index of splitter
    splitter=lis[i]
    
    #initiates lists
    little_vals=[]
    big_vals=[]
    
    #the following code determines whether the other terms belong in little_vals
    #or big_vals. Skips over index i because that's splitter.
    for j in range(i):
        temp_val=lis[j]
        if temp_val<splitter:
            little_vals.append(temp_val)
        else:
            big_vals.append(temp_val)
    for j in range(i+1,n):
        temp_val=lis[j]
        if temp_val<splitter:
            little_vals.append(temp_val)
        else:
            big_vals.append(temp_val)
    
    #recursive call
    if k<len(little_vals):
        val=select_m(little_vals,k)
    #base case
    elif k==len(little_vals):
        val=splitter
    #recursive call
    else:
        val=select_m(big_vals, k-len(little_vals)-1)
    return val
