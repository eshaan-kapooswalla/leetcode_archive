"""
Valid Sudoku (LeetCode #36)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Time Complexity: O(1) since the board size is fixed at 9x9
Space Complexity: O(1) since we use fixed-size sets
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        
        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        num = board[row][col]
                        if num != '.':
                            if num in seen:
                                return False
                            seen.add(num)
        
        return True
