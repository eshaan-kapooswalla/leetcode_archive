"""
Two Sum (LeetCode #1)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) for the hash map
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store number -> index mapping
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If complement exists in map, we found our pair
            if complement in num_map:
                return [num_map[complement], i]
                
            # Store current number and its index
            num_map[num] = i
            
        return []  # No solution found
