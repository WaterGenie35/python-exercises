import os
from typing import List, Tuple

from utils.typing import Nullable


def solution():
    """
    Solution to Project Euler problem 96
    https://projecteuler.net/problem=96
    """
    print(sum_of_top_left_as_3_digit_num(parse_sudoku("problem_96_sudoku.txt")))


# TODO: optimize
# def test_solution():
#     assert sum_of_top_left_as_3_digit_num(parse_sudoku("problem_96_sudoku.txt")) == 24_702


type Board = List[List[int]]


def parse_sudoku(filename: str) -> List[Board]:
    boards = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        rows = None
        row_count = 0
        for line in file:
            if line[:4] == "Grid":
                rows = []
                row_count = 0
                continue

            rows.append([int(char) for char in line.strip()])
            row_count += 1

            if row_count == 9:
                boards.append(rows)

    return boards


def sum_of_top_left_as_3_digit_num(boards: List[Board]) -> int:
    total = 0
    for board in boards:
        solved_board = solve_sudoku(board)
        total += (100 * solved_board[0][0]) + (10 * solved_board[0][1]) + solved_board[0][2]
    return total


def solve_sudoku(board: Board) -> Board:
    start_row, start_column = next_empty_cell(board, 0, 0)
    stack = [(start_row, start_column, 1)]
    while len(stack) > 0:
        row, column, candidate = stack.pop()

        if is_valid_choice(board, row, column, candidate):
            board[row][column] = candidate
            stack.append((row, column, candidate))

            cell = next_empty_cell(board, row, column)
            if cell is None:
                break

            next_row, next_column = cell
            stack.append((next_row, next_column, 1))
            continue

        # Invalid choice
        board[row][column] = 0

        if candidate < 9:
            stack.append((row, column, candidate + 1))
            continue

        # Backtrack
        while True:
            prev_row, prev_column, prev_candidate = stack.pop()
            board[prev_row][prev_column] = 0
            if prev_candidate < 9:
                stack.append((prev_row, prev_column, prev_candidate + 1))
                break

    return board


def next_empty_cell(board: Board, start_row: int, start_column: int) -> Nullable[Tuple[int, int]]:
    for row in range(start_row, 9):
        shifted_start_column = start_column if row == start_row else 0
        for column in range(shifted_start_column, 9):
            if board[row][column] == 0:
                return (row, column)
    return None


def is_valid_choice(board: Board, target_row: int, target_column: int, target_number: int) -> bool:
    row, column, box = get_cell_groups(board, target_row, target_column)
    index_in_row = target_column
    index_in_column = target_row
    index_in_box = (3 * (target_row % 3)) + (target_column % 3)
    is_valid_row = is_valid_choice_in_group(row, index_in_row, target_number)
    is_valid_column = is_valid_choice_in_group(column, index_in_column, target_number)
    is_valid_box = is_valid_choice_in_group(box, index_in_box, target_number)
    return is_valid_row and is_valid_column and is_valid_box


def get_cell_groups(board: Board, cell_row: int, cell_column: int) -> Tuple[List[int], List[int], List[int]]:
    row_group = list(board[cell_row])
    column_group = [row[cell_column] for row in board]

    box_row = 3 * (cell_row // 3)
    box_column = 3 * (cell_column // 3)
    box_group = []
    for row_offset in range(3):
        for column_offset in range(3):
            box_group.append(board[box_row + row_offset][box_column + column_offset])

    return (row_group, column_group, box_group)


def is_valid_choice_in_group(group: List[int], target_index: int, target_number: int) -> bool:
    group_nums = set()
    group_sum = 0
    for i, cell in enumerate(group):
        num = target_number if i == target_index else cell
        if num in group_nums:
            return False
        if num != 0:
            group_nums.add(num)
        group_sum += num

    return len(group_nums) < 9 or (len(group_nums) == 9 and group_sum == 45)
