def subsets_with_x(nums, x):
    res = []

    def backtrack(start, path):
        if x in path:
            res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res

print(subsets_with_x([2,3,4,5],3))