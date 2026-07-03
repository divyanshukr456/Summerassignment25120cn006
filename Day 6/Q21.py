def dec_to_bin(n):
    return bin(n).replace("0b", "")
n = int(input("Enter decimal number: "))
print("Binary:", dec_to_bin(n))
