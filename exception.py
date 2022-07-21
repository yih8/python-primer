def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError("x must be numeric")
    elif x<0:
        raise ValueError("x can not be negative")

try:
    x=sqrt("hi")
except TypeError as err:
    print ("Error:"+str(err))

try:
    x=sqrt(-10)
except ValueError as err:
    print ("Error:"+str(err))