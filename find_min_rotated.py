"""
Find Minimum in Rotated Sorted Array (LeetCode #153)

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Time Complexity: O(log n) where n is the length of the array
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # If array is not rotated
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right element,
            # minimum must be in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than right element,
            # minimum must be in left half including mid
            else:
                right = mid
        
        return nums[left]
