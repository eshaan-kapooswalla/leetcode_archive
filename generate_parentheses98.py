"""
Generate Parentheses (LeetCode #22)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Time Complexity: O(4^n / sqrt(n))
Space Complexity: O(4^n / sqrt(n))
"""

from typing import List

def solution():
    """
    Generate Parentheses (LeetCode 22).
    Usage: Call generateParenthesis(n) where n is the number of pairs.
    Returns all combinations of well-formed parentheses.
    """
    def generateParenthesis(n):
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
    # Example usage:
    # print(generateParenthesis(3)) # Output: ["((()))","(()())","(())()","()(())","()()()"]
    pass

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
