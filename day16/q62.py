arr = list(map(int, input("Enter elements: ").split()))

max_count = 0
max_element = None

for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        max_element = i

print("Element with maximum frequency:", max_element)
print("Frequency:", max_count)