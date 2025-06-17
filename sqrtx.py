"""
Sqrt(x) (LeetCode #69)

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Time Complexity: O(log x) using binary search
Space Complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right  # Return right as it will be the floor value
