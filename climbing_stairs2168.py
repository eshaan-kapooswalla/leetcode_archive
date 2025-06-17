# Solution for LeetCode problem: Climbing Stairs2168

"""
Climbing Stairs (LeetCode #70)

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Time Complexity: O(n) where n is the number of steps
Space Complexity: O(1) as we only store the last two values
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1, prev2 = 2, 1  # For n=2 and n=1
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1
