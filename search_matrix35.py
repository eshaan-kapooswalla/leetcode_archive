# Solution for LeetCode problem: Search Matrix35

"""
Search a 2D Matrix (LeetCode #74)

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Time Complexity: O(log(m*n)) where m and n are the dimensions of the matrix
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
