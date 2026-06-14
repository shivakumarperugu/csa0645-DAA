from collections import defaultdict

def four_sum_count(A, B, C, D):

    ab_sum = defaultdict(int)

    for a in A:
        for b in B:
            ab_sum[a + b] += 1

    count = 0

    for c in C:
        for d in D:
            count += ab_sum[-(c + d)]

    return count


# Test Case 1
A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]

print(four_sum_count(A,B,C,D))

# Test Case 2
A = [0]
B = [0]
C = [0]
D = [0]

print(four_sum_count(A,B,C,D))