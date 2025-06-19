"""
Graph Valid Tree (LeetCode #261)

Given n nodes labeled from 0 to n - 1 and a list of undirected edges, write a function to check whether these edges make up a valid tree.

A valid tree must be connected and acyclic.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def solution():
    """
    Graph Valid Tree (LeetCode 261).
    Usage: Call validTree(n, edges) where n is the number of nodes and edges is a list of edges.
    Returns True if the edges form a valid tree, False otherwise.
    """
    def validTree(n, edges):
        if len(edges) != n - 1:
            return False
        parent = [i for i in range(n)]
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pu] = pv
        return True
    # Example usage:
    # print(validTree(5, [[0,1],[0,2],[0,3],[1,4]])) # Output: True
    pass
