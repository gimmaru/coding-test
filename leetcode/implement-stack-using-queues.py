from collections import deque

class MyStack:

    def __init__(self):
        self.Q1, self.Q2 = deque(), deque()

    def push(self, x: int) -> None:
        while self.Q1:
            self.Q2.append(self.Q1.popleft())
        
        self.Q1.append(x)

        while self.Q2:
            self.Q1.append(self.Q2.popleft())

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            return self.Q1.popleft()

    def top(self) -> int:
        return self.Q1[0]

    def empty(self) -> bool:
        return False if self.Q1 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
