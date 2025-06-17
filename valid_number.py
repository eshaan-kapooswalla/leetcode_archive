"""
Valid Number (LeetCode #65)

A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1. (Optional) A sign character ('+' or '-').
2. One of the following formats:
   a. At least one digit, followed by a dot '.'.
   b. At least one digit, followed by a dot '.', followed by at least one digit.
   c. A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):
1. (Optional) A sign character ('+' or '-').
2. At least one digit.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) as we only use a few variables
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        # Remove leading and trailing whitespace
        s = s.strip()
        
        # Check if string is empty after stripping
        if not s:
            return False
            
        # Flags to track what we've seen
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        # Process each character
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char == '.':
                # Can't have more than one dot or dot after e
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in 'eE':
                # Can't have more than one e or e at start/end
                if seen_e or not seen_digit or i == len(s) - 1:
                    return False
                seen_e = True
                seen_digit = False  # Reset for the exponent part
            elif char in '+-':
                # Signs can only be at start or after e
                if i > 0 and s[i-1] not in 'eE':
                    return False
            else:
                return False
                
        return seen_digit
