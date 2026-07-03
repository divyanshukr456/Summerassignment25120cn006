def first_repeating(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
s = input("Enter string: ")
print("First repeating character:", first_repeating(s))
