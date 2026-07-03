def print_repeated_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
        print()
n = int(input("Enter number of rows: "))
print_repeated_number_pattern(n)
