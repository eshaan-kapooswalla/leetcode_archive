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

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Place each character in the appropriate row
        for char in s:
            rows[current_row] += char
            
            # Change direction if we reach the top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move to next row
            current_row += 1 if going_down else -1
            
        # Join all rows
        return ''.join(rows)
