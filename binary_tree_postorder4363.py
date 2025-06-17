# Solution for LeetCode problem: Binary Tree Postorder4363

"""
Binary Tree Postorder Traversal (LeetCode #145)

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def postorder(node: TreeNode | None) -> None:
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        postorder(root)
        return result

def solution():
    pass
