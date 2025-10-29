def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("After swapping: a =",a,"b =",b)

def swap2(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("After swapping: a =",a,"b =",b)

swap(2,3)
swap2(2,3)
