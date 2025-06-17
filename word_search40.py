"""
Word Search (LeetCode #79)

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Time Complexity: O(m * n * 4^L) where m,n are dimensions of board and L is length of word
Space Complexity: O(L) for recursion stack
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not word:
            return False
            
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, word_idx: int) -> bool:
            if word_idx == len(word):
                return True
                
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[word_idx]):
                return False
                
            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Try all 4 directions
            result = (dfs(r+1, c, word_idx+1) or
                     dfs(r-1, c, word_idx+1) or
                     dfs(r, c+1, word_idx+1) or
                     dfs(r, c-1, word_idx+1))
            
            # Backtrack
            board[r][c] = temp
            return result
            
        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
