def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def print_fibonacci(count):
    for i in range(count):
        print(fib(i))

print_fibonacci(10)