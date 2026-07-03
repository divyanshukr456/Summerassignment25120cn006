def power(x, n):
    res = 1
    for _ in range(n):
        res *= x
    return res
x = int(input("Enter base x: "))
n = int(input("Enter exponent n: "))
print("Result:", power(x, n))
