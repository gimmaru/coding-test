from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        node = root = self.insertionSortList(head.next)

        prev = None
        while node and head.val > node.val:
            prev, node = node, node.next
        
        if prev:
            head.next, prev.next = node, head
        else:
            head.next, root = root, head

        return root

'''
* 책에 나온 풀이
'''
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next  # *

            # 최적화
            if head and cur.val > head.val:
                cur = parent
        return parent.next
