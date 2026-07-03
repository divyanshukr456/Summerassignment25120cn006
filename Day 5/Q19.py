def print_factors(n):
    print(f"Factors of {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
n = int(input("Enter number: "))
print_factors(n)
