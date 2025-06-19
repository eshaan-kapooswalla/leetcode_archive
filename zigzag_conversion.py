"""
Zigzag Conversion (LeetCode #6)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Time Complexity: O(n) where n is the length of the input string
Space Complexity: O(n) to store the result
"""

def solution():
    """
    Zigzag Conversion (LeetCode 6).
    Usage: Call convert(s, numRows) where s is a string and numRows is an int.
    Returns the zigzag converted string.
    """
    def convert(s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(rows)
    # Example usage:
    # print(convert("PAYPALISHIRING", 3)) # Output: "PAHNAPLSIIGYIR"
    pass
