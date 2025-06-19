"""
Insert Delete GetRandom O(1) (LeetCode #380)

Implement the RandomizedSet class:
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements. Each element must have the same probability of being returned.

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

import random

class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.val_to_idx[last] = idx
        self.nums.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

def solution():
    """
    Insert Delete GetRandom O(1) (LeetCode 380).
    Usage: Create RandomizedSet(), then use insert(val), remove(val), and getRandom().
    Implements O(1) insert, remove, and getRandom operations.
    """
    # Example usage:
    # rs = RandomizedSet()
    # rs.insert(1)
    # rs.remove(2)
    # rs.insert(2)
    # rs.getRandom()
    pass
