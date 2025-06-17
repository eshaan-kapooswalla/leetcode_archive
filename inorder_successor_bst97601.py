"""
Inorder Successor in BST (LeetCode #285)

Given the root of a binary search tree and a node p in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Time Complexity: O(h), where h is the height of the tree
Space Complexity: O(1)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderSuccessor(self, root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
