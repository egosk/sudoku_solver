import pygame as pg
from constants import WIDTH, HEIGH, FPS
from board import Board
import sample_boards
import simple_sudoku_solver


pg.init()


def main():
    win = pg.display.set_mode((WIDTH, HEIGH))
    pg.display.set_caption('SUDOKU')

    run = True
    clock = pg.time.Clock()

    bd = sample_boards.board2

    board = Board(bd)

    solved = False

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
        # board.draw_cubes(win)
        while not solved:
            solved = board.solve(win)
        # board.display_numbers(win)
        pg.display.update()

    pg.quit()

main()