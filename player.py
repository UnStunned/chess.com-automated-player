import time
import pyautogui

import get_best_possible_move

min_x = 294
min_y = 170


# min_x = 383
# min_y = 170

def play(color):
    if color == "W":
        while True:
            first_click, second_click = get_best_possible_move.get_and_set_my_move()

            if first_click != (0, 0) and second_click != (0, 0):
                pyautogui.click(first_click[0] + min_x, min_y + first_click[1])
                time.sleep(0.5)
                pyautogui.click(second_click[0] + min_x, min_y + second_click[1])

                if pyautogui.locateOnScreen(
                        'D:\\Python Programming\\Chess_Automation\\screenshots\\promotion-white.png',
                        confidence=0.8):
                    time.sleep(0.25)
                    pyautogui.click(second_click[0] + min_x, min_y + second_click[1])

            if get_best_possible_move.check_win():
                break

            time.sleep(1)
            get_best_possible_move.get_and_set_opponents_move()
            get_best_possible_move.get_board_view()

            if get_best_possible_move.check_win():
                break
    elif color == "B":
        while True:
            get_best_possible_move.get_and_set_opponents_move()
            get_best_possible_move.get_board_view()

            if get_best_possible_move.check_win():
                break

            first_click, second_click = get_best_possible_move.get_and_set_my_move()

            if first_click != (0, 0) and second_click != (0, 0):
                pyautogui.click(first_click[0] + min_x, min_y + first_click[1])
                time.sleep(0.5)
                pyautogui.click(second_click[0] + min_x, min_y + second_click[1])

                if pyautogui.locateOnScreen(
                        'D:\\Python Programming\\Chess_Automation\\screenshots\\promotion-black.png',
                        confidence=0.8):
                    time.sleep(0.25)
                    pyautogui.click(second_click[0] + min_x, min_y + second_click[1])

            if get_best_possible_move.check_win():
                break


play(get_best_possible_move.playing_as)
