"""
Longest Common Prefix (LeetCode #14)

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Time Complexity: O(S) where S is the sum of all characters in all strings
Space Complexity: O(1) as we only store the result
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # Find the shortest string
        shortest = min(strs, key=len)
        
        # Check each character position
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
                    
        return shortest
