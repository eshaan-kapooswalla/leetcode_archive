"""
Binary Tree Inorder Traversal (LeetCode #94)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def inorder(node: TreeNode | None) -> None:
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result
