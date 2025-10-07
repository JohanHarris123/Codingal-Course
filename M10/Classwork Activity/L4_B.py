def print_factors(number):
    print("The factors of", number, "are:")
    print(1)
    for i in range(2, number//2+1):
        if number % i == 0:
            print(i)
    print(number)

number = int(input("Enter your number to find its factors: "))

print_factors(number)