def is_safe(x, y, maze, visited):
    n = len(maze)

    return (0 <= x < n and
            0 <= y < n and
            maze[x][y] == 1 and
            not visited[x][y])

def solve_robot(maze, x, y, goal_x, goal_y, visited, path):

    if x == goal_x and y == goal_y:
        path.append((x, y))
        return True

    visited[x][y] = True
    path.append((x, y))

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if is_safe(nx, ny, maze, visited):
            if solve_robot(maze, nx, ny, goal_x, goal_y,
                           visited, path):
                return True

    path.pop()
    visited[x][y] = False
    return False


# Sample Grid
maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]

n = len(maze)
visited = [[False]*n for _ in range(n)]
path = []

if solve_robot(maze, 0, 0, 3, 3, visited, path):
    print("Path Found:")
    print(path)
else:
    print("No Path Exists")