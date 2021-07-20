import pygame as pg
from constants import WIDTH, HEIGH, FPS
from board import Board


pg.init()

# class Board:
#     def __init__(self):



def main():
    win = pg.display.set_mode((WIDTH, HEIGH))
    pg.display.set_caption('SUDOKU')

    run = True
    clock = pg.time.Clock()

    bd = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    board = Board(bd)


    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
        board.draw_cubes(win)
        pg.display.update()

    pg.quit()

main()