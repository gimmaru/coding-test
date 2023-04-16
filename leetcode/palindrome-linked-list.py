from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        if head.next is None:
            return True

        rev = None
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast is not None:
            slow = slow.next

        while slow is not None:
            result = slow.val == rev.val
            if not result:
                return result
            slow, rev = slow.next, rev.next

        return result