import pygame as pg
from constants import WIDTH, HEIGH, FPS
from board import Board
import sample_boards
import pyautogui

pg.init()


def main():
    win = pg.display.set_mode((WIDTH, HEIGH))
    pg.display.set_caption('SUDOKU')

    run = True
    clock = pg.time.Clock()

    bd = sample_boards.board2

    board = Board(bd)

    pyautogui.alert("Let's solve this sudoku")
    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            # if event.type == pg.MOUSEBUTTONDOWN:
            if board.solve(win):
                pyautogui.alert("Sudoku is solved!")
                run = False

        pg.display.update()

    pg.quit()


main()
