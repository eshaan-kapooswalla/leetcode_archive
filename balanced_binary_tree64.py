"""
Balanced Binary Tree (LeetCode #110)

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node: TreeNode | None) -> int:
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return height(root) != -1
