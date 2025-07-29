# Take input values from user
x=input("Enter Value of x: ")
y=input("Enter Value of y: ")
z=input("Enter Value of z: ")

# Swapping
i = x
x = y
y = i
i = y
y = z
z = i

# Displaying results after swapping
print("Value of x after swapping: ", x)
print("Value of y after swapping: ", y)
print("Value of z after swapping: ", z)
