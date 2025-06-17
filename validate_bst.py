"""
Validate Binary Search Tree (LeetCode #98)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None, min_val: float, max_val: float) -> bool:
            # Empty trees are valid BSTs
            if not node:
                return True
                
            # Check if current node's value is within valid range
            if not (min_val < node.val < max_val):
                return False
                
            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
                    
        return validate(root, float('-inf'), float('inf'))
