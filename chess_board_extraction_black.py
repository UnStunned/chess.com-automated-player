import time

import cv2 as cv
import pyautogui

screenshot_directory = 'D:\\Python Programming\\Chess_Automation\\screenshots\\'

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8']


def quantize(x: int):
    return int(x / 100) + 1


def get_file(x: int):
    f = quantize(x)
    output_file = list(map(lambda y: 7 - FILES.index(y) + 1, FILES))
    file = output_file.index(f)
    return FILES[file]


def get_rank(x: int):
    r = quantize(x)
    output_rank = list(map(lambda y: RANKS.index(str(y)) + 1, RANKS))
    rank = output_rank.index(r)
    return RANKS[rank]


def get_image():
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    screenshot.save('D:\\Python Programming\\Chess_Automation\\screenshots\\current-chess-board.png')

    full_screen = cv.imread(screenshot_directory + 'current-chess-board.png')
    # chess_board = full_screen[169:969, 382: 1182]
    chess_board = full_screen[169:969, 294: 1094]

    cv.imwrite('D:\\Python Programming\\Chess_Automation\\screenshots\\current-chess-board.png', chess_board)

    squares = []
    coordinates = []

    for i in range(5, chess_board.shape[0], 100):
        for j in range(5, chess_board.shape[1], 100):
            if list(chess_board[i, j]) == [43, 202, 186] or list(chess_board[i, j]) == [105, 246, 246] or list(
                    chess_board[i, j]) == [105, 247, 247] or list(chess_board[i, j]) == [95, 241, 246]:
                squares.append(chess_board[i - 5:i + 95, j - 5:j + 95])
                coordinates.append((j - 5 + 50, i - 5 + 80))

    if len(squares) == 2:
        square_1 = squares[0]
        square_2 = squares[1]

        cv.imwrite('D:\\Python Programming\\Chess_Automation\\screenshots\\highlighted-square-1.png', square_1)
        cv.imwrite('D:\\Python Programming\\Chess_Automation\\screenshots\\highlighted-square-2.png', square_2)

    return coordinates


def get_move():
    coordinates = get_image()
    move = []
    for _ in coordinates:
        file = _[0]
        file = get_file(file)
        rank = _[1]
        rank = get_rank(rank)
        move.append(str(file) + str(rank))
    color = get_color()
    return move, color


def get_color():
    pixel_1 = cv.imread(screenshot_directory + '//highlighted-square-1.png')[78, 50]
    pixel_2 = cv.imread(screenshot_directory + '//highlighted-square-2.png')[78, 50]

    if list(pixel_1) == [82, 83, 86] or list(pixel_2) == [82, 83, 86]:
        return "B"
    else:
        return "W"


def get_coordinates(move: str):
    return (7 - FILES.index(move[0])) * 100 + 50, (RANKS.index(move[1])) * 100 + 50
