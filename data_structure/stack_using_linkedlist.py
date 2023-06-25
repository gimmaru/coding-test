from copy import deepcopy

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, item):
        self.last = Node(item, self.last)
    
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

    def __str__(self):
        last = deepcopy(self.last)
        string = ""
        while last is not None:
            string += f"-{last.item}"
            last = last.next
        return "None-" + string[::-1][:-1]



if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 6):
        print(f"Push {i} to Stack.")
        stack.push(i)
    print(f"\nStack example:\n{stack}\n")
    
    print("Pop Test")
    for i in range(5):
        print(stack.pop())