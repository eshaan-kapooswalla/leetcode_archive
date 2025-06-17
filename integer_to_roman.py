"""
Integer to Roman (LeetCode #12)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given an integer, convert it to a roman numeral.

Time Complexity: O(1) as the number of iterations is bounded by the number of roman numeral symbols
Space Complexity: O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        res = []
        for value, symbol in values:
            while num >= value:
                res.append(symbol)
                num -= value
        return "".join(res)
