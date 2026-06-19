arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])