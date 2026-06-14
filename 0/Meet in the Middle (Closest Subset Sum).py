from itertools import combinations
from bisect import bisect_left

def subset_sums(arr):
    sums = []

    for r in range(len(arr)+1):
        for subset in combinations(arr, r):
            sums.append(sum(subset))

    return sums


def closest_subset_sum(arr, target):

    n = len(arr)

    left = arr[:n//2]
    right = arr[n//2:]

    left_sums = subset_sums(left)
    right_sums = sorted(subset_sums(right))

    best_sum = None
    min_diff = float('inf')

    for s in left_sums:

        remain = target - s

        idx = bisect_left(right_sums, remain)

        for j in [idx-1, idx]:
            if 0 <= j < len(right_sums):
                total = s + right_sums[j]

                if abs(target-total) < min_diff:
                    min_diff = abs(target-total)
                    best_sum = total

    return best_sum


# Test Case A
arr = [45,34,4,12,5,2]
print("Closest Sum =", closest_subset_sum(arr,42))

# Test Case B
arr = [1,3,2,7,4,6]
print("Closest Sum =", closest_subset_sum(arr,10))