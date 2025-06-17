"""
Serialize and Deserialize Binary Tree (LeetCode #297)

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
be serialized to a string and this string can be deserialized to the original tree structure.

Time Complexity: O(n) for both serialization and deserialization
Space Complexity: O(n) for both serialization and deserialization
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        if not root:
            return "None"
            
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> TreeNode | None:
        def helper(values: list[str]) -> TreeNode | None:
            val = values.pop(0)
            if val == "None":
                return None
                
            node = TreeNode(int(val))
            node.left = helper(values)
            node.right = helper(values)
            return node
            
        return helper(data.split(","))
