def k_closest(points, k):

    points.sort(key=lambda p: p[0]**2 + p[1]**2)

    return points[:k]


# Test Case 1
print(k_closest([[1,3],[-2,2],[5,8],[0,1]], 2))

# Test Case 2
print(k_closest([[1,3],[-2,2]], 1))

# Test Case 3
print(k_closest([[3,3],[5,-1],[-2,4]], 2))