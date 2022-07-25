def sum_square(n):
    i=0
    d=[] 
    sum=0 
    while i<n: 
        sum = i**2+sum 
        i+=1
        d.append(sum)
    return d


a=input("the number of sum Square:")
c=int(a)

b=sum_square(c)

print (b)