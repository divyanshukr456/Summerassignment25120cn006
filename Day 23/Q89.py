def first_non_repeating(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None
s = input("Enter string: ")
print("First non-repeating character:", first_non_repeating(s))
