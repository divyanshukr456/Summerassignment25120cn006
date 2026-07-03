def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = sum(int(digit)**power for digit in s)
    return total == n
start = int(input("Enter start: "))
end = int(input("Enter end: "))
for i in range(start, end + 1):
    if is_armstrong(i):
        print(i, end=" ")
print()
