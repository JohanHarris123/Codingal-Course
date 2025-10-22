def TwoOdd(arr,size):
    xorof2 = arr[0]
    x,y,SetBit=0,0,0

    for i in range(1,size):
        xorof2 = xorof2 ^ arr[i]

    SetBit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if(arr[i] & SetBit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    return x,y

arr=[]
arr_size=int(input("Enter array size: "))
for i in range(0,arr_size):
    z=int(input("Enter element: "))
    arr.append(z)

x,y=TwoOdd(arr,arr_size)
print("TwoOdd elements are:",x,"and",y)
