import random
from decide_candidates import determine_candidates
from single_candidates import house_list_candidates, find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col
from house_list_generator import identify_row, identify_col
from fill_in_cell import fill_single_cand_in_house

board = [
    [5,0,0,0,0,0,3,4,0],
    [2,0,0,0,0,7,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,3,0,0,0,5,0],
    [0,1,4,0,0,0,0,0,0],
    [0,7,0,0,0,0,0,0,0],
    [0,0,0,8,0,0,0,0,2],
    [6,0,0,5,0,0,0,0,0],
    [0,2,0,0,0,0,7,0,0],
]

for row in board:
    print(row)

print("")
fill_single_cand_in_house(board)

for row in board:
    print(row)

