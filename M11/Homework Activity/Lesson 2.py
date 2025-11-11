def checkRightBit(number, n):
    while n:
        pos = 1
        while number:
            if number & 1:
                return pos
            number >>= 1
            pos += 1
        return 0
    
input_number = int(input("Enter a number: "))
print(checkRightBit(input_number, len(str(input_number))))