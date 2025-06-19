# Solution for LeetCode problem: Merge Intervals

def solution():
    """
    Merge Intervals (LeetCode 56).
    Usage: Call merge(intervals) where intervals is a List[List[int]].
    Returns a list of merged intervals.
    """
    def merge(intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged
    # Example usage:
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # print(merge(intervals)) # Output: [[1,6],[8,10],[15,18]]
    pass
