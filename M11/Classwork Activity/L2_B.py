def setOrNot(number,n):
    if number & (1 << (n-1)):
        print("SET")
    else:
        print("NOT SET")

number = int(input("Enter your number: "))
n=int(input("Enter the bit position: "))
setOrNot(number,n)

# The above code checks whether the nth bit in the binary representation of a given integer is set (1) or not set (0).
