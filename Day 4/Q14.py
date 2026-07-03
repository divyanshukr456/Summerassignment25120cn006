def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
n = int(input("Enter n (0-indexed): "))
print(f"{n}th term:", nth_fibonacci(n))
