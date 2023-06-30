class ChainNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hash_func = lambda x: x % 773
        self.table = [None] * 773
    
    def _get_hashval(self, key):
        return self.hash_func(key)

    def put(self, key: int, value: int) -> None:
        hashval = self._get_hashval(key)
        root = chain = self.table[hashval]

        node = ChainNode(key, value)
        while chain and key != chain.key:
            chain = chain.next
        
        if chain:
            chain.value = value
            # self.table[hashval] = root
        else:
            node.next = root
            self.table[hashval] = node

    def get(self, key: int) -> int:
        hashval = self._get_hashval(key)
        chain = self.table[hashval]

        while chain and key != chain.key:
            chain = chain.next
        
        return chain.value if chain else -1

    def remove(self, key: int) -> None:
        hashval = self._get_hashval(key)
        chain = self.table[hashval]

        if chain:
            if key == chain.key:
                self.table[hashval] = chain.next
                return None
            
            while chain.next:
                if key == chain.next.key:
                    chain.next = chain.next.next
                    break

                chain = chain.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


'''
책에 나온 풀이
'''
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)