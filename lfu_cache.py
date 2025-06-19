"""
LFU Cache (LeetCode #460)

Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or insert the key if not already present.

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity)
"""

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        
    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
            
        freq = self.key_to_freq[key]
        value = self.freq_to_keys[freq][key]
        
        # Remove from current frequency
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
                
        # Add to new frequency
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = value
        
        return value
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_to_freq:
            self.get(key)  # Update frequency
            self.freq_to_keys[self.key_to_freq[key]][key] = value
            return
            
        if len(self.key_to_freq) == self.capacity:
            # Remove least frequently used key
            key_to_remove = next(iter(self.freq_to_keys[self.min_freq]))
            del self.freq_to_keys[self.min_freq][key_to_remove]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]
            del self.key_to_freq[key_to_remove]
            
        # Add new key
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.min_freq = 1

def solution():
    """
    LFU Cache (LeetCode 460).
    Usage: Create LFUCache(capacity), then use get(key) and put(key, value).
    Implements O(1) get and put operations for LFU cache.
    """
    from collections import defaultdict, OrderedDict
    class LFUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.min_freq = 0
            self.key_to_freq = {}
            self.freq_to_keys = defaultdict(OrderedDict)
        def get(self, key: int) -> int:
            if key not in self.key_to_freq:
                return -1
            freq = self.key_to_freq[key]
            value = self.freq_to_keys[freq][key]
            del self.freq_to_keys[freq][key]
            if not self.freq_to_keys[freq]:
                del self.freq_to_keys[freq]
                if freq == self.min_freq:
                    self.min_freq += 1
            self.key_to_freq[key] = freq + 1
            self.freq_to_keys[freq + 1][key] = value
            return value
        def put(self, key: int, value: int) -> None:
            if self.capacity == 0:
                return
            if key in self.key_to_freq:
                self.get(key)
                self.freq_to_keys[self.key_to_freq[key]][key] = value
                return
            if len(self.key_to_freq) == self.capacity:
                key_to_remove = next(iter(self.freq_to_keys[self.min_freq]))
                del self.freq_to_keys[self.min_freq][key_to_remove]
                if not self.freq_to_keys[self.min_freq]:
                    del self.freq_to_keys[self.min_freq]
                del self.key_to_freq[key_to_remove]
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = value
            self.min_freq = 1
    # Example usage:
    # cache = LFUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1)) # Output: 1
    pass
