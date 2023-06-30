from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = head = ListNode(None)

        result = []
        for l_list in lists:
            while l_list:
                result.append(l_list.val)
                l_list = l_list.next
        result.sort()

        for val in result:
            new = ListNode(val)
            head.next = new
            head = new
        
        return root.next
