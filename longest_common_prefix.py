"""
Longest Common Prefix (LeetCode #14)

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Time Complexity: O(S) where S is the sum of all characters in all strings
Space Complexity: O(1) as we only store the result
"""

def solution():
    """
    Longest Common Prefix (LeetCode 14).
    Usage: Call longestCommonPrefix(strs) where strs is a list of strings.
    Returns the longest common prefix string among the array.
    """
    def longestCommonPrefix(strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        return shortest
    # Example usage:
    # print(longestCommonPrefix(["flower","flow","flight"])) # Output: "fl"
    pass
