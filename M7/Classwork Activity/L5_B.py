def factorial(n):
    if n<0:
        return("Invalid Entry")
    
    elif n==1:
        return(1)
    
    return(n*factorial(n-1)) # 5! => 5*4! => 4*3! => 3*2! => 2*1! => 1

n = int(input("Enter a number: "))
factorial_ = factorial(n)
try:
    print("%d! = %d" % (n, factorial_))
except:
    print(factorial_)