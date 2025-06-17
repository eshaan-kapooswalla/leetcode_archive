"""
Generate Parentheses (LeetCode #22)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Time Complexity: O(4^n / sqrt(n))
Space Complexity: O(4^n / sqrt(n))
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack()
        return res
