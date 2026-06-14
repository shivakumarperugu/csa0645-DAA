def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:

        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == key:
            return mid + 1, comparisons   # 1-based position

        elif arr[mid] < key:
            left = mid + 1

        else:
            right = mid - 1

    return -1, comparisons


# Test Case 1
arr = [5,10,15,20,25,30,35,40,45]
pos, comp = binary_search(arr, 20)
print("Position =", pos)
print("Comparisons =", comp)

# Test Case 2
arr = [10,20,30,40,50,60]
pos, comp = binary_search(arr, 50)
print("Position =", pos)
print("Comparisons =", comp)

# Test Case 3
arr = [21,32,40,54,65,76,87]
pos, comp = binary_search(arr, 32)
print("Position =", pos)
print("Comparisons =", comp)