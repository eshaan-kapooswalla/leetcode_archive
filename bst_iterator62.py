"""
Binary Search Tree Iterator (LeetCode #173)

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST).

Time Complexity: 
- Constructor: O(h) where h is the height of the tree
- next(): O(1) amortized
- hasNext(): O(1)

Space Complexity: O(h) where h is the height of the tree for the stack
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node: Optional[TreeNode]) -> None:
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
