s = input("Enter a string: ")

seen = []

for ch in s:
    if ch in seen:
        print("First repeating character:", ch)
        break
    seen.append(ch)
else:
    print("No repeating character found.")
    