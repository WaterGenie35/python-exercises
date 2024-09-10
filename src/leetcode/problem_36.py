from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    Solution to LeetCode problem
    https://neetcode.io/problems/valid-sudoku
    https://leetcode.com/problems/valid-sudoku/

    Check if the sudoku board is valid.
    Note the board does not necessarily have to be full or solvable.
    An empty cell is represented by '.'.
    """
    for k in range(0, 9):
        row = set()
        for i in range(0, 9):
            cell = board[k][i]
            if cell == '.':
                continue
            if cell in row:
                return False
            row.add(cell)

        column = set()
        for i in range(0, 9):
            cell = board[i][k]
            if cell == '.':
                continue
            if cell in column:
                return False
            column.add(cell)

        box = set()
        for i in range(0, 9):
            start_row = 3 * (k // 3)
            start_col = 3 * (k % 3)
            cell_row = start_row + (i // 3)
            cell_col = start_col + (i % 3)
            cell = board[cell_row][cell_col]
            if cell == '.':
                continue
            if cell in box:
                return False
            box.add(cell)

    return True


def test_solution():
    assert is_valid_sudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    assert not is_valid_sudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
