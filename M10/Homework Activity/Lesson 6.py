primes = []
for num in range(10, 100):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        primes.append(num)

print("Prime numbers between 10 and 99:", primes)