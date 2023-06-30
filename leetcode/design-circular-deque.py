from typing import Optional
from copy import deepcopy

class Block:
    def __init__(self, val: Optional[int] = None):
        self.val = val
        self.r_block = None
        self.l_block = None

class MyCircularDeque:

    def __init__(self, k: int):
        print(f"\nmax length: {k}")
        self.head = Block()
        self.tail = Block()

        self.head.r_block = self.tail
        self.tail.l_block = self.head

        self.maxlen = k
        self.size = 0
    
    def check_status(self):
        head = deepcopy(self.head)
        tail = deepcopy(self.tail)
        result_head, result_tail = "-", "-"
        while head:
            result_head += f"{head.val}-"
            head = head.r_block
        while tail:
            result_tail += f"{tail.val}-"
            tail = tail.l_block
        return result_head, result_tail

    def insertFront(self, value: int) -> bool:
        # print(f"insert front: {self.check_status()}, {value}")
        if self.isFull():
            return False

        if self.head.val is None:
            self.head.val = value
        else:
            new_block = Block(value)
            self.head.l_block = new_block
            new_block.r_block = self.head
            self.head = new_block
        
        self.size += 1
        if self.size >= 2 and self.tail.val is None:
            self.tail = self.tail.l_block

        return True

    def insertLast(self, value: int) -> bool:
        # print(f"insert last: {self.check_status()}, {value}")
        if self.isFull():
            return False

        if self.tail.val is None:
            self.tail.val = value
        else:
            new_block = Block(value)
            self.tail.r_block = new_block
            new_block.l_block = self.tail
            self.tail = new_block
        
        self.size += 1
        if self.size >= 2 and self.head.val is None:
            self.head = self.head.r_block

        return True

    def deleteFront(self) -> bool:
        # print(f"delete front: {self.check_status()}")
        if self.isEmpty():
            return False
        
        if self.head.val is None:
            self.tail.val = None
        elif self.size <= 2:
            self.head.val = None
        else:
            self.head = self.head.r_block
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        # print(f"delete last: {self.check_status()}")
        if self.isEmpty():
            return False
        
        if self.tail.val is None:
            self.head.val = None
        elif self.size <= 2:
            self.tail.val = None
        else:
            self.tail = self.tail.l_block
        self.size -= 1
        return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        elif self.head.val is None:
            return self.tail.val
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        elif self.tail.val is None:
            return self.head.val
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxlen


# 책에 나온 풀이법
'''
새로운 노드를 head와 tail 사이에 추가하고
head와 tail 노드는 양쪽 끝 점을 나타내는 역할
'''
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.right, self.left = None, None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
    
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.right.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.left.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()