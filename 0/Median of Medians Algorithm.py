def median_of_medians(arr, k):
    # Base case
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide array into groups of 5
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Find medians of each group
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Recursively find pivot
    pivot = median_of_medians(medians, len(medians)//2)

    # Partition array
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]

    if k < len(low):
        return median_of_medians(low, k)

    elif k < len(low) + len(equal):
        return pivot

    else:
        return median_of_medians(
            high,
            k - len(low) - len(equal)
        )


# Test Case 1
arr = [12, 3, 5, 7, 19]
k = 2
print("Output:", median_of_medians(arr, k))