# simple sudoku solver, using a backtracking algorithm
# takes 9x9 sudoku board and prints solution to console

import numpy as np
import sample_boards

board = sample_boards.board2

grid = np.matrix(board)


# is possible to put this number here
def is_possible(row, col, n):
    # check row
    for i in range(9):
        if grid[row, i] == n:
            return False

    # check column
    for j in range(9):
        if grid[j, col] == n:
            return False

    # check 3x3 box
    col_mod = col % 3
    row_mod = row % 3
    sub_matrix = grid[row - row_mod:row + 3 - row_mod, col - col_mod: col + 3 - col_mod]
    for k in sub_matrix.A1:
        if k == n:
            return False

    return True


def solve():
    # global grid
    for i in range(9):
        for j in range(9):
            if grid[i, j] == 0:
                for k in range(1, 10):
                    if is_possible(i, j, k):
                        grid[i, j] = k
                        solve()
                        grid[i, j] = 0
                return
    print(grid)


solve()

# algorithm:
# find empty
# for 1..9 check if possible: put it
# solve recursion
# put empty again
