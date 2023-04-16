from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        
        result = list()
        while list1 and list2:
            if list1.val <= list2.val:
                result.append(list1.val)
                list1 = list1.next
            else:
                result.append(list2.val)
                list2 = list2.next
        
        while list1:
            result.append(list1.val)
            list1 = list1.next
        
        while list2:
            result.append(list2.val)
            list2 = list2.next
        
        ll_result = None
        for v in result:
            if not ll_result:
                ll_result = ListNode(v)
            else:
                ll_result = ListNode(v, ll_result)
        
        return ll_result
            
