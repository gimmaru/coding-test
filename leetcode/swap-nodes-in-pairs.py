from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        b = head
        if head and head.next:
            b = head.next
            head.next = b.next
            head.next = self.swapPairs(head.next)
            b.next = head
        return b
