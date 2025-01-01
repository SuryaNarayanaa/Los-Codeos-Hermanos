def check_prime( n ):
    
    for i  in range(2,n):
        if(n%i ==0 ):
            return False
    return True

n1 , n2 =  map(int , input("Enter the starrtign and ending range : ").split())

for i in range(n1,n2):
    if(check_prime(i) ):
        print(i , sep=' ')
