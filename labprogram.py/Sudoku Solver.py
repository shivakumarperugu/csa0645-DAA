def solve_sudoku(board):

    def valid(r, c, num):
        for i in range(9):
            if board[r][i] == num:
                return False
            if board[i][c] == num:
                return False

        sr = (r // 3) * 3
        sc = (c // 3) * 3

        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if valid(r, c, num):
                            board[r][c] = num
                            if solve():
                                return True
                            board[r][c] = '.'
                    return False
        return True

    solve()
    return board