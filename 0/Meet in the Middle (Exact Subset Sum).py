from itertools import combinations
from bisect import bisect_left

def subset_sums(arr):

    sums = []

    for r in range(len(arr)+1):
        for subset in combinations(arr,r):
            sums.append(sum(subset))

    return sums


def exact_subset_sum(arr, target):

    n = len(arr)

    left = arr[:n//2]
    right = arr[n//2:]

    left_sums = subset_sums(left)
    right_sums = sorted(subset_sums(right))

    for s in left_sums:

        needed = target - s

        idx = bisect_left(right_sums, needed)

        if idx < len(right_sums) and right_sums[idx] == needed:
            return True

    return False


# Test Case A
arr = [1,3,9,2,7,12]
print(exact_subset_sum(arr,15))

# Test Case B
arr = [3,34,4,12,5,2]
print(exact_subset_sum(arr,15))