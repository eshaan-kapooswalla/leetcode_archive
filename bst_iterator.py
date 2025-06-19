# Solution for LeetCode problem: Bst Iterator

def solution():
    """
    Implements a BST Iterator. Example usage:
    iterator = BSTIterator(root)
    val = iterator.next()
    has_next = iterator.hasNext()
    """
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    class BSTIterator:
        def __init__(self, root):
            self.stack = []
            self._leftmost_inorder(root)
        def _leftmost_inorder(self, root):
            while root:
                self.stack.append(root)
                root = root.left
        def next(self) -> int:
            topmost_node = self.stack.pop()
            if topmost_node.right:
                self._leftmost_inorder(topmost_node.right)
            return topmost_node.val
        def hasNext(self) -> bool:
            return len(self.stack) > 0
    # Example usage:
    # root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    # iterator = BSTIterator(root)
    # print(iterator.next())    # returns 3
    # print(iterator.next())    # returns 7
    # print(iterator.hasNext()) # returns True
    # print(iterator.next())    # returns 9
    # print(iterator.hasNext()) # returns True
    # print(iterator.next())    # returns 15
    # print(iterator.hasNext()) # returns True
    # print(iterator.next())    # returns 20
    # print(iterator.hasNext()) # returns False
    pass
