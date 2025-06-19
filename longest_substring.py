# Solution for LeetCode problem: Longest Substring

"""
Longest Substring Without Repeating Characters (LeetCode #3)

Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m, n)) where m is the size of the character set
"""

def solution():
    """
    Longest Substring Without Repeating Characters (LeetCode 3).
    Usage: Call lengthOfLongestSubstring(s) where s is a string.
    Returns the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(s):
        if not s:
            return 0
        char_pos = {}
        start = 0
        max_len = 0
        for end, char in enumerate(s):
            if char in char_pos and char_pos[char] >= start:
                start = char_pos[char] + 1
            else:
                max_len = max(max_len, end - start + 1)
            char_pos[char] = end
        return max_len
    # Example usage:
    # print(lengthOfLongestSubstring("abcabcbb")) # Output: 3
    pass
