"""
String to Integer (atoi) (LeetCode #8)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'.
3. Read in next the characters until the next non-digit character or the end of the input is reached.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        s = s.strip()
        if not s:
            return 0
            
        # Check for sign
        sign = 1
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
            
        # Convert digits
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
            
        # Apply sign and clamp
        result *= sign
        return max(-2**31, min(2**31 - 1, result))
