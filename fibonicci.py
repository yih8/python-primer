def fib(i) :
    my_list=[1,1]
    if i==1:
        return [1]
    elif i==2:
        return [1,1]
    elif i>2:
        for a in range (2,i):
            x=my_list[a-2]+my_list[a-1]
            my_list.append(x)
            a+=1
    return my_list 

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(5))
print(fib(10))
           
