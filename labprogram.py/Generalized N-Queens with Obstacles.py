def generalized_n_queens(rows, cols, obstacles=set()):
    board = [-1] * rows

    def safe(r, c):
        if (r, c) in obstacles:
            return False
        for i in range(r):
            if board[i] == c or abs(board[i] - c) == abs(i - r):
                return False
        return True

    def solve(r):
        if r == rows:
            return True
        for c in range(cols):
            if safe(r, c):
                board[r] = c
                if solve(r + 1):
                    return True
        return False

    if solve(0):
        print(board)
    else:
        print("No Solution")

generalized_n_queens(5,5,{(2,2),(4,4)})