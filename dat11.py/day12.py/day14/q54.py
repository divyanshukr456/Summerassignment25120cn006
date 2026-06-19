arr = [1, 2, 3, 2, 4, 2, 5]

key = int(input("Enter element: "))

count = 0

for i in arr:
    if i == key:
        count += 1

print("Frequency =", count)