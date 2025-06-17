"""
Unique Paths (LeetCode #62)

A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?

Time Complexity: O(m * n) where m and n are the dimensions of the grid
Space Complexity: O(m * n) for the DP table
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a DP table initialized with 1s
        dp = [[1] * n for _ in range(m)]
        
        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]
