"""
Container With Most Water (LeetCode #11)

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Time Complexity: O(n) where n is the length of the input array
Space Complexity: O(1) as we only use two pointers
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

def solution():
    """
    Container With Most Water (LeetCode 11).
    Usage: Call maxArea(height) where height is a list of non-negative integers.
    Returns the maximum area of water a container can store.
    """
    def maxArea(height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    # Example usage:
    # print(maxArea([1,8,6,2,5,4,8,3,7])) # Output: 49
    pass
