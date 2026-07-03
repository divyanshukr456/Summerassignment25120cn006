def print_reverse_star_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)
n = int(input("Enter number of rows: "))
print_reverse_star_pattern(n)
