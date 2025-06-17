"""
Kth Smallest Element in a BST (LeetCode #230)

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Time Complexity: O(h + k) where h is the height of the tree
Space Complexity: O(h) for the recursion stack
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)
        
        self.count = 0
        self.result = 0  # Initialize with a default value
        inorder(root)
        return self.result
