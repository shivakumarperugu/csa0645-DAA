def partition(arr, low, high):

    pivot = arr[low]
    i = low + 1
    j = high

    while True:

        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(arr, low, high):

    if low < high:

        p = partition(arr, low, high)

        print("Partition:", arr)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

    return arr


# Test Case 1
arr = [10,16,8,12,15,6,3,9,5]
print("Sorted:", quick_sort(arr, 0, len(arr)-1))

# Test Case 2
arr = [12,4,78,23,45,67,89,1]
print("Sorted:", quick_sort(arr, 0, len(arr)-1))

# Test Case 3
arr = [38,27,43,3,9,82,10]
print("Sorted:", quick_sort(arr, 0, len(arr)-1))