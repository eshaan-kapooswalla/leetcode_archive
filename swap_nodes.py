# Solution for LeetCode problem: Swap Nodes

"""
Swap Nodes in Pairs (LeetCode #24)

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

Time Complexity: O(n) where n is the number of nodes in the linked list
Space Complexity: O(1) as we only use a few pointers
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0, head)
        prev = dummy
        
        while head and head.next:
            # Store the nodes to be swapped
            first = head
            second = head.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers for next iteration
            prev = first
            head = first.next
            
        return dummy.next

def solution():
    pass
