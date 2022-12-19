import chess
from stockfish import Stockfish
import time

import chess_board_extraction_black
import chess_board_extraction_white
import web_automation

stockfish = Stockfish('stockfish-windows-2022-x86-64-modern.exe')
# stockfish.set_depth(5)
board = chess.Board()
playing_as = input("What are you playing as? : ")

if playing_as == "W":
    time.sleep(3)


def convert_to_string(li: list):
    if li is not None:
        option = ""
        for i in li:
            option += i
        return option


def calculate_whose_turn():
    whose_turn = board.turn

    if whose_turn is True:
        whose_turn = "W"
    else:
        whose_turn = "B"
    return whose_turn


def get_best_move(color):
    if color == playing_as:
        stockfish.set_fen_position(board.fen())
        stockfish.get_evaluation()
        best_move = stockfish.get_best_move()
        return best_move


def get_and_set_opponents_move():
    options = []

    if playing_as == "W":
        options, color = chess_board_extraction_white.get_move()
        print(options)
    elif playing_as == "B":
        options, color = chess_board_extraction_black.get_move()
        print(options)

    while not options:
        if playing_as == "W":
            options, color = chess_board_extraction_white.get_move()
        elif playing_as == "B":
            options, color = chess_board_extraction_black.get_move()

    if options:
        option_1 = ""
        option_2 = ""

        for _ in options:
            option_1 += _

        options.reverse()

        for _ in options:
            option_2 += _

        legal_moves = list(board.legal_moves)

        for _ in range(len(legal_moves)):
            legal_moves[_] = str(legal_moves[_])

        opponents_move = ""

        if option_1 in legal_moves:
            opponents_move = option_1

        if option_2 in legal_moves:
            opponents_move = option_2

        if opponents_move != "":
            board.push_san(opponents_move)
            stockfish.set_fen_position(board.fen())


def get_board_view():
    print()
    print(board)
    print()


def get_and_set_my_move():
    if calculate_whose_turn() == playing_as:
        best_move = get_best_move(color=playing_as)
        board.push_san(best_move)
        stockfish.set_fen_position(board.fen())
        first_click = best_move[0:2]
        second_click = best_move[2:]
        print(best_move)

        if playing_as == "W":
            return chess_board_extraction_white.get_coordinates(
                first_click), chess_board_extraction_white.get_coordinates(second_click)
        elif playing_as == "B":
            return chess_board_extraction_black.get_coordinates(
                first_click), chess_board_extraction_black.get_coordinates(second_click)
    else:
        return (0, 0), (0, 0)


def clear_highlights():
    web_automation.run_scripts()


def check_win():
    return board.is_checkmate()


def check_promotion():
    return board.promoted
