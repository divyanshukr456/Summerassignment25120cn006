def max_occurring(s):
    from collections import Counter
    if not s: return None
    counts = Counter(s)
    return counts.most_common(1)[0][0]
s = input("Enter string: ")
print("Maximum occurring character:", max_occurring(s))
