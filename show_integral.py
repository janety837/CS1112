import integral
print (' n      approximated integral')
print ('-------------------------------------')
#calculates the integral and prints it out for various values of n(number of
#trapezoids to break the range into)
for n in range (20,101,20):
    (int_approx,vals)=integral.approx_trapezoids(-1,4,n)
    print(f'{float(n):3.0f}{int_approx:20.4f}')