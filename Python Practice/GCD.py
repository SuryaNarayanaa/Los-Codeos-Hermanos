import math
def  gcd(n1,n2):
    if(n1==0 ):
        return n2
    if(n2 ==0 ):
        return n1
    return gcd(n2 , n1%n2)


print(math.gcd(60, 48))
print(gcd(60.,48))