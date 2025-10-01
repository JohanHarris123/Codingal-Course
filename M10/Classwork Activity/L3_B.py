def sum(n):
    return n*(n+1)/2

# TC = O(1)

def arraysum(a):
    sum=0
    for i in a:
        sum=sum+1

    return sum

a=[12,3,4,15]
arraysum(a)

# TC = O(n)

def summ(n):
    if(n<=0):
        return
    return n+summ(n-1)

# TC = O(n)