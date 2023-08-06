from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node or not node.next:
            return node

        right = p = node
        while p and p.next:
            left = right
            right = right.next
            p = p.next.next
        left.next = None
        left = node
        
        left = self.sortList(left)
        right = self.sortList(right)

        if left.val > right.val:
            root = node = right
            oppo = left
        else:
            root = node = left
            oppo = right
        
        while node and oppo:
            while node and node.val <= oppo.val:
                prev = node
                node = node.next
            node = prev

            temp = node.next
            node.next = oppo
            oppo = temp
            node = node.next
        
        return root

'''
* 책에 나온 풀이
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1 or l2
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        lst = []
        while p1:
            lst.append(p1.val)
            p1 = p1.next
        
        lst.sort()

        for i in range(len(lst)):
            p2.val = lst[i]
            p2 = p2.next
        return head