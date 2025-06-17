"""
269. Alien Dictionary
Given a list of words sorted lexicographically in an alien language, return a string of the unique letters in the correct order. If no valid order exists, return an empty string.

Time Complexity: O(N * L), where N is the number of words and L is the average word length.
Space Complexity: O(1), since the alphabet size is fixed (26).
"""
from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    order = []
    while queue:
        c = queue.popleft()
        order.append(c)
        for nei in graph[c]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    return "".join(order) if len(order) == len(in_degree) else ""
