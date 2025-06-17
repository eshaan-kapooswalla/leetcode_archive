"""
Word Ladder (LeetCode #127)

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList.

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Time Complexity: O(N * 26 * L) where N is the number of words and L is the length of each word
Space Complexity: O(N) for the queue and visited set
"""

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to set for O(1) lookups
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        # Initialize queue with beginWord and its level
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, level = queue.popleft()
            
            # Try changing each character
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    # If we found the end word
                    if next_word == endWord:
                        return level + 1
                        
                    # If the word is valid and not visited
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
                        
        return 0
