number = int(input("Enter a number: "))

orignalNumber = number
reverseNumber = 0

while number > 0:
    digit = number % 10
    reverseNumber = reverseNumber * 10 + digit
    number = number // 10

if orignalNumber == reverseNumber:
    print(orignalNumber, "is a palindrome")
else:
    print(orignalNumber, "is not a palindrome")

