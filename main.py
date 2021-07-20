# sudoku solver with backtracking algorithm
import numpy as np


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]



grid = np.matrix(board)

# is possible to put this number here
def is_possible(row, col, n):
    #check row
    for i in range(9):
        if grid[row, i] == n:
            return False

    #check column
    for j in range(9):
        if grid[j, col] == n:
            return False

    #check 3x3 box
    col_mod = col % 3
    row_mod = row % 3
    sub_matrix = grid[row - row_mod:row + 3 - row_mod, col - col_mod: col + 3 - col_mod]
    for k in sub_matrix.A1:
        if k ==n:
            return False

    return True


def solve():
    # global grid
    for i in range(9):
        for j in range(9):
            if grid[i,j]==0:
                for k in range(1,10):
                    if is_possible(i, j, k):
                        grid[i,j] = k
                        solve()
                        grid[i,j] =0
                return
    print(grid)

solve()



# find empty
# for 1..9 check if possible: put it
# solve recursion
# put empty again
