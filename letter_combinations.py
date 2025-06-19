"""
Letter Combinations of a Phone Number (LeetCode #17)

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

Time Complexity: O(4^n * n) where n is the length of digits
Space Complexity: O(n) for recursion stack
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, path):
            if index == len(digits):
                res.append(''.join(path))
                return
                
            for letter in digit_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        res = []
        backtrack(0, [])
        return res

def solution():
    """
    Letter Combinations of a Phone Number (LeetCode 17).
    Usage: Call letterCombinations(digits) where digits is a string of digits 2-9.
    Returns all possible letter combinations.
    """
    def letterCombinations(digits):
        if not digits:
            return []
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        def backtrack(index, path):
            if index == len(digits):
                res.append(''.join(path))
                return
            for letter in digit_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        res = []
        backtrack(0, [])
        return res
    # Example usage:
    # print(letterCombinations("23")) # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    pass
