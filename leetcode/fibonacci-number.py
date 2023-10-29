import collections


class Solution:
    fb = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n < 2:
            return n

        if self.fb[n] != 0:
            return self.fb[n]

        self.fb[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.fb[n]

class Solution:
    def fib(self, n: int) -> int:
        fb = [0, 1]

        for i in range(2, n + 1):
            fb.append(fb[i-1] + fb[i-2])
        return fb[n]

# 답지 풀이
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x

# log(n)
import numpy as np

def fib(n):
    M = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])

    return np.matmul(M ** n, vec)[0]