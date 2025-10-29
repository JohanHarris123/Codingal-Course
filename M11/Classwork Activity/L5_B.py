def divide(ourdividend, ourDivisor):
    sign=(-1 if((ourdividend<0)^(ourDivisor<0)) else 1)
    dividend=abs(ourdividend)
    divisor=abs(ourDivisor)

    quotientNumber=0
    tempNumber=0

    for i in range(31,-1,-1):
        if(tempNumber+(divisor<<i) <= dividend):
            tempNumber += divisor << i
            quotientNumber |= 1 << i

    if sign == -1:
        quotientNumber = -quotientNumber
    return quotientNumber

a=int(input("Enter a for a/b: "))
b=int(input("Enter b for a/b: "))
print("Result of", a,"/",b,"is:",divide(a,b))
