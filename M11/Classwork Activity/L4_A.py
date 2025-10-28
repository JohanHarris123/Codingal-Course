def power2(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

num = int(input("Enter a number: "))
if power2(num):
    print("\nThe number is a power of 2.")
else:
    print("\nThe number is NOT a power of 2.")