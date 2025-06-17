"""
Decode Ways (LeetCode #91)

A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

Given a string s containing only digits, return the number of ways to decode it.

Time Complexity: O(n) where n is the length of the input string
Space Complexity: O(n) for the dp array
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has one way to decode
        dp[1] = 1  # First character has one way to decode if not '0'
        
        for i in range(2, n + 1):
            # Check if single digit is valid
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Check if two digits are valid
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
