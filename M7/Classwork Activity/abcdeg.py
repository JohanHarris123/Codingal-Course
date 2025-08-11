n = int(input("Enter the number of rows: "))

for i in range(0,n):
    print("    " * (n - i - 1), end='')
    for j in range(0,i+1):
        print(" * ", end=' ')
    print("\n")