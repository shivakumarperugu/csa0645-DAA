def minimumTimeRequired(jobs, k):
    workers = [0] * k
    jobs.sort(reverse=True)

    def backtrack(i):
        if i == len(jobs):
            return max(workers)

        ans = float('inf')

        for j in range(k):
            workers[j] += jobs[i]
            ans = min(ans, backtrack(i + 1))
            workers[j] -= jobs[i]

            if workers[j] == 0:
                break

        return ans

    return backtrack(0)

jobs = [1,2,4,7,8]
k = 2
print(minimumTimeRequired(jobs, k))