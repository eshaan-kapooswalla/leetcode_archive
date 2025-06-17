"""
Sort Colors (LeetCode #75)

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as we sort in-place
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers for the three colors
        left = 0  # points to the end of 0s
        mid = 0   # current element
        right = len(nums) - 1  # points to the start of 2s
        
        while mid <= right:
            if nums[mid] == 0:
                # Swap with left pointer and move both pointers
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                # Just move mid pointer
                mid += 1
            else:  # nums[mid] == 2
                # Swap with right pointer and move right pointer
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
