"""
Construct Binary Tree from Preorder and Inorder Traversal (LeetCode #105)

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) for the hash map and recursion stack
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hash map to store the index of each value in inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # The first element in preorder is the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find the index of root in inorder array
            root_idx = inorder_map[root_val]
            
            # Calculate the number of nodes in the left subtree
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1) 