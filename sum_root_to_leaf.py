"""
Sum Root to Leaf Numbers (LeetCode #129)

You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
Return the total sum of all root-to-leaf numbers.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, current_sum: int) -> int:
            if not node:
                return 0
                
            # Update current sum
            current_sum = current_sum * 10 + node.val
            
            # If leaf node, return the number
            if not node.left and not node.right:
                return current_sum
                
            # Recursively get sum from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
            
        return dfs(root, 0)
