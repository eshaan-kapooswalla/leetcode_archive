"""
Binary Tree Paths (LeetCode #257)

Given the root of a binary tree, return all root-to-leaf paths in any order.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        result = []
        def dfs(node: TreeNode, path: str) -> None:
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            if node.left:
                dfs(node.left, path + str(node.val) + "->")
            if node.right:
                dfs(node.right, path + str(node.val) + "->")
        dfs(root, "")
        return result
