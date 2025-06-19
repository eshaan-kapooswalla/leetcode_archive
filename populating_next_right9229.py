# Solution for LeetCode problem: Populating Next Right9229

def solution():
    """
    Populating Next Right Pointers in Each Node (LeetCode 116/117).
    Usage: Create a Node class with .val, .left, .right, .next attributes.
    Call connect(root) to populate .next pointers.
    """
    class Node:
        def __init__(self, val=0, left=None, right=None, next=None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next
    def connect(root):
        if not root:
            return None
        leftmost = root
        while leftmost:
            curr = leftmost
            prev = leftmost = None
            while curr:
                for child in (curr.left, curr.right):
                    if child:
                        if prev:
                            prev.next = child
                        else:
                            leftmost = child
                        prev = child
                curr = curr.next
        return root
    # Example usage:
    # root = Node(1, Node(2), Node(3))
    # connect(root)
    pass
