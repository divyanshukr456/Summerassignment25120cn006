arr = list(map(int, input("Enter elements: ").split()))

n = len(arr) + 1

total = n * (n + 1) // 2
actual = sum(arr)

print("Missing Number =", total - actual)