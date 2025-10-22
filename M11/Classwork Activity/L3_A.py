def checkIfSame(number1,number2):
    if((number1 ^ number2) != 0):
        print("numbers are not equal")
    else:
        print("numbers are equal")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
checkIfSame(number1,number2)
