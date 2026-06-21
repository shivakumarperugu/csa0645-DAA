def solve_n_queens(n):
    board = [-1] * n
    res = []

    def is_safe(r, c):
        for i in range(r):
            if board[i] == c or abs(board[i] - c) == abs(i - r):
                return False
        return True

    def backtrack(row):
        if row == n:
            res.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)

    if res:
        sol = res[0]
        for r in range(n):
            row = ['.'] * n
            row[sol[r]] = 'Q'
            print(' '.join(row))

solve_n_queens(4)