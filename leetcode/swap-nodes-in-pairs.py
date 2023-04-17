from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head and head.next:
    #         temp = ListNode(head.val, head.next.next)
    #         head = head.next
    #         head.next = temp
    #         head.next.next = self.swapPairs(head.next.next)
    #     return head
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next
