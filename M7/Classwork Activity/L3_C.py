num = int(input("Enter a number: "))

def check_num(n):
    if n > 50:
        print("The number is greater than 50.")
        if n % 2 == 0:
            print("And it is even too.")
        else:
            print("And it is odd.")
    else:
        print("The number is less than 50")

check_num(num)
if num < 0:
    print("But the number is negative, so the number converted to positive is:", abs(num))