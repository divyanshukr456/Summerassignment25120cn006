def count_digits(n):
    return len(str(abs(n)))
n = int(input("Enter number: "))
print("Number of digits:", count_digits(n))
