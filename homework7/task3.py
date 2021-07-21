from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    left_diagonal = [row[i] for i, row in enumerate(board)]
    right_diagonal = [row[-i] for i, row in enumerate(board, 1)]
    for lines in (board, zip(*board), (left_diagonal, right_diagonal)):
        for row in lines:
            if row[0] in ("o", "x") and all(row[0] == value for value in row):
                return f"{row[0]} wins!"

    return "unfinished!" if any("-" in row for row in board) else "draw!"
