def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
n = int(input("Enter number: "))
print("Largest prime factor:", largest_prime_factor(n))
