arr = [12, 45, 7, 89, 34]

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest =", second)