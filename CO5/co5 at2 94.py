def is_valid(grid, row, col, num):
    # Check row
    for c in range(9):
        if grid[row][c] == num:
            return False

    # Check column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True


def sudoku_solver(grid, empty_cells, index):
    # Base case
    if index == len(empty_cells):
        return True

    row, col = empty_cells[index]

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if sudoku_solver(grid, empty_cells, index + 1):
                return True

            # Backtrack
            grid[row][col] = 0

    return False


# Sample Sudoku Grid (0 = empty)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Fixed order of empty cells
empty_cells = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            empty_cells.append((i, j))

if sudoku_solver(grid, empty_cells, 0):
    print("Solved Sudoku:")
    for row in grid:
        print(row)
else:
    print("No Solution Exists")