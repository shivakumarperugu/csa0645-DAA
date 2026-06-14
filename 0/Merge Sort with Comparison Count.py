comparisons = 0

def merge_sort(arr):
    global comparisons

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Test Case 1
comparisons = 0
arr = [12,4,78,23,45,67,89,1]
sorted_arr = merge_sort(arr)

print("Sorted Array:", sorted_arr)
print("Comparisons:", comparisons)

# Test Case 2
comparisons = 0
arr = [38,27,43,3,9,82,10]
sorted_arr = merge_sort(arr)

print("Sorted Array:", sorted_arr)
print("Comparisons:", comparisons)