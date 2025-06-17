"""
2. Add Two Numbers
Given two non-empty linked lists representing two non-negative integers in reverse order, add the two numbers and return the sum as a linked list. Each node contains a single digit. Return the sum as a linked list.

Time Complexity: O(n), where n is the length of the longer list.
Space Complexity: O(n), for the output list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next
