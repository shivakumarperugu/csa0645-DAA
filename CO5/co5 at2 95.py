def subset_sum(arr, target):
    arr.sort()
    result = []

    def backtrack(start, current_sum, subset):

        if current_sum == target:
            result.append(subset[:])
            return True

        if current_sum > target:
            return False

        found = False

        for i in range(start, len(arr)):

            # Skip duplicates at same level
            if i > start and arr[i] == arr[i - 1]:
                continue

            subset.append(arr[i])

            if backtrack(i + 1,
                         current_sum + arr[i],
                         subset):
                found = True

            subset.pop()

        return found

    if backtrack(0, 0, []):
        print("Valid Subset(s):")
        for s in result:
            print(s)
    else:
        print("No Valid Subset Found")


# Sample Input
arr = [1, 2, 2, 3, 5]
target = 7

subset_sum(arr, target)