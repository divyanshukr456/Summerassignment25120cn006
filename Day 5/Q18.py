def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
def is_strong(n):
    if n <= 0: return False
    total = sum(factorial(int(digit)) for digit in str(n))
    return total == n
n = int(input("Enter number: "))
if is_strong(n):
    print("Strong number")
else:
    print("Not strong number")
