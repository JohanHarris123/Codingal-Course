numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))

while(numberSmallest):
    numberStore=numberSmallest
    numberSmallest=numberLargest%numberSmallest
    numberLargest=numberStore

print(f"HCF of {numberLargest} and {numberSmallest} is {numberLargest}")

for i in range(1, (numberLargest*numberSmallest)+1):
    if i%numberLargest==0 and i%numberSmallest==0:
        print(f"LCM of {numberLargest} and {numberSmallest} is {i}")
        break