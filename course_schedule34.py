"""
Course Schedule (LeetCode #207)

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
Space Complexity: O(V + E) for the adjacency list and recursion stack
"""

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        
        def hasCycle(course: int) -> bool:
            if visited[course] == 1:  # Cycle detected
                return True
            if visited[course] == 2:  # Already visited
                return False
            
            visited[course] = 1  # Mark as visiting
            
            # Check all neighbors
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True
            
            visited[course] = 2  # Mark as visited
            return False
        
        # Check each course for cycles
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True
