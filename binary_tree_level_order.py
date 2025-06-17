"""
Binary Tree Level Order Traversal (LeetCode #102)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) for storing the queue
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
