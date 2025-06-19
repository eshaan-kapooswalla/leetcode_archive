# Solution for LeetCode problem: Remove Nth Node9

def solution():
    """
    Remove Nth Node From End of List (LeetCode 19).
    Usage: Define ListNode class, call removeNthFromEnd(head, n).
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def removeNthFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            if fast:
                fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if slow and slow.next:
            slow.next = slow.next.next
        return dummy.next
    # Example usage:
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # new_head = removeNthFromEnd(head, 2)
    pass
