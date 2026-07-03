def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = sum(int(digit)**power for digit in s)
    return total == n
n = int(input("Enter number: "))
if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not Armstrong number")
