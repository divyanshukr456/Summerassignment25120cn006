def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
n = int(input("Enter number of terms: "))
generate_fibonacci(n)
