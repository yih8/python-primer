from re import A


def minmax(data):
    n = len(data)
    i=0 
    min=data[0]
    max=data[0]
    k=0
    while i <=n-1:
        a=data[i]
        
        if int(a)>=int(min):
            i+=1
            continue
        elif int(a)<int(min):
            min=a 
            i+=1 
    while k<=n-1:
        b=data[k]
        if int(b)>int(max):
            max=b 
            k+=1
        elif int(b)<=int(max):
            k+=1 
            continue
    return (int(min),int(max))

d= input("input number:")

print(minmax(d))