def print_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")
n = int(input("Enter side length: "))
print_hollow_square(n)
