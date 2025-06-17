"""
Lowest Common Ancestor of a Binary Search Tree (LeetCode #235)

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants.

Time Complexity: O(h) where h is the height of the tree
Space Complexity: O(1) as we only use a constant amount of extra space
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
