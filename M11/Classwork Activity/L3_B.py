def OddOccurence(arr):
    res=0
    for element in arr:
        res=res^element
    return res

arr=[]
n=int(input("Enter array size: "))
while n:
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1
print("OddOccuring number is:", OddOccurence(arr))

'''
11,10,11,01,01,01

11 -> 01 -> 10 -> 11 -> 10 -> 11

10
01 & 11 -> 01


'''