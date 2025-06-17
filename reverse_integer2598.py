# Solution for LeetCode problem: Reverse Integer2598

"""
Reverse Integer (LeetCode #7)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Time Complexity: O(log x) where x is the input number
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
            
        # Apply sign and check bounds
        result = sign * reversed_num
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result
