from find_and_fill_single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col, only_candidate
from empty_cells import empty_cells_left, first_empty_cell
import copy

#Fyller board med logiken så långt det går
def fill_board(board):
    while True:
        if empty_cells_left(board) == 0:
            break

        find_single_cand_in_house(board)
        find_single_cand_in_row(board)
        find_single_cand_in_col(board)
        only_candidate(board)

        if empty_cells_left(board) > 0 and not find_single_cand_in_house(board) and not find_single_cand_in_row(board) and not find_single_cand_in_col(board) and not only_candidate(board):
            return False
    return True

#Chansar på kandidatsiffror i första tomma platsen och kollar om detta löser hela board
def solve_sudoku(board):
    test_board = copy.deepcopy(board)
    if fill_board(board):
        return board

    if not fill_board(board):
        cell_info = first_empty_cell(board)
        row = cell_info[0]
        col = cell_info[1]
        candidates = cell_info[2]

        for cand in candidates:
            test_board[row][col] = cand
            if fill_board(test_board):
                board = test_board
                return board
            else:
                test_board = copy.deepcopy(board)
