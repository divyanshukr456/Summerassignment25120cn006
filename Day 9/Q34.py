def print_reverse_number_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
n = int(input("Enter number of rows: "))
print_reverse_number_triangle(n)
