"""
Balanced Binary Search Tree (LeetCode #1382)

Given a binary search tree, return a balanced binary search tree with the same node values. A balanced binary search tree is a binary search tree in which the depth of the two subtrees of every node never differs by more than 1.

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) for storing the inorder traversal
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node: TreeNode | None) -> list[int]:
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def build_balanced_bst(values: list[int], left: int, right: int) -> TreeNode:
            if left > right:
                return TreeNode()
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = build_balanced_bst(values, left, mid - 1)
            node.right = build_balanced_bst(values, mid + 1, right)
            return node
        
        values = inorder(root)
        return build_balanced_bst(values, 0, len(values) - 1)
