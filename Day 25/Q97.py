def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res
arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))
print("Merged array:", merge_sorted_arrays(arr1, arr2))
