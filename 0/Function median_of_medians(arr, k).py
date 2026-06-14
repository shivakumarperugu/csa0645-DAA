def median_of_medians(arr, k):
    if len(arr) <= 5:
        arr.sort()
        return arr[k]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    medians = []
    for group in groups:
        group.sort()
        medians.append(group[len(group)//2])

    pivot = median_of_medians(medians, len(medians)//2)

    left = []
    middle = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)

    if k < len(left):
        return median_of_medians(left, k)

    elif k < len(left) + len(middle):
        return pivot

    return median_of_medians(
        right,
        k - len(left) - len(middle)
    )


# Test Case 1
arr = [1,2,3,4,5,6,7,8,9,10]
k = 5      # 6th smallest element
print("K-th Smallest Element =", median_of_medians(arr, k))

# Test Case 2
arr = [23,17,31,44,55,21,20,18,19,27]
k = 4      # 5th smallest element
print("K-th Smallest Element =", median_of_medians(arr, k))