class Queue:
    def __init__(self):
        self.input, self.output = [], []
    
    def __len__(self):
        return len(self.input) + len(self.output)

    def push(self, value):
        self.input.append(value)

    def pop(self):
        self.peak()
        return self.output.pop()

    def peak(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        if self.isEmpty():
            return -1
        else:
            return self.output[-1]
    
    def bottem(self):
        if self.input:
            return self.input[-1]
        
        if self.output:
            return self.output[0]
        
        return -1

    def isEmpty(self):
        return len(self.input) == 0 and len(self.output) == 0
    


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = Queue()
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q.push(value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q.pop()
            return True

    def Front(self) -> int:
        return self.q.peak()

    def Rear(self) -> int:
        return self.q.bottem()

    def isEmpty(self) -> bool:
        return self.q.isEmpty()

    def isFull(self) -> bool:
        return len(self.q) == self.size


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # 기존 값이 사라질 곳
        self.p2 = 0 # 새로운 값이 들어갈 곳

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.p2 % self.maxlen] = value
            self.p2 += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.p1 % self.maxlen] = None
            self.p1 += 1
            return True
        
    def Front(self) -> int:
        value = self.q[self.p1 % self.maxlen]
        if value is None:
            return -1
        else:
            return value

    def Rear(self) -> int:
        value = self.q[(self.p2-1) % self.maxlen]
        if value is None:
            return -1
        else:
            return value

    def isEmpty(self) -> bool:
        return self.p2 - self.p1 == 0

    def isFull(self) -> bool:
        return self.p2 - self.p1 == self.maxlen


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
