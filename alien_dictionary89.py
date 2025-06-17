"""
Alien Dictionary (LeetCode #269)

There is a new alien language that uses the English alphabet. However, the order among letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Time Complexity: O(N + K) where N is the total number of characters in words and K is the number of unique letters.
Space Complexity: O(K)
"""

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return "".join(res) if len(res) == len(indegree) else ""
