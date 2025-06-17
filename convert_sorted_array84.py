"""
Convert Sorted Array to Binary Search Tree (LeetCode #108)

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees
of every node never differs by more than one.

Time Complexity: O(n) where n is the length of the input array
Space Complexity: O(log n) for the recursion stack
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Choose middle element as root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            
            return root
        
        return buildBST(0, len(nums) - 1)
