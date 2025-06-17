"""
Set Matrix Zeroes (LeetCode #73)

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Time Complexity: O(m*n) where m and n are the dimensions of the matrix
Space Complexity: O(1)
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return
            
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
                
        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
                
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # Set first row to zero if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # Set first column to zero if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
