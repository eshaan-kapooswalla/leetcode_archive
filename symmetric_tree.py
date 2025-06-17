"""
Symmetric Tree (LeetCode #101)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
            # If both nodes are None, they are symmetric
            if not left and not right:
                return True
                
            # If one node is None and other isn't, they are not symmetric
            if not left or not right:
                return False
                
            # Check if values are equal and subtrees are mirrors
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))
                    
        return is_mirror(root, root)
