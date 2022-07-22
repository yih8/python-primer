import random
import math
a=0
for i in range (0,10000000):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    c=x*x+y*y
    r = math.sqrt(c)
    if r<1:
        a+=1
        i+=1
    else:
        i+=1
        continue 
pi=4*a/10000000
print("pi=",pi)