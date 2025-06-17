"""
Graph Valid Tree (LeetCode #261)

Given n nodes labeled from 0 to n - 1 and a list of undirected edges, write a function to check whether these edges make up a valid tree.

A valid tree must be connected and acyclic.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
