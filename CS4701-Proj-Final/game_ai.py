import numpy as np
import matplotlib.pyplot as plt

SIMULATION_COUNT = 100

# SPM_SCALE_PARAM = 10
# SL_SCALE_PARAM = 4
# SEARCH_PARAM = 200

from game_functions import (
    initialize_game,
    random_move,
    move_down,
    move_left,
    move_right,
    move_up,
    check_for_win,
    add_new_tile,
    game_over,
)


# def get_search_params(move_number):
#     searches_per_move = SPM_SCALE_PARAM * (1 + (move_number // SEARCH_PARAM))
#     search_length = SL_SCALE_PARAM * (1 + (move_number // SEARCH_PARAM))
#     return searches_per_move, search_length


def ai_move(board):
    possible_first_moves = [
        move_left,
        move_up,
        move_down,
        move_right,
    ]  # list only gets function without call
    first_move_scores = [0, 0, 0, 0]

    for i, move in enumerate(possible_first_moves):
        AI = board
        first_move_function = move  # getting a first move
        (
            board_with_first_move,
            _,
            _,
        ) = first_move_function(AI)
        search_board = np.copy(board_with_first_move)
        rand_board, is_valid, rand_score = random_move(search_board)
        AI = rand_board
        if is_valid:
            AI = add_new_tile(AI)
            first_move_scores[i] += rand_score

    highestScore = max(first_move_scores)
    highestScoreIndex = first_move_scores.index(highestScore)
    best_move = possible_first_moves[highestScoreIndex]
    search_board, game_valid, score = best_move(board)
    return search_board, game_valid, score
