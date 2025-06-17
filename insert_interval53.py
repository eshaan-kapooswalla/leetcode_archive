"""
Insert Interval (LeetCode #57)

You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] sorted by start_i and a new interval newInterval = [start, end].
Insert newInterval into intervals such that intervals is still sorted by start_i and non-overlapping (merge if necessary).

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        # Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        # Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
