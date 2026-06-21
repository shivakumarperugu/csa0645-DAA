def findTargetSumWays(nums, target):

    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0

        return (backtrack(i + 1, total + nums[i]) +
                backtrack(i + 1, total - nums[i]))

    return backtrack(0, 0)

print(findTargetSumWays([1,1,1,1,1], 3))