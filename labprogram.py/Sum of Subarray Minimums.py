def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    ans = 0

    for i in range(n):
        mn = arr[i]
        for j in range(i, n):
            mn = min(mn, arr[j])
            ans += mn

    return ans % MOD

print(sumSubarrayMins([3,1,2,4]))