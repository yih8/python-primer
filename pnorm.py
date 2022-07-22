import math
from struct import pack

def p_norm (p,v):
    d=0
    n=len(v)
    for i in range (0,n):
        d =d + v[i]**p
        i+=1
    a= math.log10(d)
    b=a/p 
    c=10**b
    return c


print (p_norm(2,[3,4]))
print (p_norm(4,[5,6,7,8,9]))