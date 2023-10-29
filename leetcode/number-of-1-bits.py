class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 2:
            return n
        return n % 2 + self.hammingWeight(n // 2)

# 책 풀이를 참고하여 수정
class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return 0
        return 1 + self.hammingWeight(n & (n-1))

'''
* 책에 나온 풀이
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count