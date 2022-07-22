from re import I


def sum_square(n):
    
    a=0
    for i in range (0,n):
        a=a+i*i 
        i+=1

    return a 

x=input ("the input number:")
b=int(x)
print(sum_square(b))

