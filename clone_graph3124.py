"""
Clone Graph (LeetCode #133)

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
Space Complexity: O(V) for the hash map and recursion stack
"""

from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to store the mapping between original and cloned nodes
        visited = {}
        
        def dfs(original: Node) -> Node:
            if original in visited:
                return visited[original]
            
            # Create a new node
            clone = Node(original.val)
            visited[original] = clone
            
            # Clone all neighbors
            clone.neighbors = [dfs(neighbor) for neighbor in original.neighbors]
            
            return clone
        
        return dfs(node)
