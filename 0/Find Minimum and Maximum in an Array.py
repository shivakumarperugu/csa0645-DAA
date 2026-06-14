def find_min_max(arr):
    if not arr:
        return None, None

    minimum = maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


# Test Case 1
arr = [5,7,3,4,9,12,6,2]
mn, mx = find_min_max(arr)
print("Min =", mn, "Max =", mx)

# Test Case 2
arr = [1,3,5,7,9,11,13,15,17]
mn, mx = find_min_max(arr)
print("Min =", mn, "Max =", mx)

# Test Case 3
arr = [22,34,35,36,43,67,12,13,15,17]
mn, mx = find_min_max(arr)
print("Min =", mn, "Max =", mx)