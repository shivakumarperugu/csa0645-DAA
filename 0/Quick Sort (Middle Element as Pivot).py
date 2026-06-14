def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print("Pivot =", pivot)
    print("Left =", left)
    print("Middle =", middle)
    print("Right =", right)
    print()

    return quick_sort(left) + middle + quick_sort(right)


# Test Case 1
arr = [19,72,35,46,58,91,22,31]
print("Sorted Array:", quick_sort(arr))

# Test Case 2
arr = [31,23,35,27,11,21,15,28]
print("Sorted Array:", quick_sort(arr))

# Test Case 3
arr = [22,34,25,36,43,67,52,13,65,17]
print("Sorted Array:", quick_sort(arr))