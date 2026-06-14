def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2

        print(f"Step {step}:")
        print(f"Low = {low}, High = {high}, Mid = {mid}")
        print(f"arr[{mid}] = {arr[mid]}\n")

        if arr[mid] == key:
            return mid + 1  # 1-based position

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

        step += 1

    return -1


# Test Case 1
arr = [3, 9, 14, 19, 25, 31, 42, 47, 53]
key = 31

position = binary_search(arr, key)

if position != -1:
    print("Element found at position:", position)
else:
    print("Element not found")