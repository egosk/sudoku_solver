import pygame as pg
from constants import GREY, ROWS, COLS, SQUARE_SIZE, BLACK

class Board:
    def __init__(self, grid):
        self.board = grid # matrix with numbers
        self.selected_cube= None

    def draw_cubes(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                # if  (row+1)%3 ==0:
                #     pg.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE - n, SQUARE_SIZE - n))
                # else:
                pg.draw.rect(win, GREY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE-2, SQUARE_SIZE-2))

        #bold lines
        for i in range (1, ROWS//3):
            pg.draw.line(win, BLACK, (3*i*SQUARE_SIZE, 0), (3*i*SQUARE_SIZE, 9*SQUARE_SIZE), 6)
            pg.draw.line(win, BLACK, (0, 3 * i * SQUARE_SIZE), (9 * SQUARE_SIZE,  3 * i * SQUARE_SIZE), 6)

    def draw_numbers(self):
        pass