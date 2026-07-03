def print_repeated_character_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(64 + i), end="")
        print()
n = int(input("Enter number of rows: "))
print_repeated_character_pattern(n)
