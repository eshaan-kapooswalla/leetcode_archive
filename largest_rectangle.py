"""
Largest Rectangle in Histogram (LeetCode #84)

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > (heights[i] if i < n else 0)):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        return max_area

def solution():
    """
    Largest Rectangle in Histogram (LeetCode 84).
    Usage: Call largestRectangleArea(heights) where heights is a list of integers.
    Returns the area of the largest rectangle in the histogram.
    """
    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > (heights[i] if i < n else 0)):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
    # Example usage:
    # print(largestRectangleArea([2,1,5,6,2,3])) # Output: 10
    pass
