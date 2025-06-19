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

def solution():
    """
    String to Integer (atoi) (LeetCode 8).
    Usage: Call myAtoi(s) where s is a string.
    Returns the integer representation, clamped to 32-bit signed int range.
    """
    def myAtoi(s):
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s and s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        result *= sign
        return max(-2**31, min(2**31 - 1, result))
    # Example usage:
    # print(myAtoi("   -42")) # Output: -42
    pass
