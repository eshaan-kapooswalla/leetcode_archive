# Solution for LeetCode problem: Longest Palindromic31

"""
Longest Palindromic Substring (LeetCode #5)

Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same backward as forward.

Time Complexity: O(n²) where n is the length of the string
Space Complexity: O(1) as we only store the result
"""

def solution():
    """
    Longest Palindromic Substring (LeetCode 5).
    Usage: Call longestPalindrome(s) where s is a string.
    Returns the longest palindromic substring in s.
    """
    def longestPalindrome(s):
        if not s:
            return ""
        start = 0
        max_len = 1
        def expand_around_center(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)
        return s[start:start + max_len]
    # Example usage:
    # print(longestPalindrome("babad")) # Output: "bab" or "aba"
    pass

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        start = 0
        max_len = 1
        
        def expand_around_center(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
                
        for i in range(len(s)):
            # Check odd length palindromes
            expand_around_center(i, i)
            # Check even length palindromes
            expand_around_center(i, i + 1)
            
        return s[start:start + max_len]
