


from base64 import b16decode


def is_multiple(n,m):
    i=1
    b=1
    while b>0 :
        b=i*m 
        if n==b :
            return True 
            break 
        elif b<n:
            i+=1
            continue 
        elif b>n :
            return False 
            break 



a=is_multiple(9,3)
b=is_multiple(7,2)
print(a,b)



