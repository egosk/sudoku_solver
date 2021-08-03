import pygame as pg
from constants import GREY, ROWS, COLS, SQUARE_SIZE, BLACK
import numpy as np


class Board:
    def __init__(self, grid):
        # self.board = grid  # matrix with numbers
        self.grid = np.matrix(grid)
        self.selected_cube = None

    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                pg.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE - 2, SQUARE_SIZE - 2))

        # bold lines
        for i in range(1, ROWS // 3):
            pg.draw.line(win, BLACK, (3 * i * SQUARE_SIZE, 0), (3 * i * SQUARE_SIZE, 9 * SQUARE_SIZE), 6)
            pg.draw.line(win, BLACK, (0, 3 * i * SQUARE_SIZE), (9 * SQUARE_SIZE, 3 * i * SQUARE_SIZE), 6)

    def display_numbers(self, win):
        font1 = pg.font.SysFont('chalkduster.ttf', 72)
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[col, row] != 0:
                    surface_tmp = font1.render(str(self.grid[col, row]), True, BLACK)
                    win.blit(surface_tmp, (row * SQUARE_SIZE + ((SQUARE_SIZE - surface_tmp.get_width()) / 2),
                                           col * SQUARE_SIZE + ((SQUARE_SIZE - surface_tmp.get_height()) / 2)))

    def is_possible(self, row, col, n):
        # check row
        for i in range(9):
            if self.grid[row, i] == n:
                return False

        # check column
        for j in range(9):
            if self.grid[j, col] == n:
                return False

        # check 3x3 box
        col_mod = col % 3
        row_mod = row % 3
        sub_matrix = self.grid[row - row_mod:row + 3 - row_mod, col - col_mod: col + 3 - col_mod]
        for k in sub_matrix.A1:
            if k == n:
                return False

        return True

    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    return False
        return True

    def solve(self, win):
        self.draw_cubes(win)
        self.display_numbers(win)
        pg.display.update()
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    for k in range(1, 10):
                        if self.is_possible(i, j, k):
                            self.grid[i, j] = k
                            self.draw_cubes(win)
                            self.display_numbers(win)
                            pg.display.update()
                            pg.time.delay(30)
                            self.solve(win)
                            if self.is_solved():
                                return True
                            self.grid[i, j] = 0
                            self.draw_cubes(win)
                            self.display_numbers(win)
                            pg.display.update()

                    return

