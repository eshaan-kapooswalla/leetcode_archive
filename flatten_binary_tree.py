"""
Flatten Binary Tree to Linked List (LeetCode #114)

Given the root of a binary tree, flatten the tree into a linked list in-place.
The linked list should use the same TreeNode class, where the right child points to the next node in the list and the left child is always None.

Time Complexity: O(n)
Space Complexity: O(1) (if using Morris traversal), otherwise O(n) for recursion stack
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Do not return anything, modify root in-place instead."""
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                # Relink right subtree
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
