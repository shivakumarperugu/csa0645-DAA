from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit))
    starts = [job[0] for job in jobs]

    n = len(jobs)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        j = bisect_left(starts, jobs[i][1])
        dp[i] = max(dp[i + 1], jobs[i][2] + dp[j])

    return dp[0]

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(jobScheduling(startTime, endTime, profit))