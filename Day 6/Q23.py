def count_set_bits(n):
    return bin(n).count("1")
n = int(input("Enter number: "))
print("Number of set bits:", count_set_bits(n))
