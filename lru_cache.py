# Solution for LeetCode problem: Lru Cache

def solution():
    """
    Implements an LRU Cache. Example usage:
    cache = LRUCache(capacity)
    cache.put(key, value)
    value = cache.get(key)
    """
    from collections import OrderedDict
    class LRUCache:
        def __init__(self, capacity: int):
            self.cache = OrderedDict()
            self.capacity = capacity
        def get(self, key: int) -> int:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]
        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    # Example usage:
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1)) # returns 1
    # cache.put(3, 3)     # evicts key 2
    # print(cache.get(2)) # returns -1
    pass
