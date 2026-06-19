arr = list(map(int, input("Enter elements: ").split()))

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Array after removing duplicates:", unique)