import math
def prime(n):
    if n<=0:
        return("Invalid Entry")
    
    elif n==1:
        return("Not a prime number")
    
    for i in range(2,int(math.sqrt(n))+1): #"int(math.sqrt(n))+1" can be replaced by n
        if n%i==0:
            return("not a prime number")
    return("a prime number")

n = int(input("Enter a number: "))
print(f"{n} is {prime(n)}")