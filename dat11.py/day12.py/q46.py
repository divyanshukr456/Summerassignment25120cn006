def armstrong(n):
    digits = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n

num = int(input("Enter: "))

if armstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")